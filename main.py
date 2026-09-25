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

        line_edit = QLineEdit()
        text_edit = QTextEdit()

        combobox = QComboBox()
        combobox.addItems(["Option 1", "Option 2", "Option 3"])

        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        checkbox1 = QCheckBox("Check me")
        checkbox2 = QCheckBox("Or me")
        checkbox3 = QCheckBox("Or me too")

        radio1 = QRadioButton("Radio 1")
        radio2 = QRadioButton("Radio 2")
        radio3 = QRadioButton("Radio 3")

        inner_layout.addWidget(checkbox1)
        inner_layout.addWidget(checkbox2)
        inner_layout.addWidget(checkbox3)

        inner_layout.addWidget(radio1)
        inner_layout.addWidget(radio2)
        inner_layout.addWidget(radio3)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combobox)
        layout.addWidget(list_widget)
        layout.addWidget(inner_container)
        layout.addWidget(slider)

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
