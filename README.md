# KatZ — CatValue Live (Vision & Voice Katalysator-Wert-App)

Eine mobile Anwendung (iOS & Android) zur Echtzeit-Ermittlung und akustischen Ausgabe von Katalysator-Schrottwerten. Die App nutzt Computer Vision (Fahrzeug- & OCR-Erkennung), Sprachsteuerung und Live-Web-Scraping.

## 🎯 Zielstellung

Lösung des Problems, dass Katalysator-Schrottwerte stark schwanken, schwer Fahrzeugmodellen zuzuordnen sind und der Wert stark von der Einbauposition (Unterboden vs. Krümmer) abhängt.

**Fokus:** Ausschließlich Unterboden-Katalysatoren ab einem Ankaufswert von 250 €.

## 🔧 Technologiestack

| Komponente | Technologie | Zweck |
|---|---|---|
| Frontend (Mobile) | Flutter (Dart) | Cross-Platform App (iOS & Android) |
| Kamera & OCR | Google ML Kit Text Recognition | Lokale Echtzeitkamera-Texterkennung |
| Sprachausgabe | flutter_tts | Native TTS (AVSpeechSynthesizer / Android TextToSpeech) |
| Backend | Python 3.11+ (FastAPI) | Hochperformante asynchrone REST-API |
| Vision AI | OpenAI GPT-4o Vision / Mini | Fahrzeugmodell-Erkennung & Daten-Strukturierung |
| Web-Scraping | Playwright / Crawl4AI | Asynchrones Headless-Browsing für Live-Daten |
| Cache & DB | Redis + Supabase/PostgreSQL | Zwischenspeicherung & Persistierung |
| Metalle-API | GoldAPI / Metals-API | Tagesaktueller Rohstoffkurs-Abruf |

## 📂 Projektstruktur

```
KatZ/
├── backend/                 # Python FastAPI Backend
│   ├── app/
│   │   ├── main.py         # Applikationseinstieg
│   │   ├── config.py       # Konfiguration & Umgebungsvariablen
│   │   ├── api/
│   │   │   └── v1/         # API Versioning (v1)
│   │   │       ├── scan.py         # Scan-Endpunkte
│   │   │       ├── voice.py        # Voice-Query-Endpunkte
│   │   │       └── router.py       # Route-Registrierung
│   │   ├── services/
│   │   │   ├── vision.py   # GPT-4o Vision Integration
│   │   │   ├── scraper.py  # Web-Scraper Cluster
│   │   │   ├── cache.py    # Redis Cache-Logik
│   │   │   ├── metals_api.py # Edelmetallkurs-Abruf
│   │   │   └── nlg.py      # Natural Language Generation
│   │   ├── models/
│   │   │   ├── vehicle.py  # Fahrzeug-Datenmodelle
│   │   │   ├── catalyst.py # Katalysator-Datenmodelle
│   │   │   └── price.py    # Preis-Datenmodelle
│   │   ├── filters/
│   │   │   └── business_rules.py # Strikte Filter-Engine
│   │   └── utils/
│   │       ├── logging.py
│   │       └── helpers.py
│   ├── requirements.txt     # Python Dependencies
│   ├── .env.example         # Env-Variablen Template
│   └── Dockerfile          # Backend Containerisierung
│
├── frontend/                # Flutter Mobile App
│   ├── lib/
│   │   ├── main.dart       # Applikationseinstieg
│   │   ├── config/         # App-Konfiguration
│   │   ├── screens/
│   │   │   ├── camera_screen.dart      # Kamera-Sucher
│   │   │   ├── dashboard_screen.dart   # Ergebnis-Dashboard
│   │   │   └── voice_screen.dart       # Spracheingabe
│   │   ├── services/
│   │   │   ├── api_service.dart   # Backend-API Client
│   │   │   ├── camera_service.dart # Kamera-Integration
│   │   │   ├── ocr_service.dart    # Google ML Kit OCR
│   │   │   ├── voice_service.dart  # Spracheingabe/Ausgabe
│   │   │   └── tts_service.dart    # Text-To-Speech
│   │   ├── models/
│   │   │   ├── scan_response.dart
│   │   │   └── vehicle_data.dart
│   │   ├── providers/       # State Management
│   │   └── widgets/         # Custom Widgets
│   ├── pubspec.yaml        # Flutter Dependencies
│   ├── analysis_options.yaml
│   └── Dockerfile          # Frontend Containerisierung (optional)
│
├── docs/
│   ├── ARCHITECTURE.md      # System-Architektur Deep-Dive
│   ├── API_SPECIFICATION.md # REST API Spezifikation
│   ├── DATABASE_SCHEMA.md   # PostgreSQL/Supabase Schema
│   ├── ROADMAP.md          # Detaillierter Phasenplan
│   └── SETUP.md            # Installations- & Konfigurationsanleitung
│
├── scripts/
│   ├── setup.sh            # Vollautomatisches Setup
│   ├── db_migrate.py       # Datenbankmigrationen
│   └── seed_data.py        # Testdaten initialisieren
│
├── docker-compose.yml      # Lokale Entwicklungs-Umgebung
├── .github/
│   └── workflows/          # CI/CD Pipelines (optional)
│
└── .gitignore
```

## 🚀 Quick Start

### Voraussetzungen

- Python 3.11+
- Flutter SDK (latest)
- PostgreSQL 14+ oder Supabase
- Redis 6+
- Docker & Docker Compose (optional)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Konfiguration
cp .env.example .env
# .env Datei mit API-Keys füllen (OpenAI, Metals-API, etc.)

# Datenbank-Setup
python scripts/db_migrate.py

# Server starten
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
flutter pub get

# iOS
flutter run -d ios

# Android
flutter run -d android
```

### Mit Docker Compose (vollständige Umgebung)

```bash
docker-compose up -d

# Backend läuft auf: http://localhost:8000
# PostgreSQL: localhost:5432
# Redis: localhost:6379
```

## 📋 Phasenplan (6 Wochen)

| Phase | Fokus | Dauer |
|-------|-------|-------|
| **Phase 1** | Architektur, Datenbankschema & Schnittstellen | Woche 1-2 |
| **Phase 2** | Live-Scraper Pipeline & Finanz-APIs | Woche 3-4 |
| **Phase 3** | KI-Vision, Engine-Logik & Strikte Filter | Woche 5-6 |
| **Phase 4** | Mobile App UI, Kamera-Integration & On-Device OCR | Woche 7-8 |
| **Phase 5** | Voice Engine & System-Integration | Woche 9 |
| **Phase 6** | Field-Testing, Performance & Deployment | Woche 10-11 |

Detailinformationen: siehe [`docs/ROADMAP.md`](docs/ROADMAP.md)

## 🔐 Umgebungsvariablen

Erforderliche API-Keys und Konfigurationen:

```
# OpenAI Vision
OPENAI_API_KEY=sk-...

# Metals-API
METALS_API_KEY=...

# Datenbank
DATABASE_URL=postgresql://user:password@localhost:5432/katz_db
REDIS_URL=redis://localhost:6379

# Supabase (optional)
SUPABASE_URL=...
SUPABASE_KEY=...
```

## 📖 Dokumentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — System-Architektur & Datenfluss
- [`docs/API_SPECIFICATION.md`](docs/API_SPECIFICATION.md) — REST API Dokumentation
- [`docs/DATABASE_SCHEMA.md`](docs/DATABASE_SCHEMA.md) — Datenbankschema
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — Detaillierter Phasenplan mit Milestones
- [`docs/SETUP.md`](docs/SETUP.md) — Konfiguration & Troubleshooting

## 🎯 Geschäftsregeln (Strikte Filter)

1. **Einbauort-Filter:** Nur Unterboden-Katalysatoren. Krümmer & Motorraum werden ausgeschlossen.
2. **Preisschwellenwert:** Nur Katalysatoren ab 250,00 € Ankaufswert.
3. **Varianten-Aggregation:** Ermittlung von Gesamtzahl, Min- und Max-Preis für mehrere Varianten.

## 📞 Support & Kontakt

Bei Fragen zur Architektur oder zum Entwicklungsstand: Siehe Issues oder Diskussionen im Repository.

---

**Status:** 🚧 In Entwicklung — Phase 1 (Architektur & Setup)
