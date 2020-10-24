# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets,QtCore,QtGui 


def show_image(image_path='s_pycharm.jpg'):
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtGui.QPixmap(image_path)
    screen = QtWidgets.QLabel()
    screen.setPixmap(pixmap)
    screen.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
	var_exists = screen in locals() or screen in globals()
	if var_exists:
		print('存在')
	else:
		show_image()
    
