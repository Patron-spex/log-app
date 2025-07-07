import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QAction
from database import init_db
from ui.vehicle_overview import VehicleOverviewWidget
from ui.map_view import MapViewWidget
from ui.chat import ChatWidget
from ui.analytics import AnalyticsWidget
from ui.notifications import show_notification
from ui.document_upload import DocumentUploadWidget
from ui.theme_switcher import ThemeSwitcherWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logistik Dashboard")
        self.resize(1200, 800)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Module
        self.widgets = [
            ("Fahrzeuge", VehicleOverviewWidget()),
            ("Karte", MapViewWidget()),
            ("Chat", ChatWidget()),
            ("Analytics", AnalyticsWidget()),
            ("Dokumente", DocumentUploadWidget()),
            ("Theme", ThemeSwitcherWidget())
        ]
        for _, widget in self.widgets:
            self.stack.addWidget(widget)

        menubar = self.menuBar()
        module_menu = menubar.addMenu("Module")
        for idx, (name, _) in enumerate(self.widgets):
            action = QAction(name, self)
            action.triggered.connect(lambda i=idx: self.stack.setCurrentIndex(i))
            module_menu.addAction(action)

        show_notification(self, "Willkommen!", "Dashboard erfolgreich gestartet!")

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    # Modernes Stylesheet laden
    with open("modern_theme.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())