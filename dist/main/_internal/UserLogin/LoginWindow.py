from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QDialog, QLabel

from UserLogin.RegisterWindow import RegisterWindow

from UserLogin.login import Ui_Dialog



class LoginWindow(QDialog, Ui_Dialog):
    def __init__(self, main_window, users):
        super().__init__(main_window)
        self.setupUi(self)
        self.main_window = main_window
        self.resize(int(self.width() * self.main_window._wr), int(self.height() * self.main_window._hr))

        self.users = users
        self.btn_login.clicked.connect(self.check_credentials)
        self.btn_exit.clicked.connect(self.handle_exit)
        self.btn_reg.clicked.connect(self.show_register_window)
    def handle_exit(self):
        self.reject()
    def check_credentials(self):
        username = self.le_user.text()
        password = self.le_pwd.text()

        if not username or not password:
            QMessageBox.warning(self, 'Login', 'Username and password cannot be empty!')
            return  # 退出函数

        # 这里可以添加验证用户名和密码的逻辑
        if username in self.users and self.users[username] == password:
            # QMessageBox.information(self, 'Login', 'Login successful!')
            self.record_login_time(username)
            self.main_window.setupUi(self.main_window)
            self.main_window.resize(int(self.main_window.width() * self.main_window._wr), int(self.main_window.height() * self.main_window._hr))
            self.main_window.set_user(username)
            self.accept()
        else:
            QMessageBox.warning(self, 'Login', 'Invalid username or password!')

    def show_register_window(self):
        self.register_window = RegisterWindow(self.users, self)
        self.register_window.exec_()

    def record_login_time(self, username):
        current_time = datetime.now()
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file = f"logs/{username}.txt"
        with open(file, 'a') as file:
            file.write(f'{username}:{current_time}\n')
