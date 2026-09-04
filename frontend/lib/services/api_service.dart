"""API Service for backend communication."""

import 'package:dio/dio.dart';
import '../config/app_config.dart';

/// API Service for communicating with KatZ backend.
class APIService {
  static final APIService _instance = APIService._internal();

  factory APIService() {
    return _instance;
  }

  APIService._internal();

  late final Dio _dio;
  bool _isInitialized = false;

  /// Initialize API service.
  void initialize() {
    if (_isInitialized) return;

    _dio = Dio(
      BaseOptions(
        baseUrl: '${Config.apiBaseUrl}${Config.apiVersion}',
        connectTimeout: Duration(milliseconds: Config.apiTimeout),
        receiveTimeout: Duration(milliseconds: Config.apiTimeout),
        contentType: 'application/json',
      ),
    );

    _isInitialized = true;
  }

  /// Scan vehicle from image.
  Future<Map<String, dynamic>> scanVehicle(String imagePath) async {
    try {
      final formData = FormData.fromMap({
        'file': await MultipartFile.fromFile(imagePath),
      });

      final response = await _dio.post(
        '/scan/vehicle',
        data: formData,
      );

      return response.data as Map<String, dynamic>;
    } catch (e) {
      throw Exception('Failed to scan vehicle: $e');
    }
  }

  /// Scan OCR (part number).
  Future<Map<String, dynamic>> scanOCR(String imagePath) async {
    try {
      final formData = FormData.fromMap({
        'file': await MultipartFile.fromFile(imagePath),
      });

      final response = await _dio.post(
        '/scan/ocr',
        data: formData,
      );

      return response.data as Map<String, dynamic>;
    } catch (e) {
      throw Exception('Failed to scan OCR: $e');
    }
  }

  /// Voice query.
  Future<Map<String, dynamic>> voiceQuery(String queryText) async {
    try {
      final response = await _dio.post(
        '/voice/query',
        queryParameters: {'text': queryText},
      );

      return response.data as Map<String, dynamic>;
    } catch (e) {
      throw Exception('Failed to process voice query: $e');
    }
  }
}
