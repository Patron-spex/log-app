from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication

class ThemeSwitcherWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.dark_btn = QPushButton("Dark Mode (nur mit eigenem Sheet anpassbar)")
        self.light_btn = QPushButton("Light Mode")
        self.dark_btn.clicked.connect(self.set_dark)
        self.light_btn.clicked.connect(self.set_light)
        layout.addWidget(self.dark_btn)
        layout.addWidget(self.light_btn)
        self.setLayout(layout)

    def set_dark(self):
        # Beispiel: Farben im Stylesheet anpassen (hier müsstest du ggf. ein separates dark_theme.qss laden)
        with open("modern_theme.qss") as f:
            dark = f.read().replace("#f5f6fa", "#222426").replace("#232426", "#f5f6fa")
        QApplication.instance().setStyleSheet(dark)

    def set_light(self):
        with open("modern_theme.qss") as f:
            QApplication.instance().setStyleSheet(f.read())