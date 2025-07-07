# Logistik Dashboard

## Projektübersicht
Das Logistik Dashboard ist eine Anwendung zur Verwaltung und Analyse von Logistikdaten. Es bietet verschiedene Module, darunter Fahrzeugübersicht, Kartenansicht, Chat, Analysen, Dokumenten-Upload und ein Theme-Wechsler.

## Dateien
- **main.py**: Einstiegspunkt der Anwendung, der das Hauptfenster und die Module konfiguriert.
- **database.py**: Funktionen zur Initialisierung und Verwaltung der Datenbank.
- **modern_theme.qss**: Stylesheet für das Design der Benutzeroberfläche.
- **requirements.txt**: Liste der benötigten Python-Pakete.
- **ui/**: Verzeichnis mit verschiedenen Widgets für die Benutzeroberfläche.
  - **vehicle_overview.py**: Fahrzeugübersicht.
  - **map_view.py**: Kartenansicht.
  - **chat.py**: Chat-Oberfläche.
  - **analytics.py**: Analysen und Statistiken.
  - **notifications.py**: Funktion zur Anzeige von Benachrichtigungen.
  - **document_upload.py**: Widget zum Hochladen von Dokumenten.
  - **theme_switcher.py**: Widget zum Wechseln zwischen verschiedenen Themen.

## Installation
1. Klonen Sie das Repository:
   ```
   git clone <repository-url>
   ```
2. Wechseln Sie in das Projektverzeichnis:
   ```
   cd log-app
   ```
3. Installieren Sie die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```

## Verwendung
Um die Anwendung zu starten, führen Sie den folgenden Befehl aus:
```
python main.py
```

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.