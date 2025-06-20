from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class DocumentUploadWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.upload_btn = QPushButton("Dokument hochladen")
        self.upload_btn.clicked.connect(self.upload_file)
        self.info = QLabel("Kein Dokument ausgewählt.")
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.info)
        self.setLayout(layout)
    
    def upload_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Dokument auswählen")
        if fname:
            self.info.setText(f"Hochgeladen: {fname}")