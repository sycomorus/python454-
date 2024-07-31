import os
import sys



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QDialog
from qt_material import apply_stylesheet

from UserLogin.HistoryWindow import HistoryWindow
from UserLogin.LoginHistoryWindow import LoginHistoryWindow
from UserLogin.LoginWindow import LoginWindow

from overall_situation_window import OverallSituationWindow
from single_stock_situation_window import SingleStockSituationWindow
from qss import qss
from window import Ui_MainWindow

import img_rc


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, wr, hr):
        super().__init__()
        self._wr = wr
        self._hr = hr
        login_directory = f"logs"
        if not os.path.exists(login_directory):
            os.mkdir(login_directory)
        self.user = ""
        self.users = self.load_users()

        self.login_window = LoginWindow(self, self.users)
        if self.login_window.exec_() != QDialog.DialogCode.Accepted:
            self.close()
            sys.exit(0)
        else:
            self.is_logged_in = True
        self.btn_all.clicked.connect(self.show_overall_situation)
        self.btn_single.clicked.connect(self.show_single_stock_situation)
        self.btn_lh.clicked.connect(self.show_login_history)
        self.btn_h.clicked.connect(self.show_history)

    def reset_stylesheet(self):
        for i in [self.btn_all, self.btn_single, self.btn_lh, self.btn_h, ]:
            i.setStyleSheet(qss)
            i.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def load_users(self):
        users = {}
        try:
            with open('users.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    username, password = line.strip().split(':')
                    users[username] = password
        except FileNotFoundError:
            pass
        return users

    def show_history(self):
        self.history_window = HistoryWindow(self, self.user)
        self.history_window.show()

    def update_status(self):
        file = f"logs/{self.user}.txt"
        try:
            with open(file, 'r') as file:
                lines = file.readlines()
                if len(lines) > 1:
                    last_login_time = lines[-2].split(':')
                    self.statusBar.showMessage(
                        f'Last login time: {last_login_time[1]}:{last_login_time[2]}:{last_login_time[3]}')
                else:
                    self.statusBar.showMessage('Last login time: Never')
        except FileNotFoundError:
            self.statusBar.showMessage('Last login time: Never')

    def show_overall_situation(self):
        if self.is_logged_in:
            self.overall_window = OverallSituationWindow(self.user, self)
            self.overall_window.show()

    def show_single_stock_situation(self):
        if self.is_logged_in:
            stock_code, ok = QInputDialog.getText(self, 'Input Stock Code', 'Enter stock code:')
            if ok:
                self.single_stock_window = SingleStockSituationWindow(self.user, self, stock_code)
                self.single_stock_window.show()

    def show_login_history(self):
        self.history_window = LoginHistoryWindow(self.user)
        self.history_window.load_history()
        self.history_window.show()

    def set_user(self, user_name):
        self.user = user_name
        self.update_status()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



if __name__ == '__main__':
    app = QApplication(list())
    apply_stylesheet(app, theme=resource_path('da.xml'))
    screen = app.desktop().screenGeometry()
    w, h = screen.width() / 1920, screen.height() / 1080
    window = MainWindow(w, h)
    window.reset_stylesheet()
    window.show()
    app.exec()
'''
['dark_amber.xml',
     'dark_blue.xml',
     'dark_cyan.xml',
     'dark_lightgreen.xml',
     'dark_pink.xml',
     'dark_purple.xml',
     'dark_red.xml',
     'dark_teal.xml',
     'dark_yellow.xml',
     'light_amber.xml',
     'light_blue.xml',
     'light_cyan.xml',
     'light_cyan_500.xml',
     'light_lightgreen.xml',
     'light_pink.xml',
     'light_purple.xml',
     'light_red.xml',
     'light_teal.xml',
     'light_yellow.xml']
'''
