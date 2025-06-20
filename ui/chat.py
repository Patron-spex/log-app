from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from database import get_connection

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.input = QLineEdit()
        self.send_btn = QPushButton("Senden")
        self.send_btn.clicked.connect(self.send_msg)
        layout.addWidget(self.history)
        layout.addWidget(self.input)
        layout.addWidget(self.send_btn)
        self.setLayout(layout)
        self.load_history()
    
    def load_history(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT sender, message FROM chat ORDER BY id ASC")
        for sender, msg in c.fetchall():
            self.history.append(f"{sender}: {msg}")
        conn.close()
    
    def send_msg(self):
        msg = self.input.text()
        if msg:
            self.history.append(f"Du: {msg}")
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO chat (sender, message, time) VALUES (?, ?, datetime('now'))", ("Du", msg))
            conn.commit()
            conn.close()
            self.input.clear()