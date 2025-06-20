from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QLineEdit, QMessageBox, QInputDialog
)
from models import get_vehicles, add_vehicle, search_vehicles

class VehicleOverviewWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Fahrzeugübersicht"))

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Suchen...")
        search_button = QPushButton("Suchen")
        search_button.clicked.connect(self.search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        add_btn = QPushButton("Fahrzeug hinzufügen")
        add_btn.clicked.connect(self.add_vehicle)
        layout.addWidget(add_btn)

        self.setLayout(layout)
        self.load_data()

    def load_data(self, vehicles=None):
        if vehicles is None:
            vehicles = get_vehicles()
        self.table.setRowCount(len(vehicles))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Kennzeichen", "Modell", "Fahrer", "Status"])
        for row, v in enumerate(vehicles):
            for col, val in enumerate(v):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()

    def search(self):
        text = self.search_input.text()
        vehicles = search_vehicles(text)
        self.load_data(vehicles)

    def add_vehicle(self):
        license_plate, ok = QInputDialog.getText(self, "Kennzeichen", "Kennzeichen:")
        if not ok or not license_plate:
            return
        model, ok = QInputDialog.getText(self, "Modell", "Modell:")
        if not ok or not model:
            return
        driver, ok = QInputDialog.getText(self, "Fahrer", "Fahrer:")
        if not ok or not driver:
            return
        status, ok = QInputDialog.getText(self, "Status", "Status:")
        if not ok or not status:
            return
        add_vehicle(license_plate, model, driver, status)
        self.load_data()