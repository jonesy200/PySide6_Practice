from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QPushButton, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton,
                               QCheckBox, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, QTabWidget, QStackedWidget,
                               )
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(1000, 800)

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label = QLabel("Hello, World!")
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)

        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])

        list_widget.itemClicked.connect(lambda item: print(f"Clicked on {item.text()}"))
        list_widget.itemDoubleClicked.connect(lambda item: print(f"Double clicked on {item.text()}"))

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        radio1 = QRadioButton("Radio 1")
        radio2 = QRadioButton("Radio 2")
        radio3 = QRadioButton("Radio 3")

        for r in (radio1, radio2, radio3):
            r.toggled.connect(self.on_radio_changed)
            r.clicked.connect(self.on_radio_clicked)

        inner_layout.addWidget(radio1)
        inner_layout.addWidget(radio2)
        inner_layout.addWidget(radio3)

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(list_widget)
        layout.addWidget(inner_container)

    def on_button_clicked(self):
        print("Button clicked!")

    def on_radio_changed(self):
        r = self.sender()
        if r.isChecked():
            print(f"{r.text()} is selected.")

        else:
            print(f"Unselected {r.text()}.")

    def on_radio_clicked(self):
        r = self.sender()
        print(f"{r.text()} clicked.")


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
