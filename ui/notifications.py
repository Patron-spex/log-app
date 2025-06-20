from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtGui import QIcon

def show_notification(app, title, message):
    tray = QSystemTrayIcon(QIcon())
    tray.show()
    tray.showMessage(title, message, QSystemTrayIcon.Information, 5000)