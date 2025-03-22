import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Registration")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("../sign-form.ico"))
        self.center()
        self.initUI()

    def initUI(self):
        labels = ["First Name:", "Last Name:", "Username:", "Password:", "Email Address:", "Contact Number:"]
        self.textboxes = []
        y_offset = 20

        for label in labels:
            lbl = QLabel(label, self)
            lbl.move(20, y_offset)

            txt = QLineEdit(self)
            txt.move(150, y_offset)

            if "Password" in label:
                txt.setEchoMode(QLineEdit.Password)

            self.textboxes.append(txt)
            y_offset += 40

        # Submit and Clear Buttons
        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.move(100, y_offset)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.move(200, y_offset)

        self.clear_btn.clicked.connect(self.clearFields)

    def clearFields(self):
        for txt in self.textboxes:
            txt.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())