"""Scan Response Model."""

class ScanResponse {
  final String vehicleManufacturer;
  final String vehicleModel;
  final String vehicleGeneration;
  final int catalystCount;
  final double minPriceEur;
  final double maxPriceEur;
  final String voiceMessage;
  final String? message;

  ScanResponse({
    required this.vehicleManufacturer,
    required this.vehicleModel,
    required this.vehicleGeneration,
    required this.catalystCount,
    required this.minPriceEur,
    required this.maxPriceEur,
    required this.voiceMessage,
    this.message,
  });

  factory ScanResponse.fromJson(Map<String, dynamic> json) {
    return ScanResponse(
      vehicleManufacturer: json['vehicle_manufacturer'] as String,
      vehicleModel: json['vehicle_model'] as String,
      vehicleGeneration: json['vehicle_generation'] as String,
      catalystCount: json['catalyst_count'] as int,
      minPriceEur: (json['min_price_eur'] as num).toDouble(),
      maxPriceEur: (json['max_price_eur'] as num).toDouble(),
      voiceMessage: json['voice_message'] as String,
      message: json['message'] as String?,
    );
  }

  Map<String, dynamic> toJson() => {
        'vehicle_manufacturer': vehicleManufacturer,
        'vehicle_model': vehicleModel,
        'vehicle_generation': vehicleGeneration,
        'catalyst_count': catalystCount,
        'min_price_eur': minPriceEur,
        'max_price_eur': maxPriceEur,
        'voice_message': voiceMessage,
        'message': message,
      };
}
