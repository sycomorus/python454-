import os

from PyQt5.QtWidgets import QListWidgetItem, QLabel, QMainWindow, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from UserLogin.history import Ui_MainWindow


class HistoryWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user
        self.setupUi(self)
        self.resize(1600, 900)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(0, 12)
        self.verticalLayout.setStretch(1, 1)
        self.setup_more()
        self.history_items = []
        self.load = False
        self.history_list_widget.itemClicked.connect(self.show_image)
        self.load_button.clicked.connect(self.load_history)

    def setup_more(self):
        self.image_label = QLabel()
        self.image_label.setFixedSize(1200, 800)  # 设置图像显示标签的固定大小
        self.image_label.setScaledContents(True)  # 启用图像内容缩放
        self.scroll_area.setWidget(self.image_label)

    # def init_ui(self):
        # self.setWindowTitle("History")
        # self.setGeometry(100, 100, 1200, 1000)  # 假设宽度为600，高度为400
        #
        # self.layout = QVBoxLayout()
        #
        # self.history_list_widget = QListWidget()
        # self.history_list_widget.itemClicked.connect(self.show_image)
        # self.layout.addWidget(self.history_list_widget)
        #
        # self.image_label = QLabel()
        # self.image_label.setAlignment(Qt.AlignCenter)
        # self.layout.addWidget(self.image_label)

        # self.load_button = QPushButton("Load History")
        # self.load_button.clicked.connect(self.load_history)
        # self.layout.addWidget(self.load_button)

        # self.scroll_area = QScrollArea()
        # self.image_label = QLabel()
        # self.image_label.setFixedSize(1200, 800)  # 设置图像显示标签的固定大小
        # self.image_label.setScaledContents(True)  # 启用图像内容缩放
        # self.scroll_area.setWidget(self.image_label)
        # self.layout.addWidget(self.scroll_area)

        # self.exit_button = QPushButton('Exit')
        # self.exit_button.clicked.connect(self.close)
        # self.layout.addWidget(self.exit_button)
        #
        # self.setLayout(self.layout)

    def load_history(self):
        base_path = f"analysis/{self.user}"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        for filename in os.listdir(base_path):
            if filename.endswith(".png"):  # 假设历史图片是PNG格式
                file_path = os.path.join(base_path, filename)
                if filename not in self.history_items:
                    item = QListWidgetItem(os.path.basename(filename))
                    item.setData(Qt.UserRole, file_path)  # 存储文件路径
                    self.history_list_widget.addItem(item)
                    self.history_items.append(filename)

        if not self.history_items and self.load == False:
            self.history_list_widget.addItem("No history found.")
            self.load = True

    def show_image(self, item):
        if item and item.data(Qt.UserRole):
            image_path = item.data(Qt.UserRole)
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

            # 调整滚动区域的大小策略
            self.image_label.resize(pixmap.size())
            self.scroll_area.setWidgetResizable(True)

            self.image_label.show()