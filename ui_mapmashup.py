# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mapmashup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mapmashup(object):
    def setupUi(self, Mapmashup):
        Mapmashup.setObjectName("Mapmashup")
        Mapmashup.resize(346, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(Mapmashup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.leImageFolder = QtWidgets.QLineEdit(Mapmashup)
        self.leImageFolder.setObjectName("leImageFolder")
        self.gridLayout.addWidget(self.leImageFolder, 0, 0, 1, 1)
        self.butBrowseImg = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butBrowseImg.sizePolicy().hasHeightForWidth())
        self.butBrowseImg.setSizePolicy(sizePolicy)
        self.butBrowseImg.setMinimumSize(QtCore.QSize(0, 0))
        self.butBrowseImg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.butBrowseImg.setObjectName("butBrowseImg")
        self.gridLayout.addWidget(self.butBrowseImg, 0, 1, 1, 1)
        self.leRegistrationFolder = QtWidgets.QLineEdit(Mapmashup)
        self.leRegistrationFolder.setObjectName("leRegistrationFolder")
        self.gridLayout.addWidget(self.leRegistrationFolder, 1, 0, 1, 1)
        self.butBrowseReg = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butBrowseReg.sizePolicy().hasHeightForWidth())
        self.butBrowseReg.setSizePolicy(sizePolicy)
        self.butBrowseReg.setMinimumSize(QtCore.QSize(0, 0))
        self.butBrowseReg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.butBrowseReg.setObjectName("butBrowseReg")
        self.gridLayout.addWidget(self.butBrowseReg, 1, 1, 1, 1)
        self.cboRegistrations = QtWidgets.QComboBox(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboRegistrations.sizePolicy().hasHeightForWidth())
        self.cboRegistrations.setSizePolicy(sizePolicy)
        self.cboRegistrations.setObjectName("cboRegistrations")
        self.gridLayout.addWidget(self.cboRegistrations, 2, 0, 1, 1)
        self.butRefresh = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRefresh.sizePolicy().hasHeightForWidth())
        self.butRefresh.setSizePolicy(sizePolicy)
        self.butRefresh.setMinimumSize(QtCore.QSize(0, 0))
        self.butRefresh.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.butRefresh.setObjectName("butRefresh")
        self.gridLayout.addWidget(self.butRefresh, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.leName = QtWidgets.QLineEdit(Mapmashup)
        self.leName.setObjectName("leName")
        self.horizontalLayout.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.hsTransparency = QtWidgets.QSlider(Mapmashup)
        self.hsTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.hsTransparency.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hsTransparency.setTickInterval(10)
        self.hsTransparency.setObjectName("hsTransparency")
        self.horizontalLayout_3.addWidget(self.hsTransparency)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbTransparentColour = QtWidgets.QCheckBox(self.groupBox)
        self.cbTransparentColour.setObjectName("cbTransparentColour")
        self.verticalLayout_2.addWidget(self.cbTransparentColour)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.mcbTransparentColour = QgsColorButton(self.groupBox)
        self.mcbTransparentColour.setColor(QtGui.QColor(255, 255, 255))
        self.mcbTransparentColour.setDefaultColor(QtGui.QColor(255, 255, 255))
        self.mcbTransparentColour.setObjectName("mcbTransparentColour")
        self.horizontalLayout_2.addWidget(self.mcbTransparentColour)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leStyleFile = QtWidgets.QLineEdit(Mapmashup)
        self.leStyleFile.setObjectName("leStyleFile")
        self.horizontalLayout_6.addWidget(self.leStyleFile)
        self.pbBrowseStyleFile = QtWidgets.QPushButton(Mapmashup)
        self.pbBrowseStyleFile.setMinimumSize(QtCore.QSize(100, 0))
        self.pbBrowseStyleFile.setObjectName("pbBrowseStyleFile")
        self.horizontalLayout_6.addWidget(self.pbBrowseStyleFile)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.cbApplyStyle = QtWidgets.QCheckBox(Mapmashup)
        self.cbApplyStyle.setObjectName("cbApplyStyle")
        self.verticalLayout.addWidget(self.cbApplyStyle)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.butLoadImage = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImage.sizePolicy().hasHeightForWidth())
        self.butLoadImage.setSizePolicy(sizePolicy)
        self.butLoadImage.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImage.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/mashup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImage.setIcon(icon)
        self.butLoadImage.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImage.setObjectName("butLoadImage")
        self.horizontalLayout_4.addWidget(self.butLoadImage)
        self.butLoadImageFile = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImageFile.sizePolicy().hasHeightForWidth())
        self.butLoadImageFile.setSizePolicy(sizePolicy)
        self.butLoadImageFile.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImageFile.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImageFile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/mashup2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImageFile.setIcon(icon1)
        self.butLoadImageFile.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImageFile.setObjectName("butLoadImageFile")
        self.horizontalLayout_4.addWidget(self.butLoadImageFile)
        self.butLoadImageBrowse = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImageBrowse.sizePolicy().hasHeightForWidth())
        self.butLoadImageBrowse.setSizePolicy(sizePolicy)
        self.butLoadImageBrowse.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImageBrowse.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImageBrowse.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/mashup3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImageBrowse.setIcon(icon2)
        self.butLoadImageBrowse.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImageBrowse.setObjectName("butLoadImageBrowse")
        self.horizontalLayout_4.addWidget(self.butLoadImageBrowse)
        self.butClearLast = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClearLast.sizePolicy().hasHeightForWidth())
        self.butClearLast.setSizePolicy(sizePolicy)
        self.butClearLast.setMinimumSize(QtCore.QSize(30, 30))
        self.butClearLast.setMaximumSize(QtCore.QSize(30, 30))
        self.butClearLast.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/removelayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClearLast.setIcon(icon3)
        self.butClearLast.setIconSize(QtCore.QSize(26, 26))
        self.butClearLast.setObjectName("butClearLast")
        self.horizontalLayout_4.addWidget(self.butClearLast)
        self.butClear = QtWidgets.QPushButton(Mapmashup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClear.sizePolicy().hasHeightForWidth())
        self.butClear.setSizePolicy(sizePolicy)
        self.butClear.setMinimumSize(QtCore.QSize(30, 30))
        self.butClear.setMaximumSize(QtCore.QSize(30, 30))
        self.butClear.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/removelayers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClear.setIcon(icon4)
        self.butClear.setIconSize(QtCore.QSize(26, 26))
        self.butClear.setObjectName("butClear")
        self.horizontalLayout_4.addWidget(self.butClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.butHelp = QtWidgets.QPushButton(Mapmashup)
        self.butHelp.setMinimumSize(QtCore.QSize(30, 30))
        self.butHelp.setMaximumSize(QtCore.QSize(30, 30))
        self.butHelp.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHelp.setIcon(icon5)
        self.butHelp.setIconSize(QtCore.QSize(24, 24))
        self.butHelp.setObjectName("butHelp")
        self.horizontalLayout_4.addWidget(self.butHelp)
        self.butGithub = QtWidgets.QPushButton(Mapmashup)
        self.butGithub.setMinimumSize(QtCore.QSize(30, 30))
        self.butGithub.setMaximumSize(QtCore.QSize(30, 30))
        self.butGithub.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butGithub.setIcon(icon6)
        self.butGithub.setIconSize(QtCore.QSize(24, 24))
        self.butGithub.setObjectName("butGithub")
        self.horizontalLayout_4.addWidget(self.butGithub)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.groupBox.raise_()
        self.cbApplyStyle.raise_()
        self.butRefresh.raise_()
        self.butBrowseReg.raise_()
        self.butBrowseImg.raise_()
        self.leImageFolder.raise_()

        self.retranslateUi(Mapmashup)
        QtCore.QMetaObject.connectSlotsByName(Mapmashup)

    def retranslateUi(self, Mapmashup):
        _translate = QtCore.QCoreApplication.translate
        Mapmashup.setWindowTitle(_translate("Mapmashup", "FSC QGIS plugin"))
        self.leImageFolder.setToolTip(_translate("Mapmashup", "Path of folder for temp image files"))
        self.butBrowseImg.setToolTip(_translate("Mapmashup", "Browse for image folder"))
        self.butBrowseImg.setText(_translate("Mapmashup", "Image folder"))
        self.leRegistrationFolder.setToolTip(_translate("Mapmashup", "Folder where WLD files are kept"))
        self.butBrowseReg.setToolTip(_translate("Mapmashup", "Browse for folder containing WLD files"))
        self.butBrowseReg.setText(_translate("Mapmashup", "Registration folder"))
        self.cboRegistrations.setToolTip(_translate("Mapmashup", "Select WLD registration info"))
        self.butRefresh.setToolTip(_translate("Mapmashup", "Refresh the list of WLD files"))
        self.butRefresh.setText(_translate("Mapmashup", "Refresh"))
        self.label_2.setText(_translate("Mapmashup", "Layer name"))
        self.leName.setToolTip(_translate("Mapmashup", "Text to be used in layer name"))
        self.label.setText(_translate("Mapmashup", "Global transparency"))
        self.hsTransparency.setToolTip(_translate("Mapmashup", "Set the layer\'s global transparency"))
        self.groupBox.setTitle(_translate("Mapmashup", "Transparent colour"))
        self.cbTransparentColour.setText(_translate("Mapmashup", "Set transparent background colour"))
        self.label_3.setText(_translate("Mapmashup", "Colour"))
        self.mcbTransparentColour.setToolTip(_translate("Mapmashup", "Use this button to select transparent colour"))
        self.mcbTransparentColour.setColorDialogTitle(_translate("Mapmashup", "Select transparent colour"))
        self.leStyleFile.setToolTip(_translate("Mapmashup", "Path of style file to apply to created maps"))
        self.pbBrowseStyleFile.setText(_translate("Mapmashup", "Browse style file"))
        self.cbApplyStyle.setText(_translate("Mapmashup", "Apply style"))
        self.butLoadImage.setToolTip(_translate("Mapmashup", "Paste image from clipboard to map with specified registration"))
        self.butLoadImageFile.setToolTip(_translate("Mapmashup", "Paste most recent  image from image folder to map with specified registration"))
        self.butLoadImageBrowse.setToolTip(_translate("Mapmashup", "Browse for image to paste into map with specified registration"))
        self.butClearLast.setToolTip(_translate("Mapmashup", "Remove last mashed map"))
        self.butClear.setToolTip(_translate("Mapmashup", "Remove all mashed maps"))
        self.butHelp.setToolTip(_translate("Mapmashup", "<html><head/><body><p><span style=\" font-size:12pt;\">Get more information about this tool and help on using it. This links to a webpage with up-to-date information about the tool. </span></p></body></html>"))
        self.butGithub.setToolTip(_translate("Mapmashup", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Report an issue with this tool.</span><span style=\" font-size:12pt;\"> Using this channel is the best way to get attention quickly. Issues can be bug reports, enhancement requests or just questions. Anyone can view current issues, but to add a new issue you will need to sign up for a free Github account (very easy).</span></p></body></html>"))

from qgscolorbutton import QgsColorButton
