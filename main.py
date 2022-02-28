import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Желтые окружности')
        self.show_circle = False
        self.ShowButton.clicked.connect(self.btn_pressed)
        self.csize = 0

    def btn_pressed(self):
        self.csize = random.randint(10, 100)
        self.show_circle = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.show_circle:
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(self.width() // 2 - self.csize, self.height() // 2 - self.csize, 2 * self.csize,
                           2 * self.csize)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # Выглядит лучше, чем стиль по умолчанию
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())
