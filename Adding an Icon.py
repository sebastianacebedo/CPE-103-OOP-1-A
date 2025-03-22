import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "First OOP GUI"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowIcon(QIcon('chatgpt_logo_openai_gpt_ia_line_icon_264985.ico'))  # Make sure 'python.ico' is in the directory
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())