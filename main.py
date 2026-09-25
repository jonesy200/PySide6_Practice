from PySide6.QtWidgets import (QApplication, QMainWindow

                               )
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000, 800)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")

        aboutAction = help_menu.addAction("About")
        aboutAction.triggered.connect(lambda: print("Tutorial help menu item clicked"))



        submenu = file_menu.addMenu("Submenu")
        exitAction = submenu.addAction("Exit")

        exitAction.triggered.connect(self.close)






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
