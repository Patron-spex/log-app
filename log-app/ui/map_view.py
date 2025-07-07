from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class MapViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Kartenansicht wird hier angezeigt.")
        layout.addWidget(label)
        self.setLayout(layout)