from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel


from PySide6.QtCore import Qt

class SecondaryWindow(QMainWindow):
    def __init__(self,n):
        super().__init__()

        self.setWindowTitle(f"Window {n}")

        label = QLabel(f"This is window {n}.")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(400, 300)

        button = QPushButton("Open Window")
        button.clicked.connect(self.open_window)

        self.setCentralWidget(button)

        self.count = 1
        self.windows = []

    def open_window(self):
        w = SecondaryWindow(self.count)

        self.count += 1
        self.windows.append(w)

        w.show()

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
