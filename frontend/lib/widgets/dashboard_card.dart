import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';

class DashboardCard extends StatelessWidget {
  final Map<String, dynamic> entry;

  const DashboardCard({Key? key, required this.entry}) : super(key: key);

  String _buildTitle() {
    final m = entry['vehicle_manufacturer'] ?? '';
    final mod = entry['vehicle_model'] ?? '';
    return '$m $mod'.trim();
  }

  @override
  Widget build(BuildContext context) {
    final flutterTts = FlutterTts();
    final title = _buildTitle();
    final minPrice = entry['min_price_eur'] ?? 0;
    final maxPrice = entry['max_price_eur'] ?? 0;
    final note = entry['note'] ?? '';

    return Semantics(
      container: true,
      label: 'Scan entry $title. Preis von $minPrice bis $maxPrice Euro. $note',
      child: Card(
        margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        child: Padding(
          padding: const EdgeInsets.all(12.0),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title.isEmpty ? 'Unbekanntes Fahrzeug' : title,
                      style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
                    ),
                    const SizedBox(height: 6),
                    Text('Kats: ${entry['catalyst_count'] ?? 0}'),
                    const SizedBox(height: 6),
                    Text('Preis: €$minPrice – €$maxPrice'),
                    if (note.isNotEmpty) ...[
                      const SizedBox(height: 6),
                      Text('Hinweis: $note'),
                    ]
                  ],
                ),
              ),
              IconButton(
                tooltip: 'Sprachausgabe',
                icon: const Icon(Icons.volume_up),
                onPressed: () async {
                  final message =
                      '$title. Geschätzter Preis zwischen $minPrice und $maxPrice Euro.';
                  await flutterTts.setLanguage('de-DE');
                  await flutterTts.setSpeechRate(0.5);
                  await flutterTts.speak(message);
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
