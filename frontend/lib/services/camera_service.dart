"""Camera Service for vehicle and OCR scanning."""

import 'package:camera/camera.dart';
import 'dart:async';

/// Camera Service for managing camera operations.
class CameraService {
  static final CameraService _instance = CameraService._internal();

  factory CameraService() {
    return _instance;
  }

  CameraService._internal();

  CameraController? _controller;
  List<CameraDescription> _cameras = [];
  bool _isInitialized = false;

  /// Check if camera service is initialized.
  bool get isInitialized => _isInitialized && _controller?.value.isInitialized == true;

  /// Get camera controller.
  CameraController? get controller => _controller;

  /// Initialize camera service.
  Future<void> initialize() async {
    try {
      _cameras = await availableCameras();
      if (_cameras.isEmpty) {
        throw Exception('No cameras available');
      }

      // Use rear camera by default
      final rearCamera = _cameras.firstWhere(
        (camera) => camera.lensDirection == CameraLensDirection.back,
        orElse: () => _cameras[0],
      );

      _controller = CameraController(
        rearCamera,
        ResolutionPreset.high,
        enableAudio: false,
      );

      await _controller!.initialize();
      _isInitialized = true;
    } catch (e) {
      throw Exception('Failed to initialize camera: $e');
    }
  }

  /// Take a picture.
  Future<XFile?> takePicture() async {
    try {
      if (!isInitialized) {
        throw Exception('Camera not initialized');
      }
      return await _controller!.takePicture();
    } catch (e) {
      throw Exception('Failed to take picture: $e');
    }
  }

  /// Dispose camera service.
  Future<void> dispose() async {
    await _controller?.dispose();
    _isInitialized = false;
  }
}
