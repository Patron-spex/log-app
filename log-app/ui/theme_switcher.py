from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox

class ThemeSwitcherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Theme Switcher")
        self.layout = QVBoxLayout()

        self.label = QLabel("Wählen Sie ein Thema:")
        self.layout.addWidget(self.label)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems(["Modern", "Classic", "Dark"])
        self.layout.addWidget(self.theme_selector)

        self.apply_button = QPushButton("Anwenden")
        self.apply_button.clicked.connect(self.apply_theme)
        self.layout.addWidget(self.apply_button)

        self.setLayout(self.layout)

    def apply_theme(self):
        selected_theme = self.theme_selector.currentText()
        if selected_theme == "Modern":
            self.setStyleSheet("/* Modern theme styles */")
        elif selected_theme == "Classic":
            self.setStyleSheet("/* Classic theme styles */")
        elif selected_theme == "Dark":
            self.setStyleSheet("/* Dark theme styles */")