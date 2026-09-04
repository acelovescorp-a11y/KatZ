"""Configuration module."""

abstract final class Config {
  /// API Configuration
  static const String apiBaseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'http://localhost:8000',
  );

  static const String apiVersion = '/api/v1';

  /// App Configuration
  static const String appName = 'KatZ';
  static const String appVersion = '0.1.0';
  static const String appDescription =
      'Vision & Voice Katalysator-Wert-App';

  /// Feature Flags
  static const bool enableLogging = true;
  static const bool enableCrashReporting = false;
  static const bool enableAnalytics = false;

  /// Timeouts (in milliseconds)
  static const int apiTimeout = 30000;
  static const int cameraTimeout = 5000;
  static const int voiceTimeout = 30000;

  /// UI Configuration
  static const Duration animationDuration = Duration(milliseconds: 300);
  static const double cornerRadius = 12.0;
  static const double defaultPadding = 16.0;
}
