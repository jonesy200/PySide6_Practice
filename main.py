from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox

                               )
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000, 800)

        button = QPushButton("Show Choices")
        button.clicked.connect(self.ask_choices)

        self.setCentralWidget(button)


    def ask_choices(self):
        msg = QMessageBox(self)

        msg.setWindowTitle("Choice")
        msg.setText("Please choose an option:")

        msg.addButton("Option 1", QMessageBox.AcceptRole)
        msg.addButton("Option 2", QMessageBox.AcceptRole)
        msg.addButton("Option 3", QMessageBox.AcceptRole)

        msg.exec()

        if msg.clickedButton().text() == "Option 1":
            print("You chose Option 1")
        elif msg.clickedButton().text() == "Option 2":
            print("You chose Option 2")
        elif msg.clickedButton().text() == "Option 3":
            print("You chose Option 3")


app = QApplication()

window = MainWindow()
window.show()

app.exec()






































# label2 = QLabel("This is a PySide6 application.")
#         label2.setAlignment(Qt.AlignCenter)
#
#         label3 = QLabel("Hello")
#         label3.setAlignment(Qt.AlignCenter)
#
#         label4 = QLabel("World")
#         label4.setAlignment(Qt.AlignCenter)
#
#         layout.addWidget(label, 0, 0)
#         layout.addWidget(label2, 0, 1)
#         layout.addWidget(label3, 1, 0)
#         layout.addWidget(label4, 1, 1)
