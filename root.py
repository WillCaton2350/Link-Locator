from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton
from PyQt6.QtWidgets import QApplication, QLineEdit
import sys
import os

class url_enum(QMainWindow):
    def __init__(self):
        super(url_enum,self).__init__()
        self.setGeometry(500,100,500,500)
        self.setStyleSheet("background-color:#141414;")
        self.setFixedSize(500,500)
# QLabel Main
        self.label = QLabel(self)
        self.label.move(200, 10)
        self.label.setStyleSheet("background-color:#141414;")
        self.label.setStyleSheet("font-size:20px;")
        self.label.setText("URL ENUM")

# QLabels
        self.label1 = QLabel(self)
        self.label1.move(214,100)
        self.label1.setStyleSheet("background-color:#141414;")
        self.label1.setStyleSheet("font-size:12px;")
        self.label1.setText("Enter URL 1:")

        self.label2 = QLabel(self)
        self.label2.move(214,200)
        self.label2.setStyleSheet("background-color:#141414;")
        self.label2.setStyleSheet("font-size:12px;")
        self.label2.setText("Enter URL 2:")

        self.label3 = QLabel(self)
        self.label3.move(214,300)
        self.label3.setStyleSheet("background-color:#141414;")
        self.label3.setStyleSheet("font-size:12px;")
        self.label3.setText("Enter URL 3:")

# QPushbutton
        self.button = QPushButton(self)
        self.button.move(10,100)
        self.button.setStyleSheet("background-color:grey;")
        self.button.setText("Btn 1")

        self.button.clicked.connect(self.func)
        self.button = QPushButton(self)
        self.button.move(10,200)
        self.button.setStyleSheet("background-color:grey;")
        self.button.setText("Btn 2")

        self.button.clicked.connect(self.func1)
        self.button = QPushButton(self)
        self.button.move(10,300)
        self.button.setStyleSheet("background-color:grey;")
        self.button.setText("Btn 3")
        self.button.clicked.connect(self.func2)

# QLineEdit
        self.input = QLineEdit(self)
        self.input.move(390, 100)
        self.input.setStyleSheet("background-color:#fff;")

        self.input_2 = QLineEdit(self)
        self.input_2.move(390, 200)
        self.input_2.setStyleSheet("background-color:#fff;")
    
        self.input_3 = QLineEdit(self)
        self.input_3.move(390, 300)
        self.input_3.setStyleSheet("background-color:#fff;")

# OS functions
    def func(self):
        os.system("python3 main1.py")
    def func1(self):
        os.system("python3 main2.py")
    def func2(self):
        os.system("python3 main3.py")

if __name__ == "__main__":
    def main():
        run_app = QApplication(sys.argv)
        win = url_enum()
        win.show()
        sys.exit(run_app.exec())
    main()

# NOTES
    # FIX UX ISSUE. BUT THE BUTTONS ON THE FAR LEFT AND QLINEEDITS IN THE MIDDLE
    # READ -> TYPE -> CLICK 