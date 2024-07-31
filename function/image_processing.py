from PyQt5 import QtGui
from PIL import Image

class ImageProcessor:
    def __init__(self, image_label):
        self.image_label = image_label

    def load_and_display_image(self, path):
        pixmap = self.load_image(path)
        self.image_label.setPixmap(pixmap)

    def load_image(self, path, target_width=800, target_height=600):
        image = Image.open(path)
        image.thumbnail((target_width, target_height), Image.LANCZOS)
        image.save("resized_image.png")  # 保存调整大小后的图像
        pixmap = QtGui.QPixmap("resized_image.png")
        return pixmap
