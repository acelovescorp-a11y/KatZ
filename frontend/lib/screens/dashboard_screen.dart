import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/local_storage.dart';
import '../widgets/dashboard_card.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  bool _loading = true;
  List<Map<String, dynamic>> _entries = [];

  @override
  void initState() {
    super.initState();
    APIService().initialize();
    _loadEntries();
  }

  Future<void> _loadEntries() async {
    setState(() => _loading = true);
    try {
      final data = await APIService().fetchDashboard();
      setState(() {
        _entries = data;
        _loading = false;
      });
      // Save a local copy for offline use
      await LocalStorage().saveDashboard(_entries);
    } catch (e) {
      // Fallback to local storage
      final local = await LocalStorage().loadDashboard();
      setState(() {
        _entries = local.map((e) => Map<String, dynamic>.from(e as Map)).toList();
        _loading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard'),
      ),
      body: RefreshIndicator(
        onRefresh: _loadEntries,
        child: _loading
            ? const Center(child: CircularProgressIndicator())
            : _entries.isEmpty
                ? ListView(
                    physics: const AlwaysScrollableScrollPhysics(),
                    children: const [
                      SizedBox(height: 120),
                      Center(child: Text('Keine Einträge gefunden')),
                    ],
                  )
                : ListView.builder(
                    itemCount: _entries.length,
                    itemBuilder: (context, index) {
                      final entry = _entries[index];
                      return DashboardCard(entry: entry);
                    },
                  ),
      ),
    );
  }
}
