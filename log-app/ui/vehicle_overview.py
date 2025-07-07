from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView
from PyQt5.QtCore import QStringListModel

class VehicleOverviewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fahrzeugübersicht")
        self.layout = QVBoxLayout()

        self.label = QLabel("Fahrzeugübersicht")
        self.layout.addWidget(self.label)

        self.vehicle_list_view = QListView()
        self.vehicle_model = QStringListModel(["Fahrzeug 1", "Fahrzeug 2", "Fahrzeug 3"])
        self.vehicle_list_view.setModel(self.vehicle_model)
        self.layout.addWidget(self.vehicle_list_view)

        self.setLayout(self.layout)