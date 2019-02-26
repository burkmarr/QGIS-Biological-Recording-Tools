# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_biorec.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Biorec(object):
    def setupUi(self, Biorec):
        Biorec.setObjectName("Biorec")
        Biorec.resize(383, 607)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Biorec)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Biorec)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cboDatasource = QtWidgets.QComboBox(self.tab)
        self.cboDatasource.setObjectName("cboDatasource")
        self.cboDatasource.addItem("")
        self.cboDatasource.addItem("")
        self.horizontalLayout_12.addWidget(self.cboDatasource)
        self.butBrowse = QtWidgets.QPushButton(self.tab)
        self.butBrowse.setEnabled(True)
        self.butBrowse.setMinimumSize(QtCore.QSize(30, 0))
        self.butBrowse.setMaximumSize(QtCore.QSize(30, 16777215))
        self.butBrowse.setObjectName("butBrowse")
        self.horizontalLayout_12.addWidget(self.butBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblLayer = QtWidgets.QLabel(self.tab)
        self.lblLayer.setObjectName("lblLayer")
        self.gridLayout.addWidget(self.lblLayer, 0, 0, 1, 1)
        self.mlcbSourceLayer = QgsMapLayerComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mlcbSourceLayer.sizePolicy().hasHeightForWidth())
        self.mlcbSourceLayer.setSizePolicy(sizePolicy)
        self.mlcbSourceLayer.setAllowEmptyLayer(True)
        self.mlcbSourceLayer.setObjectName("mlcbSourceLayer")
        self.gridLayout.addWidget(self.mlcbSourceLayer, 0, 1, 1, 1)
        self.lblGridRefCol = QtWidgets.QLabel(self.tab)
        self.lblGridRefCol.setObjectName("lblGridRefCol")
        self.gridLayout.addWidget(self.lblGridRefCol, 1, 0, 1, 1)
        self.fcbGridRefCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbGridRefCol.sizePolicy().hasHeightForWidth())
        self.fcbGridRefCol.setSizePolicy(sizePolicy)
        self.fcbGridRefCol.setEditable(False)
        self.fcbGridRefCol.setAllowEmptyFieldName(True)
        self.fcbGridRefCol.setObjectName("fcbGridRefCol")
        self.gridLayout.addWidget(self.fcbGridRefCol, 1, 1, 1, 1)
        self.lblXCol = QtWidgets.QLabel(self.tab)
        self.lblXCol.setObjectName("lblXCol")
        self.gridLayout.addWidget(self.lblXCol, 2, 0, 1, 1)
        self.fcbXCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbXCol.sizePolicy().hasHeightForWidth())
        self.fcbXCol.setSizePolicy(sizePolicy)
        self.fcbXCol.setAllowEmptyFieldName(True)
        self.fcbXCol.setObjectName("fcbXCol")
        self.gridLayout.addWidget(self.fcbXCol, 2, 1, 1, 1)
        self.lblYCol = QtWidgets.QLabel(self.tab)
        self.lblYCol.setObjectName("lblYCol")
        self.gridLayout.addWidget(self.lblYCol, 3, 0, 1, 1)
        self.fcbYCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbYCol.sizePolicy().hasHeightForWidth())
        self.fcbYCol.setSizePolicy(sizePolicy)
        self.fcbYCol.setAllowEmptyFieldName(True)
        self.fcbYCol.setObjectName("fcbYCol")
        self.gridLayout.addWidget(self.fcbYCol, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.fcbDateCol = QgsFieldComboBox(self.tab)
        self.fcbDateCol.setAllowEmptyFieldName(True)
        self.fcbDateCol.setObjectName("fcbDateCol")
        self.gridLayout.addWidget(self.fcbDateCol, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.fcbDate2Col = QgsFieldComboBox(self.tab)
        self.fcbDate2Col.setAllowEmptyFieldName(True)
        self.fcbDate2Col.setObjectName("fcbDate2Col")
        self.gridLayout.addWidget(self.fcbDate2Col, 5, 1, 1, 1)
        self.lblAbundanceColumn = QtWidgets.QLabel(self.tab)
        self.lblAbundanceColumn.setObjectName("lblAbundanceColumn")
        self.gridLayout.addWidget(self.lblAbundanceColumn, 6, 0, 1, 1)
        self.fcbAbundanceCol = QgsFieldComboBox(self.tab)
        self.fcbAbundanceCol.setAllowEmptyFieldName(True)
        self.fcbAbundanceCol.setObjectName("fcbAbundanceCol")
        self.gridLayout.addWidget(self.fcbAbundanceCol, 6, 1, 1, 1)
        self.lblGroupingCol = QtWidgets.QLabel(self.tab)
        self.lblGroupingCol.setEnabled(True)
        self.lblGroupingCol.setObjectName("lblGroupingCol")
        self.gridLayout.addWidget(self.lblGroupingCol, 7, 0, 1, 1)
        self.fcbGroupingCol = QgsFieldComboBox(self.tab)
        self.fcbGroupingCol.setAllowEmptyFieldName(True)
        self.fcbGroupingCol.setObjectName("fcbGroupingCol")
        self.gridLayout.addWidget(self.fcbGroupingCol, 7, 1, 1, 1)
        self.lblTaxonCol = QtWidgets.QLabel(self.tab)
        self.lblTaxonCol.setObjectName("lblTaxonCol")
        self.gridLayout.addWidget(self.lblTaxonCol, 8, 0, 1, 1)
        self.fcbTaxonCol = QgsFieldComboBox(self.tab)
        self.fcbTaxonCol.setAllowEmptyFieldName(True)
        self.fcbTaxonCol.setObjectName("fcbTaxonCol")
        self.gridLayout.addWidget(self.fcbTaxonCol, 8, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.cbLoadTaxa = QtWidgets.QCheckBox(self.tab)
        self.cbLoadTaxa.setEnabled(True)
        self.cbLoadTaxa.setChecked(True)
        self.cbLoadTaxa.setObjectName("cbLoadTaxa")
        self.horizontalLayout_13.addWidget(self.cbLoadTaxa)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_13, 9, 1, 1, 1)
        self.cbIsScientific = QtWidgets.QCheckBox(self.tab)
        self.cbIsScientific.setEnabled(False)
        self.cbIsScientific.setChecked(False)
        self.cbIsScientific.setObjectName("cbIsScientific")
        self.gridLayout.addWidget(self.cbIsScientific, 9, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pswInputCRS = QgsProjectionSelectionWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswInputCRS.sizePolicy().hasHeightForWidth())
        self.pswInputCRS.setSizePolicy(sizePolicy)
        self.pswInputCRS.setObjectName("pswInputCRS")
        self.horizontalLayout_11.addWidget(self.pswInputCRS)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rbOutCrsBritish = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutCrsBritish.sizePolicy().hasHeightForWidth())
        self.rbOutCrsBritish.setSizePolicy(sizePolicy)
        self.rbOutCrsBritish.setMinimumSize(QtCore.QSize(50, 0))
        self.rbOutCrsBritish.setChecked(True)
        self.rbOutCrsBritish.setObjectName("rbOutCrsBritish")
        self.horizontalLayout_7.addWidget(self.rbOutCrsBritish)
        self.rbOutCrsIrish = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutCrsIrish.sizePolicy().hasHeightForWidth())
        self.rbOutCrsIrish.setSizePolicy(sizePolicy)
        self.rbOutCrsIrish.setMinimumSize(QtCore.QSize(50, 0))
        self.rbOutCrsIrish.setObjectName("rbOutCrsIrish")
        self.horizontalLayout_7.addWidget(self.rbOutCrsIrish)
        self.rbOutCrsInput = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutCrsInput.sizePolicy().hasHeightForWidth())
        self.rbOutCrsInput.setSizePolicy(sizePolicy)
        self.rbOutCrsInput.setMinimumSize(QtCore.QSize(50, 0))
        self.rbOutCrsInput.setObjectName("rbOutCrsInput")
        self.horizontalLayout_7.addWidget(self.rbOutCrsInput)
        self.rbOutCrsOther = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutCrsOther.sizePolicy().hasHeightForWidth())
        self.rbOutCrsOther.setSizePolicy(sizePolicy)
        self.rbOutCrsOther.setMinimumSize(QtCore.QSize(50, 0))
        self.rbOutCrsOther.setObjectName("rbOutCrsOther")
        self.horizontalLayout_7.addWidget(self.rbOutCrsOther)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.pswOutputCRS = QgsProjectionSelectionWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswOutputCRS.sizePolicy().hasHeightForWidth())
        self.pswOutputCRS.setSizePolicy(sizePolicy)
        self.pswOutputCRS.setObjectName("pswOutputCRS")
        self.verticalLayout_6.addWidget(self.pswOutputCRS)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tvTaxa = QtWidgets.QTreeView(self.tab_3)
        self.tvTaxa.setToolTip("")
        self.tvTaxa.setObjectName("tvTaxa")
        self.tvTaxa.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.tvTaxa)
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.butContract = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butContract.sizePolicy().hasHeightForWidth())
        self.butContract.setSizePolicy(sizePolicy)
        self.butContract.setMinimumSize(QtCore.QSize(25, 0))
        self.butContract.setMaximumSize(QtCore.QSize(25, 16777215))
        self.butContract.setObjectName("butContract")
        self.horizontalLayout.addWidget(self.butContract)
        self.butExpand = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butExpand.sizePolicy().hasHeightForWidth())
        self.butExpand.setSizePolicy(sizePolicy)
        self.butExpand.setMinimumSize(QtCore.QSize(25, 0))
        self.butExpand.setMaximumSize(QtCore.QSize(25, 16777215))
        self.butExpand.setObjectName("butExpand")
        self.horizontalLayout.addWidget(self.butExpand)
        self.butCheckAll = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butCheckAll.sizePolicy().hasHeightForWidth())
        self.butCheckAll.setSizePolicy(sizePolicy)
        self.butCheckAll.setMinimumSize(QtCore.QSize(55, 0))
        self.butCheckAll.setMaximumSize(QtCore.QSize(200, 16777215))
        self.butCheckAll.setObjectName("butCheckAll")
        self.horizontalLayout.addWidget(self.butCheckAll)
        self.butUncheckAll = QtWidgets.QPushButton(self.frame_2)
        self.butUncheckAll.setMinimumSize(QtCore.QSize(65, 0))
        self.butUncheckAll.setMaximumSize(QtCore.QSize(200, 16777215))
        self.butUncheckAll.setObjectName("butUncheckAll")
        self.horizontalLayout.addWidget(self.butUncheckAll)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.butGenTree = QtWidgets.QPushButton(self.frame_2)
        self.butGenTree.setObjectName("butGenTree")
        self.horizontalLayout.addWidget(self.butGenTree)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cboBatchMode = QtWidgets.QComboBox(self.tab_5)
        self.cboBatchMode.setMinimumSize(QtCore.QSize(130, 0))
        self.cboBatchMode.setMaximumSize(QtCore.QSize(130, 16777215))
        self.cboBatchMode.setObjectName("cboBatchMode")
        self.cboBatchMode.addItem("")
        self.cboBatchMode.addItem("")
        self.verticalLayout_5.addWidget(self.cboBatchMode)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leStyleFile = QtWidgets.QLineEdit(self.tab_5)
        self.leStyleFile.setObjectName("leStyleFile")
        self.horizontalLayout_4.addWidget(self.leStyleFile)
        self.pbBrowseStyleFile = QtWidgets.QPushButton(self.tab_5)
        self.pbBrowseStyleFile.setMinimumSize(QtCore.QSize(0, 0))
        self.pbBrowseStyleFile.setObjectName("pbBrowseStyleFile")
        self.horizontalLayout_4.addWidget(self.pbBrowseStyleFile)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.cbApplyStyle = QtWidgets.QCheckBox(self.tab_5)
        self.cbApplyStyle.setObjectName("cbApplyStyle")
        self.verticalLayout_5.addWidget(self.cbApplyStyle)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.hsLayerTransparency = QtWidgets.QSlider(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hsLayerTransparency.sizePolicy().hasHeightForWidth())
        self.hsLayerTransparency.setSizePolicy(sizePolicy)
        self.hsLayerTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.hsLayerTransparency.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hsLayerTransparency.setTickInterval(10)
        self.hsLayerTransparency.setObjectName("hsLayerTransparency")
        self.horizontalLayout_8.addWidget(self.hsLayerTransparency)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.mGroupBox = QgsCollapsibleGroupBox(self.tab_5)
        self.mGroupBox.setObjectName("mGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.cboOutputFormat = QtWidgets.QComboBox(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboOutputFormat.sizePolicy().hasHeightForWidth())
        self.cboOutputFormat.setSizePolicy(sizePolicy)
        self.cboOutputFormat.setEditable(False)
        self.cboOutputFormat.setObjectName("cboOutputFormat")
        self.cboOutputFormat.addItem("")
        self.cboOutputFormat.addItem("")
        self.cboOutputFormat.addItem("")
        self.cboOutputFormat.addItem("")
        self.cboOutputFormat.addItem("")
        self.horizontalLayout_9.addWidget(self.cboOutputFormat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.qgsOutputCRS = QgsProjectionSelectionWidget(self.mGroupBox)
        self.qgsOutputCRS.setObjectName("qgsOutputCRS")
        self.verticalLayout_2.addWidget(self.qgsOutputCRS)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leImageFolder = QtWidgets.QLineEdit(self.mGroupBox)
        self.leImageFolder.setObjectName("leImageFolder")
        self.horizontalLayout_3.addWidget(self.leImageFolder)
        self.pbBrowseImageFolder = QtWidgets.QPushButton(self.mGroupBox)
        self.pbBrowseImageFolder.setObjectName("pbBrowseImageFolder")
        self.horizontalLayout_3.addWidget(self.pbBrowseImageFolder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cbTaxonMetaData = QtWidgets.QCheckBox(self.mGroupBox)
        self.cbTaxonMetaData.setMinimumSize(QtCore.QSize(0, 0))
        self.cbTaxonMetaData.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbTaxonMetaData.setObjectName("cbTaxonMetaData")
        self.horizontalLayout_10.addWidget(self.cbTaxonMetaData)
        self.mlcbTaxonMetaDataLayer = QgsMapLayerComboBox(self.mGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mlcbTaxonMetaDataLayer.sizePolicy().hasHeightForWidth())
        self.mlcbTaxonMetaDataLayer.setSizePolicy(sizePolicy)
        self.mlcbTaxonMetaDataLayer.setObjectName("mlcbTaxonMetaDataLayer")
        self.horizontalLayout_10.addWidget(self.mlcbTaxonMetaDataLayer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.mGroupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.cboBatchMode.raise_()
        self.cbApplyStyle.raise_()
        self.mGroupBox.raise_()
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pteLog = QtWidgets.QPlainTextEdit(self.tab_4)
        self.pteLog.setObjectName("pteLog")
        self.verticalLayout_4.addWidget(self.pteLog)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.progBatch = QtWidgets.QProgressBar(Biorec)
        self.progBatch.setProperty("value", 0)
        self.progBatch.setObjectName("progBatch")
        self.horizontalLayout_6.addWidget(self.progBatch)
        self.pbCancel = QtWidgets.QPushButton(Biorec)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_6.addWidget(self.pbCancel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cboSymbol = QtWidgets.QComboBox(Biorec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboSymbol.sizePolicy().hasHeightForWidth())
        self.cboSymbol.setSizePolicy(sizePolicy)
        self.cboSymbol.setMinimumSize(QtCore.QSize(0, 0))
        self.cboSymbol.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cboSymbol.setObjectName("cboSymbol")
        self.cboSymbol.addItem("")
        self.cboSymbol.addItem("")
        self.horizontalLayout_5.addWidget(self.cboSymbol)
        self.cboMapType = QtWidgets.QComboBox(Biorec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMapType.sizePolicy().hasHeightForWidth())
        self.cboMapType.setSizePolicy(sizePolicy)
        self.cboMapType.setObjectName("cboMapType")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.cboMapType.addItem("")
        self.horizontalLayout_5.addWidget(self.cboMapType)
        self.dsbGridSize = QtWidgets.QDoubleSpinBox(Biorec)
        self.dsbGridSize.setDecimals(3)
        self.dsbGridSize.setMaximum(100000000.0)
        self.dsbGridSize.setSingleStep(100.0)
        self.dsbGridSize.setObjectName("dsbGridSize")
        self.horizontalLayout_5.addWidget(self.dsbGridSize)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.butMap = QtWidgets.QPushButton(Biorec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butMap.sizePolicy().hasHeightForWidth())
        self.butMap.setSizePolicy(sizePolicy)
        self.butMap.setMinimumSize(QtCore.QSize(32, 32))
        self.butMap.setMaximumSize(QtCore.QSize(32, 32))
        self.butMap.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/maptaxa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butMap.setIcon(icon)
        self.butMap.setIconSize(QtCore.QSize(30, 30))
        self.butMap.setObjectName("butMap")
        self.horizontalLayout_2.addWidget(self.butMap)
        self.butSaveImage = QtWidgets.QPushButton(Biorec)
        self.butSaveImage.setMinimumSize(QtCore.QSize(32, 32))
        self.butSaveImage.setMaximumSize(QtCore.QSize(32, 32))
        self.butSaveImage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/saveimage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSaveImage.setIcon(icon1)
        self.butSaveImage.setIconSize(QtCore.QSize(28, 28))
        self.butSaveImage.setObjectName("butSaveImage")
        self.horizontalLayout_2.addWidget(self.butSaveImage)
        self.butShowAll = QtWidgets.QPushButton(Biorec)
        self.butShowAll.setMinimumSize(QtCore.QSize(32, 32))
        self.butShowAll.setMaximumSize(QtCore.QSize(32, 32))
        self.butShowAll.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/layershow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butShowAll.setIcon(icon2)
        self.butShowAll.setIconSize(QtCore.QSize(26, 26))
        self.butShowAll.setObjectName("butShowAll")
        self.horizontalLayout_2.addWidget(self.butShowAll)
        self.butHideAll = QtWidgets.QPushButton(Biorec)
        self.butHideAll.setMinimumSize(QtCore.QSize(32, 32))
        self.butHideAll.setMaximumSize(QtCore.QSize(32, 32))
        self.butHideAll.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/layerhide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHideAll.setIcon(icon3)
        self.butHideAll.setIconSize(QtCore.QSize(26, 26))
        self.butHideAll.setObjectName("butHideAll")
        self.horizontalLayout_2.addWidget(self.butHideAll)
        self.butRemoveMap = QtWidgets.QPushButton(Biorec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRemoveMap.sizePolicy().hasHeightForWidth())
        self.butRemoveMap.setSizePolicy(sizePolicy)
        self.butRemoveMap.setMinimumSize(QtCore.QSize(32, 32))
        self.butRemoveMap.setMaximumSize(QtCore.QSize(32, 32))
        self.butRemoveMap.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/removelayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRemoveMap.setIcon(icon4)
        self.butRemoveMap.setIconSize(QtCore.QSize(30, 30))
        self.butRemoveMap.setObjectName("butRemoveMap")
        self.horizontalLayout_2.addWidget(self.butRemoveMap)
        self.butRemoveMaps = QtWidgets.QPushButton(Biorec)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRemoveMaps.sizePolicy().hasHeightForWidth())
        self.butRemoveMaps.setSizePolicy(sizePolicy)
        self.butRemoveMaps.setMinimumSize(QtCore.QSize(32, 32))
        self.butRemoveMaps.setMaximumSize(QtCore.QSize(32, 32))
        self.butRemoveMaps.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/removelayers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRemoveMaps.setIcon(icon5)
        self.butRemoveMaps.setIconSize(QtCore.QSize(30, 30))
        self.butRemoveMaps.setObjectName("butRemoveMaps")
        self.horizontalLayout_2.addWidget(self.butRemoveMaps)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.butHelp = QtWidgets.QPushButton(Biorec)
        self.butHelp.setMinimumSize(QtCore.QSize(30, 30))
        self.butHelp.setMaximumSize(QtCore.QSize(30, 30))
        self.butHelp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHelp.setIcon(icon6)
        self.butHelp.setIconSize(QtCore.QSize(24, 24))
        self.butHelp.setObjectName("butHelp")
        self.horizontalLayout_2.addWidget(self.butHelp)
        self.butGithub = QtWidgets.QPushButton(Biorec)
        self.butGithub.setMinimumSize(QtCore.QSize(30, 30))
        self.butGithub.setMaximumSize(QtCore.QSize(30, 30))
        self.butGithub.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butGithub.setIcon(icon7)
        self.butGithub.setIconSize(QtCore.QSize(24, 24))
        self.butGithub.setObjectName("butGithub")
        self.horizontalLayout_2.addWidget(self.butGithub)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Biorec)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Biorec)

    def retranslateUi(self, Biorec):
        _translate = QtCore.QCoreApplication.translate
        Biorec.setWindowTitle(_translate("Biorec", "FSC QGIS plugin"))
        self.cboDatasource.setItemText(0, _translate("Biorec", "Create source from CSV file"))
        self.cboDatasource.setItemText(1, _translate("Biorec", "Create source from R6 database"))
        self.butBrowse.setToolTip(_translate("Biorec", "Define data source"))
        self.butBrowse.setText(_translate("Biorec", "..."))
        self.lblLayer.setText(_translate("Biorec", "Source layer"))
        self.lblGridRefCol.setText(_translate("Biorec", "OS Grid Ref Column"))
        self.lblXCol.setText(_translate("Biorec", "X Column"))
        self.lblYCol.setText(_translate("Biorec", "Y Column"))
        self.label_3.setText(_translate("Biorec", "Start Date Column"))
        self.label_4.setText(_translate("Biorec", "End Date Column"))
        self.lblAbundanceColumn.setText(_translate("Biorec", "Abundance Column"))
        self.lblGroupingCol.setText(_translate("Biorec", "Grouping Column"))
        self.lblTaxonCol.setText(_translate("Biorec", "Taxon Column"))
        self.cbLoadTaxa.setToolTip(_translate("Biorec", "Select if taxon column contains scientific binomials"))
        self.cbLoadTaxa.setText(_translate("Biorec", "Load taxa on source selection"))
        self.cbIsScientific.setToolTip(_translate("Biorec", "Select if taxon column contains scientific binomials"))
        self.cbIsScientific.setText(_translate("Biorec", "Scientific names"))
        self.groupBox_2.setTitle(_translate("Biorec", "Input CRS"))
        self.groupBox.setTitle(_translate("Biorec", "Output CRS"))
        self.rbOutCrsBritish.setText(_translate("Biorec", "British"))
        self.rbOutCrsIrish.setText(_translate("Biorec", "Irish"))
        self.rbOutCrsInput.setText(_translate("Biorec", "Input"))
        self.rbOutCrsOther.setText(_translate("Biorec", "Other"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Biorec", "Data specification"))
        self.butContract.setToolTip(_translate("Biorec", "Contract all items"))
        self.butContract.setText(_translate("Biorec", "-"))
        self.butExpand.setToolTip(_translate("Biorec", "Expand all items"))
        self.butExpand.setText(_translate("Biorec", "+"))
        self.butCheckAll.setToolTip(_translate("Biorec", "Check all items"))
        self.butCheckAll.setText(_translate("Biorec", "Check all"))
        self.butUncheckAll.setToolTip(_translate("Biorec", "Uncheck all items"))
        self.butUncheckAll.setText(_translate("Biorec", "Uncheck all"))
        self.butGenTree.setToolTip(_translate("Biorec", "Create/recreate species tree"))
        self.butGenTree.setText(_translate("Biorec", "Reload taxa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Biorec", "Taxa"))
        self.cboBatchMode.setToolTip(_translate("Biorec", "Single or batch mode?"))
        self.cboBatchMode.setItemText(0, _translate("Biorec", "Single map mode"))
        self.cboBatchMode.setItemText(1, _translate("Biorec", "Batch map mode"))
        self.leStyleFile.setToolTip(_translate("Biorec", "Path of style file to apply to created maps"))
        self.pbBrowseStyleFile.setText(_translate("Biorec", "Browse style file"))
        self.cbApplyStyle.setText(_translate("Biorec", "Apply style"))
        self.label_2.setText(_translate("Biorec", "Transparency"))
        self.mGroupBox.setTitle(_translate("Biorec", "Output options"))
        self.label.setText(_translate("Biorec", "Format"))
        self.cboOutputFormat.setItemText(0, _translate("Biorec", "Image"))
        self.cboOutputFormat.setItemText(1, _translate("Biorec", "Shapefile"))
        self.cboOutputFormat.setItemText(2, _translate("Biorec", "GeoJSON"))
        self.cboOutputFormat.setItemText(3, _translate("Biorec", "Composer image"))
        self.cboOutputFormat.setItemText(4, _translate("Biorec", "Composer PDF"))
        self.leImageFolder.setToolTip(_translate("Biorec", "Folder for atlas images"))
        self.pbBrowseImageFolder.setText(_translate("Biorec", "Browse output folder"))
        self.cbTaxonMetaData.setText(_translate("Biorec", "Taxon Metadata Layer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Biorec", "Options"))
        self.pteLog.setToolTip(_translate("Biorec", "Information messages generated during map layer creation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Biorec", "Log"))
        self.progBatch.setToolTip(_translate("Biorec", "Shows progress in batch mode"))
        self.pbCancel.setToolTip(_translate("Biorec", "Cancel batch process"))
        self.pbCancel.setText(_translate("Biorec", "Cancel"))
        self.cboSymbol.setToolTip(_translate("Biorec", "Squares or circles?"))
        self.cboSymbol.setItemText(0, _translate("Biorec", "Atlas squares"))
        self.cboSymbol.setItemText(1, _translate("Biorec", "Atlas circles"))
        self.cboMapType.setToolTip(_translate("Biorec", "Type of map"))
        self.cboMapType.setItemText(0, _translate("Biorec", "Records as points"))
        self.cboMapType.setItemText(1, _translate("Biorec", "Records as grid squares"))
        self.cboMapType.setItemText(2, _translate("Biorec", "1 m atlas (10 fig gr)"))
        self.cboMapType.setItemText(3, _translate("Biorec", "10 m atlas (8 fig gr)"))
        self.cboMapType.setItemText(4, _translate("Biorec", "100 m atlas (6 fig gr)"))
        self.cboMapType.setItemText(5, _translate("Biorec", "1 km atlas (monads)"))
        self.cboMapType.setItemText(6, _translate("Biorec", "2 km atlas (tetrads)"))
        self.cboMapType.setItemText(7, _translate("Biorec", "5 km atlas (quadrants)"))
        self.cboMapType.setItemText(8, _translate("Biorec", "10 km atlas (hectads)"))
        self.cboMapType.setItemText(9, _translate("Biorec", "User-defined atlas size:"))
        self.dsbGridSize.setToolTip(_translate("Biorec", "<html><head/><body><p>Grid size for atlas - specify in units used by output CRS</p></body></html>"))
        self.butMap.setToolTip(_translate("Biorec", "Create map layer"))
        self.butSaveImage.setToolTip(_translate("Biorec", "Save temporary map layers as images or permanent layers"))
        self.butShowAll.setToolTip(_translate("Biorec", "Show all generated map layers"))
        self.butHideAll.setToolTip(_translate("Biorec", "Hide all generated map layers"))
        self.butRemoveMap.setToolTip(_translate("Biorec", "Remove last map layer"))
        self.butRemoveMaps.setToolTip(_translate("Biorec", "Remove all map layers"))
        self.butHelp.setToolTip(_translate("Biorec", "<html><head/><body><p><span style=\" font-size:12pt;\">Get more information about this tool and help on using it. This links to a webpage with up-to-date information about the tool. </span></p></body></html>"))
        self.butGithub.setToolTip(_translate("Biorec", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Report an issue with this tool.</span><span style=\" font-size:12pt;\"> Using this channel is the best way to get attention quickly. Issues can be bug reports, enhancement requests or just questions. Anyone can view current issues, but to add a new issue you will need to sign up for a free Github account (very easy).</span></p></body></html>"))

from qgscollapsiblegroupbox import QgsCollapsibleGroupBox
from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox
from qgsprojectionselectionwidget import QgsProjectionSelectionWidget
