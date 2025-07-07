from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class AnalyticsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel("Analytics Overview")
        layout.addWidget(title)
        self.setLayout(layout)