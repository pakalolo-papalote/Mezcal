# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mezcal-widget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MezcalPicker(object):
    def setupUi(self, MezcalPicker):
        MezcalPicker.setObjectName("MezcalPicker")
        MezcalPicker.resize(438, 591)
        MezcalPicker.setAutoFillBackground(False)
        MezcalPicker.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridLayout_2 = QtWidgets.QGridLayout(MezcalPicker)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tetrad4 = QtWidgets.QFrame(MezcalPicker)
        self.tetrad4.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.tetrad4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tetrad4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tetrad4.setObjectName("tetrad4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tetrad4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.push_tetrad4 = QtWidgets.QPushButton(self.tetrad4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tetrad4.sizePolicy().hasHeightForWidth())
        self.push_tetrad4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_tetrad4.setFont(font)
        self.push_tetrad4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_tetrad4.setAutoFillBackground(False)
        self.push_tetrad4.setDefault(False)
        self.push_tetrad4.setFlat(True)
        self.push_tetrad4.setObjectName("push_tetrad4")
        self.gridLayout_6.addWidget(self.push_tetrad4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.tetrad4)
        self.monochrome1 = QtWidgets.QFrame(MezcalPicker)
        self.monochrome1.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.monochrome1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monochrome1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.monochrome1.setObjectName("monochrome1")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.monochrome1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.push_monochrome1 = QtWidgets.QPushButton(self.monochrome1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_monochrome1.sizePolicy().hasHeightForWidth())
        self.push_monochrome1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_monochrome1.setFont(font)
        self.push_monochrome1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_monochrome1.setAutoFillBackground(False)
        self.push_monochrome1.setDefault(False)
        self.push_monochrome1.setFlat(True)
        self.push_monochrome1.setObjectName("push_monochrome1")
        self.gridLayout_10.addWidget(self.push_monochrome1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.monochrome1)
        self.monochrome2 = QtWidgets.QFrame(MezcalPicker)
        self.monochrome2.setStyleSheet("background-color: rgb(0, 59, 119);\n"
"")
        self.monochrome2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monochrome2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.monochrome2.setObjectName("monochrome2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.monochrome2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.push_monochrome2 = QtWidgets.QPushButton(self.monochrome2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_monochrome2.sizePolicy().hasHeightForWidth())
        self.push_monochrome2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_monochrome2.setFont(font)
        self.push_monochrome2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_monochrome2.setAutoFillBackground(False)
        self.push_monochrome2.setDefault(False)
        self.push_monochrome2.setFlat(True)
        self.push_monochrome2.setObjectName("push_monochrome2")
        self.gridLayout_12.addWidget(self.push_monochrome2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.monochrome2)
        self.monochrome3 = QtWidgets.QFrame(MezcalPicker)
        self.monochrome3.setStyleSheet("background-color: rgb(0, 17, 34);")
        self.monochrome3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monochrome3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.monochrome3.setObjectName("monochrome3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.monochrome3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.push_monochrome3 = QtWidgets.QPushButton(self.monochrome3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_monochrome3.sizePolicy().hasHeightForWidth())
        self.push_monochrome3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_monochrome3.setFont(font)
        self.push_monochrome3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_monochrome3.setAutoFillBackground(False)
        self.push_monochrome3.setDefault(False)
        self.push_monochrome3.setFlat(True)
        self.push_monochrome3.setObjectName("push_monochrome3")
        self.gridLayout_11.addWidget(self.push_monochrome3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.monochrome3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tetrad3 = QtWidgets.QFrame(MezcalPicker)
        self.tetrad3.setStyleSheet("background-color: rgb(204, 102, 0);")
        self.tetrad3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tetrad3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tetrad3.setObjectName("tetrad3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tetrad3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.push_tetrad3 = QtWidgets.QPushButton(self.tetrad3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tetrad3.sizePolicy().hasHeightForWidth())
        self.push_tetrad3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_tetrad3.setFont(font)
        self.push_tetrad3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_tetrad3.setAutoFillBackground(False)
        self.push_tetrad3.setDefault(False)
        self.push_tetrad3.setFlat(True)
        self.push_tetrad3.setObjectName("push_tetrad3")
        self.gridLayout_5.addWidget(self.push_tetrad3, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.tetrad3)
        self.tetrad2 = QtWidgets.QFrame(MezcalPicker)
        self.tetrad2.setStyleSheet("background-color: rgb(204, 0, 204);")
        self.tetrad2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tetrad2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tetrad2.setObjectName("tetrad2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tetrad2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.push_tetrad2 = QtWidgets.QPushButton(self.tetrad2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tetrad2.sizePolicy().hasHeightForWidth())
        self.push_tetrad2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_tetrad2.setFont(font)
        self.push_tetrad2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_tetrad2.setAutoFillBackground(False)
        self.push_tetrad2.setDefault(False)
        self.push_tetrad2.setFlat(True)
        self.push_tetrad2.setObjectName("push_tetrad2")
        self.gridLayout_4.addWidget(self.push_tetrad2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.tetrad2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.rum_color = QtWidgets.QFrame(MezcalPicker)
        self.rum_color.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y0:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.rum_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rum_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rum_color.setObjectName("rum_color")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.rum_color)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.push_rum_color = QtWidgets.QPushButton(self.rum_color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_rum_color.sizePolicy().hasHeightForWidth())
        self.push_rum_color.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(88)
        self.push_rum_color.setFont(font)
        self.push_rum_color.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.push_rum_color.setAutoFillBackground(False)
        self.push_rum_color.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.push_rum_color.setCheckable(False)
        self.push_rum_color.setDefault(True)
        self.push_rum_color.setFlat(False)
        self.push_rum_color.setObjectName("push_rum_color")
        self.gridLayout_13.addWidget(self.push_rum_color, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.rum_color)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tetrad1 = QtWidgets.QFrame(MezcalPicker)
        self.tetrad1.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.tetrad1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tetrad1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tetrad1.setProperty("tetrad_bg", QtGui.QColor(0, 0, 255))
        self.tetrad1.setObjectName("tetrad1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tetrad1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.push_tetrad1 = QtWidgets.QPushButton(self.tetrad1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tetrad1.sizePolicy().hasHeightForWidth())
        self.push_tetrad1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_tetrad1.setFont(font)
        self.push_tetrad1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_tetrad1.setAutoFillBackground(False)
        self.push_tetrad1.setDefault(False)
        self.push_tetrad1.setFlat(True)
        self.push_tetrad1.setObjectName("push_tetrad1")
        self.gridLayout_3.addWidget(self.push_tetrad1, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.tetrad1)
        self.triad3 = QtWidgets.QFrame(MezcalPicker)
        self.triad3.setStyleSheet("background-color: rgb(102, 204, 0);")
        self.triad3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.triad3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.triad3.setObjectName("triad3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.triad3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.push_triad3 = QtWidgets.QPushButton(self.triad3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_triad3.sizePolicy().hasHeightForWidth())
        self.push_triad3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_triad3.setFont(font)
        self.push_triad3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_triad3.setAutoFillBackground(False)
        self.push_triad3.setDefault(False)
        self.push_triad3.setFlat(True)
        self.push_triad3.setObjectName("push_triad3")
        self.gridLayout_9.addWidget(self.push_triad3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.triad3)
        self.triad2 = QtWidgets.QFrame(MezcalPicker)
        self.triad2.setStyleSheet("background-color: rgb(204, 0, 102);")
        self.triad2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.triad2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.triad2.setObjectName("triad2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.triad2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.push_triad2 = QtWidgets.QPushButton(self.triad2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_triad2.sizePolicy().hasHeightForWidth())
        self.push_triad2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_triad2.setFont(font)
        self.push_triad2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_triad2.setAutoFillBackground(False)
        self.push_triad2.setDefault(False)
        self.push_triad2.setFlat(True)
        self.push_triad2.setObjectName("push_triad2")
        self.gridLayout_8.addWidget(self.push_triad2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.triad2)
        self.triad1 = QtWidgets.QFrame(MezcalPicker)
        self.triad1.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.triad1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.triad1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.triad1.setObjectName("triad1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.triad1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.push_triad1 = QtWidgets.QPushButton(self.triad1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_triad1.sizePolicy().hasHeightForWidth())
        self.push_triad1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_triad1.setFont(font)
        self.push_triad1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_triad1.setAutoFillBackground(False)
        self.push_triad1.setDefault(False)
        self.push_triad1.setFlat(True)
        self.push_triad1.setObjectName("push_triad1")
        self.gridLayout_7.addWidget(self.push_triad1, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.triad1)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.analogous3 = QtWidgets.QFrame(MezcalPicker)
        self.analogous3.setStyleSheet("background-color: rgb(102, 204, 0);")
        self.analogous3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analogous3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analogous3.setObjectName("analogous3")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.analogous3)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.push_analogous3 = QtWidgets.QPushButton(self.analogous3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_analogous3.sizePolicy().hasHeightForWidth())
        self.push_analogous3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_analogous3.setFont(font)
        self.push_analogous3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_analogous3.setAutoFillBackground(False)
        self.push_analogous3.setDefault(False)
        self.push_analogous3.setFlat(True)
        self.push_analogous3.setObjectName("push_analogous3")
        self.gridLayout_20.addWidget(self.push_analogous3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.analogous3, 2, 2, 1, 1)
        self.scompliment2 = QtWidgets.QFrame(MezcalPicker)
        self.scompliment2.setStyleSheet("background-color: rgb(204, 20, 0);")
        self.scompliment2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scompliment2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scompliment2.setObjectName("scompliment2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.scompliment2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.push_scompliment2 = QtWidgets.QPushButton(self.scompliment2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_scompliment2.sizePolicy().hasHeightForWidth())
        self.push_scompliment2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_scompliment2.setFont(font)
        self.push_scompliment2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_scompliment2.setAutoFillBackground(False)
        self.push_scompliment2.setDefault(False)
        self.push_scompliment2.setFlat(True)
        self.push_scompliment2.setObjectName("push_scompliment2")
        self.gridLayout_18.addWidget(self.push_scompliment2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.scompliment2, 0, 0, 1, 1)
        self.scompliment1 = QtWidgets.QFrame(MezcalPicker)
        self.scompliment1.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.scompliment1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scompliment1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scompliment1.setObjectName("scompliment1")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scompliment1)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.push_scompliment1 = QtWidgets.QPushButton(self.scompliment1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_scompliment1.sizePolicy().hasHeightForWidth())
        self.push_scompliment1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_scompliment1.setFont(font)
        self.push_scompliment1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_scompliment1.setAutoFillBackground(False)
        self.push_scompliment1.setDefault(False)
        self.push_scompliment1.setFlat(True)
        self.push_scompliment1.setObjectName("push_scompliment1")
        self.gridLayout_16.addWidget(self.push_scompliment1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.scompliment1, 0, 1, 1, 1)
        self.scompliment3 = QtWidgets.QFrame(MezcalPicker)
        self.scompliment3.setStyleSheet("background-color: rgb(204, 184, 0);")
        self.scompliment3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scompliment3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scompliment3.setObjectName("scompliment3")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.scompliment3)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.push_scompliment3 = QtWidgets.QPushButton(self.scompliment3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_scompliment3.sizePolicy().hasHeightForWidth())
        self.push_scompliment3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_scompliment3.setFont(font)
        self.push_scompliment3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_scompliment3.setAutoFillBackground(False)
        self.push_scompliment3.setDefault(False)
        self.push_scompliment3.setFlat(True)
        self.push_scompliment3.setObjectName("push_scompliment3")
        self.gridLayout_21.addWidget(self.push_scompliment3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.scompliment3, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.compliment2 = QtWidgets.QFrame(MezcalPicker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compliment2.sizePolicy().hasHeightForWidth())
        self.compliment2.setSizePolicy(sizePolicy)
        self.compliment2.setStyleSheet("background-color: rgb(204, 102, 0);")
        self.compliment2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.compliment2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compliment2.setObjectName("compliment2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.compliment2)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.push_compliment2 = QtWidgets.QPushButton(self.compliment2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_compliment2.sizePolicy().hasHeightForWidth())
        self.push_compliment2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_compliment2.setFont(font)
        self.push_compliment2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_compliment2.setAutoFillBackground(False)
        self.push_compliment2.setDefault(False)
        self.push_compliment2.setFlat(True)
        self.push_compliment2.setObjectName("push_compliment2")
        self.gridLayout_15.addWidget(self.push_compliment2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.compliment2, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.analogous2 = QtWidgets.QFrame(MezcalPicker)
        self.analogous2.setStyleSheet("background-color: rgb(204, 0, 102);")
        self.analogous2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analogous2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analogous2.setObjectName("analogous2")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.analogous2)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.push_analogous2 = QtWidgets.QPushButton(self.analogous2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_analogous2.sizePolicy().hasHeightForWidth())
        self.push_analogous2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_analogous2.setFont(font)
        self.push_analogous2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_analogous2.setAutoFillBackground(False)
        self.push_analogous2.setDefault(False)
        self.push_analogous2.setFlat(True)
        self.push_analogous2.setObjectName("push_analogous2")
        self.gridLayout_19.addWidget(self.push_analogous2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.analogous2, 2, 0, 1, 1)
        self.analogous1 = QtWidgets.QFrame(MezcalPicker)
        self.analogous1.setStyleSheet("background-color: rgb(0, 102, 204);")
        self.analogous1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analogous1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analogous1.setObjectName("analogous1")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.analogous1)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.push_analogous1 = QtWidgets.QPushButton(self.analogous1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_analogous1.sizePolicy().hasHeightForWidth())
        self.push_analogous1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Emoji")
        font.setPointSize(24)
        self.push_analogous1.setFont(font)
        self.push_analogous1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.push_analogous1.setAutoFillBackground(False)
        self.push_analogous1.setDefault(False)
        self.push_analogous1.setFlat(True)
        self.push_analogous1.setObjectName("push_analogous1")
        self.gridLayout_14.addWidget(self.push_analogous1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.analogous1, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.retranslateUi(MezcalPicker)
        self.push_scompliment1.clicked.connect(MezcalPicker.set_scompliments1)
        self.push_analogous3.clicked.connect(MezcalPicker.set_analogous3)
        self.push_analogous1.clicked.connect(MezcalPicker.set_analogous1)
        self.push_analogous2.clicked.connect(MezcalPicker.set_analogous2)
        self.push_compliment2.clicked.connect(MezcalPicker.set_compliments2)
        self.push_monochrome2.clicked.connect(MezcalPicker.set_monochrome2)
        self.push_monochrome3.clicked.connect(MezcalPicker.set_monochrome3)
        self.push_scompliment2.clicked.connect(MezcalPicker.set_scompliments2)
        self.push_scompliment3.clicked.connect(MezcalPicker.set_scompliments3)
        self.push_tetrad1.clicked.connect(MezcalPicker.set_tetrad1)
        self.push_tetrad2.clicked.connect(MezcalPicker.set_tetrad2)
        self.push_tetrad3.clicked.connect(MezcalPicker.set_tetrad3)
        self.push_triad1.clicked.connect(MezcalPicker.set_triad1)
        self.push_triad2.clicked.connect(MezcalPicker.set_triad2)
        self.push_triad3.clicked.connect(MezcalPicker.set_tetrad3)
        self.push_monochrome1.clicked.connect(MezcalPicker.set_monochrome1)
        self.push_tetrad4.clicked.connect(MezcalPicker.set_tetrad4)
        self.push_rum_color.clicked.connect(MezcalPicker.pick_theme)
        MezcalPicker.theme_color['QColor'].connect(MezcalPicker.set_theme)
        MezcalPicker.sig_analogous1['QString'].connect(self.analogous1.setStyleSheet)
        MezcalPicker.sig_analogous2['QString'].connect(self.analogous2.setStyleSheet)
        MezcalPicker.sig_analogous3['QString'].connect(self.analogous3.setStyleSheet)
        MezcalPicker.sig_compliments1['QString'].connect(self.scompliment1.setStyleSheet)
        MezcalPicker.sig_compliments2['QString'].connect(self.compliment2.setStyleSheet)
        MezcalPicker.sig_mono1['QString'].connect(self.monochrome1.setStyleSheet)
        MezcalPicker.sig_mono2['QString'].connect(self.monochrome2.setStyleSheet)
        MezcalPicker.sig_mono3['QString'].connect(self.monochrome3.setStyleSheet)
        MezcalPicker.sig_scompliments1['QString'].connect(self.scompliment1.setStyleSheet)
        MezcalPicker.sig_scompliments2['QString'].connect(self.scompliment2.setStyleSheet)
        MezcalPicker.sig_scompliments3['QString'].connect(self.scompliment3.setStyleSheet)
        MezcalPicker.sig_tetrad1['QString'].connect(self.tetrad1.setStyleSheet)
        MezcalPicker.sig_tetrad2['QString'].connect(self.tetrad2.setStyleSheet)
        MezcalPicker.sig_tetrad3['QString'].connect(self.tetrad3.setStyleSheet)
        MezcalPicker.sig_tetrad4['QString'].connect(self.tetrad4.setStyleSheet)
        MezcalPicker.sig_triad1['QString'].connect(self.triad1.setStyleSheet)
        MezcalPicker.sig_triad2['QString'].connect(self.triad2.setStyleSheet)
        MezcalPicker.sig_triad3['QString'].connect(self.triad3.setStyleSheet)
        QtCore.QMetaObject.connectSlotsByName(MezcalPicker)
        MezcalPicker.setTabOrder(self.push_analogous1, self.push_analogous2)
        MezcalPicker.setTabOrder(self.push_analogous2, self.push_analogous3)
        MezcalPicker.setTabOrder(self.push_analogous3, self.push_scompliment1)
        MezcalPicker.setTabOrder(self.push_scompliment1, self.push_compliment2)
        MezcalPicker.setTabOrder(self.push_compliment2, self.push_scompliment2)
        MezcalPicker.setTabOrder(self.push_scompliment2, self.push_scompliment3)
        MezcalPicker.setTabOrder(self.push_scompliment3, self.push_triad1)
        MezcalPicker.setTabOrder(self.push_triad1, self.push_triad2)
        MezcalPicker.setTabOrder(self.push_triad2, self.push_triad3)
        MezcalPicker.setTabOrder(self.push_triad3, self.push_tetrad1)
        MezcalPicker.setTabOrder(self.push_tetrad1, self.push_tetrad2)
        MezcalPicker.setTabOrder(self.push_tetrad2, self.push_tetrad3)
        MezcalPicker.setTabOrder(self.push_tetrad3, self.push_tetrad4)
        MezcalPicker.setTabOrder(self.push_tetrad4, self.push_monochrome1)
        MezcalPicker.setTabOrder(self.push_monochrome1, self.push_monochrome2)
        MezcalPicker.setTabOrder(self.push_monochrome2, self.push_monochrome3)
        MezcalPicker.setTabOrder(self.push_monochrome3, self.push_rum_color)

    def retranslateUi(self, MezcalPicker):
        _translate = QtCore.QCoreApplication.translate
        MezcalPicker.setWindowTitle(_translate("MezcalPicker", "Mezcal Color Scheme Picker"))
        self.push_tetrad4.setText(_translate("MezcalPicker", "🐊"))
        self.push_monochrome1.setText(_translate("MezcalPicker", "🐣"))
        self.push_monochrome2.setText(_translate("MezcalPicker", "🐤"))
        self.push_monochrome3.setText(_translate("MezcalPicker", "🐔"))
        self.push_tetrad3.setText(_translate("MezcalPicker", "🐙"))
        self.push_tetrad2.setText(_translate("MezcalPicker", "🐬"))
        self.push_rum_color.setText(_translate("MezcalPicker", "🌈"))
        self.tetrad1.setProperty("bg_style", _translate("MezcalPicker", "asdfsadfdsf"))
        self.push_tetrad1.setText(_translate("MezcalPicker", "🐋"))
        self.push_triad3.setText(_translate("MezcalPicker", "🐂"))
        self.push_triad2.setText(_translate("MezcalPicker", "🐇"))
        self.push_triad1.setText(_translate("MezcalPicker", "🐀"))
        self.push_analogous3.setText(_translate("MezcalPicker", "🌱"))
        self.push_scompliment2.setText(_translate("MezcalPicker", "🌛"))
        self.push_scompliment1.setText(_translate("MezcalPicker", "🌚"))
        self.push_scompliment3.setText(_translate("MezcalPicker", "🌜"))
        self.push_compliment2.setText(_translate("MezcalPicker", "🌝"))
        self.push_analogous2.setText(_translate("MezcalPicker", "⛈"))
        self.push_analogous1.setText(_translate("MezcalPicker", "🌞"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MezcalPicker = QtWidgets.QWidget()
    ui = Ui_MezcalPicker()
    ui.setupUi(MezcalPicker)
    MezcalPicker.show()
    sys.exit(app.exec_())
