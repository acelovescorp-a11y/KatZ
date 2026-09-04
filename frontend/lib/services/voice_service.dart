"""Voice Service for speech input and output."""

import 'package:flutter_tts/flutter_tts.dart';
import 'package:record/record.dart';
import 'dart:async';

/// Voice Service for TTS and speech recognition.
class VoiceService {
  static final VoiceService _instance = VoiceService._internal();

  factory VoiceService() {
    return _instance;
  }

  VoiceService._internal();

  late final FlutterTts _tts;
  late final AudioRecorder _recorder;
  bool _isInitialized = false;
  bool _isRecording = false;

  /// Initialize voice service.
  Future<void> initialize() async {
    try {
      _tts = FlutterTts();
      _recorder = AudioRecorder();

      // Configure TTS
      await _tts.setLanguage('de-DE');
      await _tts.setSpeechRate(0.8);
      await _tts.setVolume(1.0);
      await _tts.setPitch(1.0);

      _isInitialized = true;
    } catch (e) {
      throw Exception('Failed to initialize voice service: $e');
    }
  }

  /// Speak text using text-to-speech.
  Future<void> speak(String text) async {
    try {
      if (!_isInitialized) {
        throw Exception('Voice service not initialized');
      }
      await _tts.speak(text);
    } catch (e) {
      throw Exception('Failed to speak: $e');
    }
  }

  /// Stop current speech.
  Future<void> stop() async {
    try {
      await _tts.stop();
    } catch (e) {
      throw Exception('Failed to stop speech: $e');
    }
  }

  /// Start recording audio.
  Future<String?> startRecording() async {
    try {
      if (!_isInitialized) {
        throw Exception('Voice service not initialized');
      }

      // Check permission
      if (await _recorder.hasPermission()) {
        final path = 'audio_${DateTime.now().millisecondsSinceEpoch}.m4a';
        await _recorder.start(
          path: path,
        );
        _isRecording = true;
        return path;
      } else {
        throw Exception('Microphone permission denied');
      }
    } catch (e) {
      throw Exception('Failed to start recording: $e');
    }
  }

  /// Stop recording audio.
  Future<String?> stopRecording() async {
    try {
      if (!_isInitialized || !_isRecording) {
        throw Exception('Recording not active');
      }

      final path = await _recorder.stop();
      _isRecording = false;
      return path;
    } catch (e) {
      throw Exception('Failed to stop recording: $e');
    }
  }

  /// Check if currently recording.
  bool get isRecording => _isRecording;

  /// Dispose voice service.
  Future<void> dispose() async {
    await _tts.stop();
    await _recorder.dispose();
    _isInitialized = false;
  }
}
