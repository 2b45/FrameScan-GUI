# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrameScan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 813)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_vuln_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_all.setMinimumSize(QtCore.QSize(115, 28))
        self.pushButton_vuln_all.setStyleSheet("")
        self.pushButton_vuln_all.setObjectName("pushButton_vuln_all")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_all)
        self.pushButton_vuln_noall = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_noall.setMinimumSize(QtCore.QSize(115, 28))
        self.pushButton_vuln_noall.setStyleSheet("")
        self.pushButton_vuln_noall.setObjectName("pushButton_vuln_noall")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_noall)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_vuln_url = QtWidgets.QLabel(self.centralwidget)
        self.label_vuln_url.setObjectName("label_vuln_url")
        self.horizontalLayout_5.addWidget(self.label_vuln_url)
        self.lineEdit_vuln_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vuln_url.setMinimumSize(QtCore.QSize(0, 26))
        self.lineEdit_vuln_url.setStyleSheet("")
        self.lineEdit_vuln_url.setObjectName("lineEdit_vuln_url")
        self.horizontalLayout_5.addWidget(self.lineEdit_vuln_url)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_vuln_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_file.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_file.setStyleSheet("")
        self.pushButton_vuln_file.setObjectName("pushButton_vuln_file")
        self.horizontalLayout.addWidget(self.pushButton_vuln_file)
        self.pushButton_vuln_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_start.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_start.setStyleSheet("")
        self.pushButton_vuln_start.setObjectName("pushButton_vuln_start")
        self.horizontalLayout.addWidget(self.pushButton_vuln_start)
        self.pushButton_vuln_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_export.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_export.setStyleSheet("")
        self.pushButton_vuln_export.setObjectName("pushButton_vuln_export")
        self.horizontalLayout.addWidget(self.pushButton_vuln_export)
        self.pushButton_vuln_showplugins = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_showplugins.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_showplugins.setStyleSheet("")
        self.pushButton_vuln_showplugins.setObjectName("pushButton_vuln_showplugins")
        self.horizontalLayout.addWidget(self.pushButton_vuln_showplugins)
        self.pushButton_vuln_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vuln_exit.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_exit.setStyleSheet("")
        self.pushButton_vuln_exit.setObjectName("pushButton_vuln_exit")
        self.horizontalLayout.addWidget(self.pushButton_vuln_exit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.threadsnum = QtWidgets.QComboBox(self.centralwidget)
        self.threadsnum.setStyleSheet("")
        self.threadsnum.setObjectName("threadsnum")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.horizontalLayout_3.addWidget(self.threadsnum)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget_Plugins = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_Plugins.sizePolicy().hasHeightForWidth())
        self.treeWidget_Plugins.setSizePolicy(sizePolicy)
        self.treeWidget_Plugins.setMaximumSize(QtCore.QSize(240, 16777215))
        self.treeWidget_Plugins.setStyleSheet("")
        self.treeWidget_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_Plugins.setObjectName("treeWidget_Plugins")
        self.treeWidget_Plugins.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.horizontalLayout_4.addWidget(self.treeWidget_Plugins)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_vuln = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_vuln.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_vuln.setAutoFillBackground(False)
        self.tableWidget_vuln.setStyleSheet("")
        self.tableWidget_vuln.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_vuln.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_vuln.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_vuln.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_vuln.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_vuln.setObjectName("tableWidget_vuln")
        self.tableWidget_vuln.setColumnCount(4)
        self.tableWidget_vuln.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(3, item)
        self.tableWidget_vuln.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_vuln.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_vuln.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_vuln.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_vuln.verticalHeader().setVisible(False)
        self.tableWidget_vuln.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_vuln.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.tableWidget_vuln)
        self.textEdit_log = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_log.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_log.setStyleSheet("")
        self.textEdit_log.setObjectName("textEdit_log")
        self.verticalLayout.addWidget(self.textEdit_log)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1278, 26))
        self.menubar.setObjectName("menubar")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.action_dir_export = QtWidgets.QAction(MainWindow)
        self.action_dir_export.setObjectName("action_dir_export")
        self.action_dir_Import = QtWidgets.QAction(MainWindow)
        self.action_dir_Import.setObjectName("action_dir_Import")
        self.action_reload = QtWidgets.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_ideas = QtWidgets.QAction(MainWindow)
        self.action_ideas.setObjectName("action_ideas")
        self.action_zhiwen_export = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_export.setObjectName("action_zhiwen_export")
        self.action_zhiwen_import = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_import.setObjectName("action_zhiwen_import")
        self.action_port_export = QtWidgets.QAction(MainWindow)
        self.action_port_export.setObjectName("action_port_export")
        self.action_sub_export = QtWidgets.QAction(MainWindow)
        self.action_sub_export.setObjectName("action_sub_export")
        self.action_vuln_export = QtWidgets.QAction(MainWindow)
        self.action_vuln_export.setObjectName("action_vuln_export")
        self.action_port_import = QtWidgets.QAction(MainWindow)
        self.action_port_import.setObjectName("action_port_import")
        self.action_sub_import = QtWidgets.QAction(MainWindow)
        self.action_sub_import.setObjectName("action_sub_import")
        self.action_vuln_import = QtWidgets.QAction(MainWindow)
        self.action_vuln_import.setObjectName("action_vuln_import")
        self.action_vuln_reload = QtWidgets.QAction(MainWindow)
        self.action_vuln_reload.setObjectName("action_vuln_reload")
        self.action_vuln_showplubins = QtWidgets.QAction(MainWindow)
        self.action_vuln_showplubins.setObjectName("action_vuln_showplubins")
        self.action_dir_start = QtWidgets.QAction(MainWindow)
        self.action_dir_start.setObjectName("action_dir_start")
        self.action_dir_stop = QtWidgets.QAction(MainWindow)
        self.action_dir_stop.setObjectName("action_dir_stop")
        self.action_zhiwen_start = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_start.setObjectName("action_zhiwen_start")
        self.action_zhiwen_stop = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_stop.setObjectName("action_zhiwen_stop")
        self.action_port_start = QtWidgets.QAction(MainWindow)
        self.action_port_start.setObjectName("action_port_start")
        self.action_port_stop = QtWidgets.QAction(MainWindow)
        self.action_port_stop.setObjectName("action_port_stop")
        self.action_sub_start = QtWidgets.QAction(MainWindow)
        self.action_sub_start.setObjectName("action_sub_start")
        self.action_sub_stop = QtWidgets.QAction(MainWindow)
        self.action_sub_stop.setObjectName("action_sub_stop")
        self.action_vuln_start = QtWidgets.QAction(MainWindow)
        self.action_vuln_start.setObjectName("action_vuln_start")
        self.action_vuln_stop = QtWidgets.QAction(MainWindow)
        self.action_vuln_stop.setObjectName("action_vuln_stop")
        self.menu_5.addAction(self.action_vuln_start)
        self.menu_5.addAction(self.action_vuln_export)
        self.menu_5.addAction(self.action_vuln_import)
        self.menu_5.addAction(self.action_vuln_reload)
        self.menu_5.addAction(self.action_vuln_showplubins)
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_vuln_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FrameScan  by  qianxiao996"))
        self.pushButton_vuln_all.setText(_translate("MainWindow", "全  选"))
        self.pushButton_vuln_noall.setText(_translate("MainWindow", "反  选"))
        self.label_vuln_url.setText(_translate("MainWindow", " 目标："))
        self.pushButton_vuln_file.setText(_translate("MainWindow", "导入地址"))
        self.pushButton_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.pushButton_vuln_export.setText(_translate("MainWindow", "导出结果"))
        self.pushButton_vuln_showplugins.setText(_translate("MainWindow", "查看插件"))
        self.pushButton_vuln_exit.setText(_translate("MainWindow", "退出程序"))
        self.label.setText(_translate("MainWindow", "线程数量"))
        self.threadsnum.setItemText(0, _translate("MainWindow", "3"))
        self.threadsnum.setItemText(1, _translate("MainWindow", "5"))
        self.threadsnum.setItemText(2, _translate("MainWindow", "10"))
        self.threadsnum.setItemText(3, _translate("MainWindow", "15"))
        self.treeWidget_Plugins.headerItem().setText(0, _translate("MainWindow", "Plugins"))
        item = self.tableWidget_vuln.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "网页地址"))
        item = self.tableWidget_vuln.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "漏洞名称"))
        item = self.tableWidget_vuln.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "检测结果"))
        item = self.tableWidget_vuln.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Payload"))
        self.menu_5.setTitle(_translate("MainWindow", "选项"))
        self.action_dir_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_dir_Import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_update.setText(_translate("MainWindow", "更新"))
        self.action_version.setText(_translate("MainWindow", "版本"))
        self.action_ideas.setText(_translate("MainWindow", "意见反馈"))
        self.action_zhiwen_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_zhiwen_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_port_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_sub_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_vuln_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_port_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_sub_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_vuln_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_vuln_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_vuln_showplubins.setText(_translate("MainWindow", "查看插件信息"))
        self.action_dir_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_dir_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_zhiwen_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_zhiwen_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_port_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_port_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_sub_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_sub_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_vuln_stop.setText(_translate("MainWindow", "停止扫描"))

