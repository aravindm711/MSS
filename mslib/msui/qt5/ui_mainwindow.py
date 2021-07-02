# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mslib/msui/ui/ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MSSMainWindow(object):
    def setupUi(self, MSSMainWindow):
        MSSMainWindow.setObjectName("MSSMainWindow")
        MSSMainWindow.resize(769, 736)
        MSSMainWindow.setMinimumSize(QtCore.QSize(507, 736))
        self.centralwidget = QtWidgets.QWidget(MSSMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.openViewsGb = QtWidgets.QGroupBox(self.centralwidget)
        self.openViewsGb.setObjectName("openViewsGb")
        self.openViewsVL = QtWidgets.QVBoxLayout(self.openViewsGb)
        self.openViewsVL.setContentsMargins(8, 8, 8, 8)
        self.openViewsVL.setObjectName("openViewsVL")
        self.openViewsLabel = QtWidgets.QLabel(self.openViewsGb)
        self.openViewsLabel.setObjectName("openViewsLabel")
        self.openViewsVL.addWidget(self.openViewsLabel)
        self.listViews = QtWidgets.QListWidget(self.openViewsGb)
        self.listViews.setObjectName("listViews")
        self.openViewsVL.addWidget(self.listViews)
        self.gridLayout.addWidget(self.openViewsGb, 2, 0, 1, 1)
        self.userOptionsHL = QtWidgets.QHBoxLayout()
        self.userOptionsHL.setContentsMargins(0, -1, 0, -1)
        self.userOptionsHL.setObjectName("userOptionsHL")
        self.mscStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.mscStatusLabel.setWordWrap(True)
        self.mscStatusLabel.setObjectName("mscStatusLabel")
        self.userOptionsHL.addWidget(self.mscStatusLabel)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.userOptionsHL.addWidget(self.usernameLabel, 0, QtCore.Qt.AlignRight)
        self.userOptionsTb = QtWidgets.QToolButton(self.centralwidget)
        self.userOptionsTb.setStyleSheet("::menu-indicator { image: none; }")
        self.userOptionsTb.setText("")
        self.userOptionsTb.setObjectName("userOptionsTb")
        self.userOptionsHL.addWidget(self.userOptionsTb, 0, QtCore.Qt.AlignRight)
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setObjectName("connectBtn")
        self.userOptionsHL.addWidget(self.connectBtn, 0, QtCore.Qt.AlignRight)
        self.userOptionsHL.setStretch(0, 1)
        self.gridLayout.addLayout(self.userOptionsHL, 0, 0, 1, 2)
        self.openProjectsGb = QtWidgets.QGroupBox(self.centralwidget)
        self.openProjectsGb.setTitle("")
        self.openProjectsGb.setObjectName("openProjectsGb")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.openProjectsGb)
        self.gridLayout_3.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.workingStatusLabel = QtWidgets.QLabel(self.openProjectsGb)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.workingStatusLabel.setFont(font)
        self.workingStatusLabel.setWordWrap(True)
        self.workingStatusLabel.setObjectName("workingStatusLabel")
        self.gridLayout_3.addWidget(self.workingStatusLabel, 2, 0, 1, 2)
        self.workLocallyCheckbox = QtWidgets.QCheckBox(self.openProjectsGb)
        self.workLocallyCheckbox.setObjectName("workLocallyCheckbox")
        self.gridLayout_3.addWidget(self.workLocallyCheckbox, 3, 0, 1, 1)
        self.openProjectsMSCLabel = QtWidgets.QLabel(self.openProjectsGb)
        self.openProjectsMSCLabel.setObjectName("openProjectsMSCLabel")
        self.gridLayout_3.addWidget(self.openProjectsMSCLabel, 0, 0, 1, 1)
        self.listProjectsMSC = QtWidgets.QListWidget(self.openProjectsGb)
        self.listProjectsMSC.setObjectName("listProjectsMSC")
        self.gridLayout_3.addWidget(self.listProjectsMSC, 1, 0, 1, 2)
        self.serverOptionsCb = QtWidgets.QComboBox(self.openProjectsGb)
        self.serverOptionsCb.setObjectName("serverOptionsCb")
        self.serverOptionsCb.addItem("")
        self.serverOptionsCb.addItem("")
        self.serverOptionsCb.addItem("")
        self.gridLayout_3.addWidget(self.serverOptionsCb, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.openProjectsGb, 1, 1, 2, 1)
        self.openFlightTracksGb = QtWidgets.QGroupBox(self.centralwidget)
        self.openFlightTracksGb.setTitle("")
        self.openFlightTracksGb.setObjectName("openFlightTracksGb")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.openFlightTracksGb)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openFlightTracksLabel = QtWidgets.QLabel(self.openFlightTracksGb)
        self.openFlightTracksLabel.setObjectName("openFlightTracksLabel")
        self.verticalLayout.addWidget(self.openFlightTracksLabel)
        self.listFlightTracks = QtWidgets.QListWidget(self.openFlightTracksGb)
        self.listFlightTracks.setObjectName("listFlightTracks")
        self.verticalLayout.addWidget(self.listFlightTracks)
        self.gridLayout.addWidget(self.openFlightTracksGb, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        MSSMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MSSMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImportFlightTrack = QtWidgets.QMenu(self.menuFile)
        self.menuImportFlightTrack.setObjectName("menuImportFlightTrack")
        self.menuExportActiveFlightTrack = QtWidgets.QMenu(self.menuFile)
        self.menuExportActiveFlightTrack.setObjectName("menuExportActiveFlightTrack")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuViews = QtWidgets.QMenu(self.menubar)
        self.menuViews.setObjectName("menuViews")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuProjectProperties = QtWidgets.QMenu(self.menuProject)
        self.menuProjectProperties.setObjectName("menuProjectProperties")
        MSSMainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MSSMainWindow)
        self.statusBar.setObjectName("statusBar")
        MSSMainWindow.setStatusBar(self.statusBar)
        self.actionSaveActiveFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrack.setObjectName("actionSaveActiveFlightTrack")
        self.actionSaveActiveFlightTrackAs = QtWidgets.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrackAs.setObjectName("actionSaveActiveFlightTrackAs")
        self.actionAboutMSUI = QtWidgets.QAction(MSSMainWindow)
        self.actionAboutMSUI.setObjectName("actionAboutMSUI")
        self.actionOnlineHelp = QtWidgets.QAction(MSSMainWindow)
        self.actionOnlineHelp.setObjectName("actionOnlineHelp")
        self.actionOpenFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionOpenFlightTrack.setObjectName("actionOpenFlightTrack")
        self.actionNewFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionNewFlightTrack.setObjectName("actionNewFlightTrack")
        self.actionQuit = QtWidgets.QAction(MSSMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionShortcuts = QtWidgets.QAction(MSSMainWindow)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionActivateSelectedFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionActivateSelectedFlightTrack.setObjectName("actionActivateSelectedFlightTrack")
        self.actionCloseSelectedFlightTrack = QtWidgets.QAction(MSSMainWindow)
        self.actionCloseSelectedFlightTrack.setObjectName("actionCloseSelectedFlightTrack")
        self.actionUpdater = QtWidgets.QAction(MSSMainWindow)
        self.actionUpdater.setObjectName("actionUpdater")
        self.actionConfiguration = QtWidgets.QAction(MSSMainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionTopView = QtWidgets.QAction(MSSMainWindow)
        self.actionTopView.setObjectName("actionTopView")
        self.actionSideView = QtWidgets.QAction(MSSMainWindow)
        self.actionSideView.setObjectName("actionSideView")
        self.actionTableView = QtWidgets.QAction(MSSMainWindow)
        self.actionTableView.setObjectName("actionTableView")
        self.actionLinearView = QtWidgets.QAction(MSSMainWindow)
        self.actionLinearView.setObjectName("actionLinearView")
        self.actionChat = QtWidgets.QAction(MSSMainWindow)
        self.actionChat.setObjectName("actionChat")
        self.actionVersionHistory = QtWidgets.QAction(MSSMainWindow)
        self.actionVersionHistory.setObjectName("actionVersionHistory")
        self.actionManageUsers = QtWidgets.QAction(MSSMainWindow)
        self.actionManageUsers.setObjectName("actionManageUsers")
        self.actionMSColab = QtWidgets.QAction(MSSMainWindow)
        self.actionMSColab.setObjectName("actionMSColab")
        self.actionAddProject = QtWidgets.QAction(MSSMainWindow)
        self.actionAddProject.setObjectName("actionAddProject")
        self.actionEditProject = QtWidgets.QAction(MSSMainWindow)
        self.actionEditProject.setObjectName("actionEditProject")
        self.actionDeleteProject = QtWidgets.QAction(MSSMainWindow)
        self.actionDeleteProject.setObjectName("actionDeleteProject")
        self.menuFile.addAction(self.actionNewFlightTrack)
        self.menuFile.addAction(self.actionOpenFlightTrack)
        self.menuFile.addAction(self.actionAddProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionActivateSelectedFlightTrack)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveActiveFlightTrack)
        self.menuFile.addAction(self.actionSaveActiveFlightTrackAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCloseSelectedFlightTrack)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuImportFlightTrack.menuAction())
        self.menuFile.addAction(self.menuExportActiveFlightTrack.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConfiguration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuHelp.addAction(self.actionMSColab)
        self.menuHelp.addAction(self.actionUpdater)
        self.menuHelp.addAction(self.actionOnlineHelp)
        self.menuHelp.addAction(self.actionAboutMSUI)
        self.menuViews.addAction(self.actionTopView)
        self.menuViews.addAction(self.actionSideView)
        self.menuViews.addAction(self.actionTableView)
        self.menuViews.addAction(self.actionLinearView)
        self.menuProjectProperties.addAction(self.actionEditProject)
        self.menuProjectProperties.addAction(self.actionDeleteProject)
        self.menuProject.addAction(self.actionChat)
        self.menuProject.addAction(self.actionVersionHistory)
        self.menuProject.addAction(self.actionManageUsers)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.menuProjectProperties.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MSSMainWindow)
        self.actionQuit.triggered.connect(MSSMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MSSMainWindow)
        MSSMainWindow.setTabOrder(self.connectBtn, self.userOptionsTb)
        MSSMainWindow.setTabOrder(self.userOptionsTb, self.listFlightTracks)
        MSSMainWindow.setTabOrder(self.listFlightTracks, self.listViews)
        MSSMainWindow.setTabOrder(self.listViews, self.listProjectsMSC)
        MSSMainWindow.setTabOrder(self.listProjectsMSC, self.workLocallyCheckbox)
        MSSMainWindow.setTabOrder(self.workLocallyCheckbox, self.serverOptionsCb)

    def retranslateUi(self, MSSMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MSSMainWindow.setWindowTitle(_translate("MSSMainWindow", "Mission Support System"))
        self.openViewsLabel.setText(_translate("MSSMainWindow", "Open Views:"))
        self.mscStatusLabel.setText(_translate("MSSMainWindow", "Status: Disconnected"))
        self.usernameLabel.setText(_translate("MSSMainWindow", "User"))
        self.connectBtn.setToolTip(_translate("MSSMainWindow", "Connect to an MSColab Server"))
        self.connectBtn.setText(_translate("MSSMainWindow", "Connect to MSColab"))
        self.workingStatusLabel.setText(_translate("MSSMainWindow", "No projects selected"))
        self.workLocallyCheckbox.setText(_translate("MSSMainWindow", "Work Asynchronously"))
        self.openProjectsMSCLabel.setText(_translate("MSSMainWindow", "Open Projects:"))
        self.serverOptionsCb.setItemText(0, _translate("MSSMainWindow", "Server Options"))
        self.serverOptionsCb.setItemText(1, _translate("MSSMainWindow", "Fetch From Server"))
        self.serverOptionsCb.setItemText(2, _translate("MSSMainWindow", "Save To Server"))
        self.openFlightTracksLabel.setText(_translate("MSSMainWindow", "Open Flight Tracks:"))
        self.menuFile.setTitle(_translate("MSSMainWindow", "&File"))
        self.menuImportFlightTrack.setTitle(_translate("MSSMainWindow", "Import Flight Track"))
        self.menuExportActiveFlightTrack.setTitle(_translate("MSSMainWindow", "Export Flight Track"))
        self.menuHelp.setTitle(_translate("MSSMainWindow", "&Help"))
        self.menuViews.setTitle(_translate("MSSMainWindow", "Views"))
        self.menuProject.setTitle(_translate("MSSMainWindow", "Project"))
        self.menuProjectProperties.setTitle(_translate("MSSMainWindow", "Project Properties"))
        self.actionSaveActiveFlightTrack.setText(_translate("MSSMainWindow", "&Save Active Flight Track"))
        self.actionSaveActiveFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+S"))
        self.actionSaveActiveFlightTrackAs.setText(_translate("MSSMainWindow", "Save Active Flight Track As"))
        self.actionSaveActiveFlightTrackAs.setShortcut(_translate("MSSMainWindow", "Ctrl+Shift+S"))
        self.actionAboutMSUI.setText(_translate("MSSMainWindow", "&About MSUI"))
        self.actionOnlineHelp.setText(_translate("MSSMainWindow", "&Online Help"))
        self.actionOpenFlightTrack.setText(_translate("MSSMainWindow", "&Open Flight Track"))
        self.actionOpenFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+O"))
        self.actionNewFlightTrack.setText(_translate("MSSMainWindow", "&New Flight Track"))
        self.actionNewFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MSSMainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MSSMainWindow", "Ctrl+Q"))
        self.actionShortcuts.setText(_translate("MSSMainWindow", "&Shortcuts"))
        self.actionShortcuts.setShortcut(_translate("MSSMainWindow", "Alt+S"))
        self.actionActivateSelectedFlightTrack.setText(_translate("MSSMainWindow", "&Activate Selected Flight Track"))
        self.actionCloseSelectedFlightTrack.setText(_translate("MSSMainWindow", "&Close Selected Flight Track"))
        self.actionUpdater.setText(_translate("MSSMainWindow", "&Updater"))
        self.actionConfiguration.setText(_translate("MSSMainWindow", "&Configuration"))
        self.actionConfiguration.setShortcut(_translate("MSSMainWindow", "Ctrl+,"))
        self.actionTopView.setText(_translate("MSSMainWindow", "&Top View (Horizontal Section)"))
        self.actionTopView.setShortcut(_translate("MSSMainWindow", "Meta+H"))
        self.actionSideView.setText(_translate("MSSMainWindow", "&Side View (Vertical Section)"))
        self.actionSideView.setShortcut(_translate("MSSMainWindow", "Meta+V"))
        self.actionTableView.setText(_translate("MSSMainWindow", "&Table View"))
        self.actionTableView.setShortcut(_translate("MSSMainWindow", "Meta+T"))
        self.actionLinearView.setText(_translate("MSSMainWindow", "&Linear View"))
        self.actionLinearView.setShortcut(_translate("MSSMainWindow", "Meta+L"))
        self.actionChat.setText(_translate("MSSMainWindow", "&Chat"))
        self.actionVersionHistory.setText(_translate("MSSMainWindow", "&Version History"))
        self.actionManageUsers.setText(_translate("MSSMainWindow", "&Manage Users"))
        self.actionMSColab.setText(_translate("MSSMainWindow", "&MSColab"))
        self.actionAddProject.setText(_translate("MSSMainWindow", "&Add Project"))
        self.actionEditProject.setText(_translate("MSSMainWindow", "&Edit Project"))
        self.actionDeleteProject.setText(_translate("MSSMainWindow", "&Delete Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MSSMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MSSMainWindow()
    ui.setupUi(MSSMainWindow)
    MSSMainWindow.show()
    sys.exit(app.exec_())
