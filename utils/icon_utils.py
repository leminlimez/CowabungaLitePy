from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

def createRoundedPixmap(pixmap, roundnessPercentage):
    roundedPixmap = QPixmap(pixmap.size())
    roundedPixmap.fill(Qt.transparent)

    painter = QPainter(roundedPixmap)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

    width = pixmap.width()
    height = pixmap.height()
    radius = min(width, height) * roundnessPercentage

    path = QPainterPath()
    path.addRoundedRect(roundedPixmap.rect(), radius, radius)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)

    return roundedPixmap