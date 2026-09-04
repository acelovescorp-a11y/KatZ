# Dashboard

Dieser kleine Guide erklärt, wie das einfache, kostenfreie Dashboard in KatZ funktioniert.

- Frontend: `frontend/lib/screens/dashboard_screen.dart` zeigt Einträge und nutzt TTS.
- Backend: `GET /api/v1/dashboard/` liefert mock-Daten aus `backend/data/dashboard_mock.json`.

So nutzt du es lokal:

1. Backend starten (wie im README beschrieben):

```bash
cd backend
# optional: activate venv
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Frontend starten (Flutter):

```bash
cd frontend
flutter pub get
flutter run -d <device>
```

Das Dashboard ist bewusst offline‑freundlich: bei fehlender Backend‑Verbindung wird eine lokale JSON‑Kopie verwendet.
