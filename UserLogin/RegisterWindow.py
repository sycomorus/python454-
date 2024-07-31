from PyQt5.QtWidgets import QMessageBox, QDialog

from UserLogin.register import Ui_Dialog


class RegisterWindow(QDialog, Ui_Dialog):
    def __init__(self, users, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.users = users
        self.btn_reg.clicked.connect(self.register_user)
        self.btn_exit.clicked.connect(self.close)
    def register_user(self):
        username = self.le_user.text()
        password = self.le_pwd.text()
        confirm_password = self.le_rpwd.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, 'Login', 'Username and password cannot be empty!')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Register', 'Passwords do not match!')
            return

        if self.check_username_in_file(username):
            QMessageBox.warning(self, 'Login', 'Username has been registered!')
            return

        self.save_user(username, password)
        self.users[username] = password
        QMessageBox.information(self, 'Register', 'Registration successful!')
        self.close()

    @staticmethod
    def save_user(username, password):
        with open('users.txt', 'a') as file:
            file.write(f'{username}:{password}\n')

    def check_username_in_file(self, username, filename='users.txt'):
        # 确保用户名不为空
        if not username:
            return False

        try:
            with open(filename, 'r') as file:
                for line in file:
                    # 去除每行的首尾空白字符，包括 '\n'
                    line = line.strip()
                    # 分割用户名和密码
                    if ':' in line:
                        stored_username, password = line.split(':', 1)
                        # 检查用户名是否匹配
                        if stored_username == username:
                            return True  # 返回True和密码
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return False
