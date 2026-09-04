import 'dart:convert';
import 'dart:io';

import 'package:path_provider/path_provider.dart';

/// Simple local storage using a JSON file inside application documents directory.
class LocalStorage {
  static final LocalStorage _instance = LocalStorage._internal();

  factory LocalStorage() {
    return _instance;
  }

  LocalStorage._internal();

  Future<File> _getLocalFile() async {
    final dir = await getApplicationDocumentsDirectory();
    final file = File('${dir.path}/katz_dashboard.json');
    if (!await file.exists()) {
      await file.create(recursive: true);
      await file.writeAsString(jsonEncode([]));
    }
    return file;
  }

  Future<List<dynamic>> loadDashboard() async {
    try {
      final file = await _getLocalFile();
      final content = await file.readAsString();
      return jsonDecode(content) as List<dynamic>;
    } catch (e) {
      return <dynamic>[];
    }
  }

  Future<void> saveDashboard(List<dynamic> entries) async {
    final file = await _getLocalFile();
    await file.writeAsString(jsonEncode(entries));
  }
}
