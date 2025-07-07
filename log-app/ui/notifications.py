def show_notification(parent, title, message):
    from PyQt5.QtWidgets import QMessageBox
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()