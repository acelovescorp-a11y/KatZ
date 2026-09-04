"""OCR Service using Google ML Kit for text recognition."""

import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';
import 'dart:io';
import 'dart:async';

/// OCR Service for text recognition.
class OCRService {
  static final OCRService _instance = OCRService._internal();

  factory OCRService() {
    return _instance;
  }

  OCRService._internal();

  late final TextRecognizer _textRecognizer;
  bool _isInitialized = false;

  /// Initialize OCR service.
  Future<void> initialize() async {
    try {
      _textRecognizer = TextRecognizer(script: TextRecognitionScript.latin);
      _isInitialized = true;
    } catch (e) {
      throw Exception('Failed to initialize OCR: $e');
    }
  }

  /// Recognize text from image file.
  Future<String> recognizeText(String imagePath) async {
    try {
      if (!_isInitialized) {
        throw Exception('OCR service not initialized');
      }

      final inputImage = InputImage.fromFile(File(imagePath));
      final recognizedText = await _textRecognizer.processImage(inputImage);

      return recognizedText.text;
    } catch (e) {
      throw Exception('Failed to recognize text: $e');
    }
  }

  /// Extract part numbers from text using regex.
  List<String> extractPartNumbers(String text) {
    // Regex pattern: 2-4 alphanumeric characters followed by 3-7 digits
    final regex = RegExp(r'\b[A-Z0-9]{2,4}\s?[0-9]{3,7}\b', caseSensitive: false);
    return regex.allMatches(text).map((match) => match.group(0)!).toList();
  }

  /// Dispose OCR service.
  Future<void> dispose() async {
    await _textRecognizer.close();
    _isInitialized = false;
  }
}
