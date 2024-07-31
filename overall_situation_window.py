import os
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QApplication, QPinchGesture
from PyQt5.QtGui import QPixmap
from analysis import Ui_MainWindow
from function.file_handling import FileHandler


class OverallSituationWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.file_handler = FileHandler(user)
        self.saved_file_path = ""
        self.q_pix = None  # 初始化 q_pix 属性
        self.setupUi(self)
        self.resize(int(self.width() * parent._wr), int(self.height() * parent._hr))
        self.setup_combo_box()
        self.setup_image_tab()

        self.upload_button.clicked.connect(self.upload_file)
        self.analyze_button.clicked.connect(self.analyze_file)
        self.scale_factor = 2  # 初始缩放因子
        self.base_scale_factor = 2  # 基础缩放因子

        # 启用 PinchGesture 识别
        self.grabGesture(Qt.PinchGesture)

    def setup_combo_box(self):
        self.combo_box.addItem("Analyze Amplitude", "amplitude")
        self.combo_box.addItem("Analyze Opening and Closing Prices", "opening_closing")
        self.combo_box.addItem("Analyze Turnover Rate", "turnover")
        self.combo_box.addItem("Analyze Volume of Business", "volume_of_business")
        self.combo_box.addItem("Analyze Max Price", "max_price")
        self.combo_box.addItem("Analyze Min Price", "min_price")
        self.combo_box.addItem("Analyze Composite Rise and Fall", "composite_rise_and_fall")

    def setup_image_tab(self):
        try:
            self.scroll_area = QScrollArea(self)
            self.scroll_area.setWidgetResizable(True)
            self.image_label = QLabel(self)
            self.image_label.setAlignment(Qt.AlignCenter)
            self.scroll_area.setWidget(self.image_label)

            layout = QVBoxLayout(self.result_image)
            layout.addWidget(self.scroll_area)
            self.result_image.setLayout(layout)
        except Exception as e:
            print(f"Error in setup_image_tab: {e}")

    def upload_file(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
            if os.path.isfile(file_path):
                self.saved_file_path = file_path
                self.le_path.setText(file_path)
        except Exception as e:
            print(f"Error in upload_file: {e}")

    def analyze_file(self):
        try:
            if self.saved_file_path:
                analysis_type = self.combo_box.currentData()
                output_image_path = self.file_handler.analyze_file(self.saved_file_path, analysis_type)
                self.display_result_image(output_image_path)
        except Exception as e:
            print(f"Error in analyze_file: {e}")

    def display_result_image(self, image_path):
        try:
            self.q_pix = QPixmap(image_path)
            if self.q_pix.isNull():
                raise ValueError(f"Failed to load image: {image_path}")
            self.adjust_image_to_window()
        except Exception as e:
            print(f"Error in display_result_image: {e}")

    def adjust_image_to_window(self):
        try:
            if self.q_pix:
                window_size = self.scroll_area.size()
                scaled_pixmap = self.q_pix.scaled(window_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(scaled_pixmap)
                self.base_scale_factor = self.image_label.pixmap().width() / self.q_pix.width()  # 基础缩放因子
                self.scale_factor = self.base_scale_factor  # 初始化缩放因子
        except Exception as e:
            print(f"Error in adjust_image_to_window: {e}")

    def update_image(self):
        try:
            if self.q_pix:
                scaled_pixmap = self.q_pix.scaled(self.scale_factor * self.q_pix.size(), Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)
                self.image_label.setPixmap(scaled_pixmap)
        except Exception as e:
            print(f"Error in update_image: {e}")

    def wheelEvent(self, event):
        try:
            if self.q_pix:
                if event.angleDelta().y() > 0:
                    self.scale_factor *= 1.25  # 放大
                else:
                    self.scale_factor *= 0.8  # 缩小
                self.update_image()
        except Exception as e:
            print(f"Error in wheelEvent: {e}")

    # def event(self, event):
    #     if event.type() == QEvent.Wheel:
    #         return self.wheelEvent(event)
    #     return super().event(event)

    # def gestureEvent(self, event):
    #     pinch = event.gesture(Qt.PinchGesture)
    #     if pinch:
    #         self.pinchTriggered(pinch)
    #     return True
    #
    # def pinchTriggered(self, gesture):
    #     if gesture.state() == Qt.GestureStarted:
    #         self.current_scale = self.scale_factor
    #     self.scale_factor = self.current_scale * gesture.scaleFactor()
    #     self.update_image()

    def resizeEvent(self, event):
        try:
            self.adjust_image_to_window()
            super().resizeEvent(event)
        except Exception as e:
            print(f"Error in resizeEvent: {e}")


if __name__ == '__main__':
    import sys

    try:
        app = QApplication(sys.argv)
        window = OverallSituationWindow("User")
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error in main: {e}")