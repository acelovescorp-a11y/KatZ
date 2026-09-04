import 'package:flutter/material.dart';
import 'screens/dashboard_screen.dart';

/// Uncomment the line below to use the recommended Material 3 theme.
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'KatZ - Katalysator-Wert-App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'KatZ'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'KatZ - Vision & Voice Katalysator-Wert-App',
              style: TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 20),
            const Text(
              'Phase 1: Projektstruktur wird aufgebaut',
              style: TextStyle(fontSize: 14),
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {},
              child: const Text('Auto scannen'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {},
              child: const Text('Teilenummer scannen'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {},
              child: const Text('Spracheingabe'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).push(MaterialPageRoute(
                  builder: (_) => const DashboardScreen(),
                ));
              },
              child: const Text('Dashboard'),
            ),
          ],
        ),
      ),
    );
  }
}
