from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class LoginHistoryWindow(QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login History")
        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # 设置文本编辑器为只读
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)

    def load_history(self):
        file = f"logs/{self.user}.txt"
        try:
            with open(file, 'r') as file:
                lines = file.readlines()
                history_text = "\n".join(lines)
                self.text_edit.setText(history_text)
        except FileNotFoundError:
            self.text_edit.setText("No login history found.")

