from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class MapViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.webview = QWebEngineView()
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8"/>
            <title>Karte</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"/>
            <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        </head>
        <body>
            <div id="map" style="width: 100%; height: 100vh;"></div>
            <script>
                var map = L.map('map').setView([52.52, 13.405], 10);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19
                }).addTo(map);
                L.marker([52.52, 13.405]).addTo(map).bindPopup("Fahrzeug 1").openPopup();
            </script>
        </body>
        </html>
        '''
        self.webview.setHtml(html)
        layout.addWidget(self.webview)
        self.setLayout(layout)