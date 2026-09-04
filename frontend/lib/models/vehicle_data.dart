"""Vehicle Data Model."""

class VehicleData {
  final int? id;
  final String manufacturer;
  final String model;
  final String generation;
  final int yearFrom;
  final int? yearTo;
  final String? engineVariants;

  VehicleData({
    this.id,
    required this.manufacturer,
    required this.model,
    required this.generation,
    required this.yearFrom,
    this.yearTo,
    this.engineVariants,
  });

  factory VehicleData.fromJson(Map<String, dynamic> json) {
    return VehicleData(
      id: json['id'] as int?,
      manufacturer: json['manufacturer'] as String,
      model: json['model'] as String,
      generation: json['generation'] as String,
      yearFrom: json['year_from'] as int,
      yearTo: json['year_to'] as int?,
      engineVariants: json['engine_variants'] as String?,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'manufacturer': manufacturer,
        'model': model,
        'generation': generation,
        'year_from': yearFrom,
        'year_to': yearTo,
        'engine_variants': engineVariants,
      };

  @override
  String toString() =>
      '$manufacturer $model $generation ($yearFrom${yearTo != null ? '-$yearTo' : '-present'})';
}
