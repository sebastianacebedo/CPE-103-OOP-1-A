import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Line Edit"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('chatgpt_logo_openai_gpt_ia_line_icon_264985.ico'))

        self.textboxlbl = QLabel("Hello World!", self)
        self.textboxlbl.move(30, 25)  # Position of the label

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())