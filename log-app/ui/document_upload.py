from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class DocumentUploadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dokumente Hochladen")
        self.layout = QVBoxLayout()

        self.label = QLabel("Wählen Sie ein Dokument zum Hochladen:")
        self.layout.addWidget(self.label)

        self.upload_button = QPushButton("Dokument auswählen")
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.upload_button)

        self.setLayout(self.layout)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Dokument auswählen", "", "Alle Dateien (*);;PDF-Dateien (*.pdf);;Textdateien (*.txt)", options=options)
        if file_name:
            self.label.setText(f"Ausgewähltes Dokument: {file_name}")