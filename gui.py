# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 951)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QChartView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 680, 1201, 171))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 528, 535))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 10, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 12, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setText("")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 11, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_left = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_left.setMinimumSize(QtCore.QSize(100, 100))
        self.button_left.setMaximumSize(QtCore.QSize(130, 16777215))
        self.button_left.setText("")
        self.button_left.setObjectName("button_left")
        self.horizontalLayout_2.addWidget(self.button_left)
        self.add_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.add_Button.setMinimumSize(QtCore.QSize(100, 100))
        self.add_Button.setMaximumSize(QtCore.QSize(100, 100))
        self.add_Button.setObjectName("add_Button")
        self.horizontalLayout_2.addWidget(self.add_Button)
        self.del_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.del_Button.setMinimumSize(QtCore.QSize(100, 100))
        self.del_Button.setMaximumSize(QtCore.QSize(100, 100))
        self.del_Button.setObjectName("del_Button")
        self.horizontalLayout_2.addWidget(self.del_Button)
        self.change_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.change_Button.setMinimumSize(QtCore.QSize(100, 100))
        self.change_Button.setMaximumSize(QtCore.QSize(100, 100))
        self.change_Button.setObjectName("change_Button")
        self.horizontalLayout_2.addWidget(self.change_Button)
        self.button_right = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_right.setMinimumSize(QtCore.QSize(100, 100))
        self.button_right.setMaximumSize(QtCore.QSize(100, 100))
        self.button_right.setText("")
        self.button_right.setObjectName("button_right")
        self.horizontalLayout_2.addWidget(self.button_right)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 15, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 9, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.foto4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.foto4.setMinimumSize(QtCore.QSize(100, 100))
        self.foto4.setMaximumSize(QtCore.QSize(100, 100))
        self.foto4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foto4.setText("")
        self.foto4.setPixmap(QtGui.QPixmap("resources/no-photo-60.png"))
        self.foto4.setScaledContents(True)
        self.foto4.setObjectName("foto4")
        self.horizontalLayout.addWidget(self.foto4)
        self.foto3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.foto3.setMinimumSize(QtCore.QSize(100, 100))
        self.foto3.setMaximumSize(QtCore.QSize(100, 100))
        self.foto3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foto3.setText("")
        self.foto3.setPixmap(QtGui.QPixmap("resources/no-photo-60.png"))
        self.foto3.setScaledContents(True)
        self.foto3.setObjectName("foto3")
        self.horizontalLayout.addWidget(self.foto3)
        self.foto2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.foto2.setMinimumSize(QtCore.QSize(100, 100))
        self.foto2.setMaximumSize(QtCore.QSize(100, 100))
        self.foto2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foto2.setText("")
        self.foto2.setPixmap(QtGui.QPixmap("resources/no-photo-60.png"))
        self.foto2.setScaledContents(True)
        self.foto2.setObjectName("foto2")
        self.horizontalLayout.addWidget(self.foto2)
        self.foto1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.foto1.setMinimumSize(QtCore.QSize(100, 100))
        self.foto1.setMaximumSize(QtCore.QSize(100, 100))
        self.foto1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.foto1.setText("")
        self.foto1.setPixmap(QtGui.QPixmap("resources/no-photo-60.png"))
        self.foto1.setScaledContents(True)
        self.foto1.setObjectName("foto1")
        self.horizontalLayout.addWidget(self.foto1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout, 14, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 13, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 201, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Овощи отсутствуют"))
        self.label_16.setText(_translate("MainWindow", "Коментарий:"))
        self.add_Button.setText(_translate("MainWindow", "Добавить\n"
"растение"))
        self.del_Button.setText(_translate("MainWindow", "Удалить\n"
"растение"))
        self.change_Button.setText(_translate("MainWindow", "Изменить\n"
"растение"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить\n"
"фото"))
        self.label_12.setText(_translate("MainWindow", "Статус: "))
        self.label_14.setText(_translate("MainWindow", "Высажено"))
        self.pushButton_5.setText(_translate("MainWindow", "Посадить\n"
"семена"))
        self.pushButton.setText(_translate("MainWindow", "Очистить базу"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "О программе"))
from PyQt5.QtChart import QChartView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())