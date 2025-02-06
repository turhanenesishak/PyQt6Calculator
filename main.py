import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)
        self.setStyleSheet("background-color: #2c3e50;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #34495e;
                color: white;
                font-size: 24px;
                border: none;
                border-radius: 5px;
                padding: 5px;
                margin: 5px;
            }
        """)
        self.main_layout.addWidget(self.display)

        self.grid_layout = QGridLayout()
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row, row_buttons in enumerate(buttons):
            for col, button_text in enumerate(row_buttons):
                button = QPushButton(button_text)
                button.setFixedSize(60, 60)
                if button_text == '=':
                    button.clicked.connect(self.calculate)
                else:
                    button.clicked.connect(lambda checked, text=button_text: self.display.setText(self.display.text() + text))
                self.grid_layout.addWidget(button, row, col)

        self.clear_button = QPushButton("C")
        self.clear_button.setFixedSize(60, 60)
        self.clear_button.setStyleSheet("background-color: #e74c3c;")
        self.clear_button.clicked.connect(self.clear_display)
        self.grid_layout.addWidget(self.clear_button, 4, 0, 1, 2)

        self.main_layout.addLayout(self.grid_layout)
        
        self.central_widget.setLayout(self.main_layout)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: white;
                font-size: 18px;
                border: none;
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:active {
                background-color: #27ae60;
            }
        """)

    def calculate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error")

    def clear_display(self):
        self.display.setText("")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.calculate()
        elif event.key() == Qt.Key.Key_Backspace:
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif event.key() == Qt.Key.Key_Escape:
            self.close()
        elif event.key() == Qt.Key.Key_C:
            self.clear_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
#A simple, colourful and modern calculator project based on PyQt6.
