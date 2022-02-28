import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Желтые окружности')
        self.show_circle = False
        self.ShowButton.clicked.connect(self.btn_pressed)
        self.csize = 0
        self.ccolor = QColor(0, 0, 0)

    def btn_pressed(self):
        self.ccolor = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.csize = random.randint(10, 100)
        self.show_circle = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        try:
            if self.show_circle:
                qp.setBrush(self.ccolor)
                qp.setPen(self.ccolor)
                qp.drawEllipse(self.width() // 2 - self.csize, self.height() // 2 - self.csize - 40, 2 * self.csize,
                               2 * self.csize)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # Выглядит лучше, чем стиль по умолчанию
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())
