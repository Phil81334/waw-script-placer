# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPJTXSg.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 591)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 100))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background: rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	opacity: 100;\n"
"	border: 2px solid #0800ff;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMaximumSize(QSize(16777215, 50))
        self.headerFrame.setStyleSheet(u"#headerFrame{\n"
"	background: rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	opacity: 100;\n"
"	border: 2px solid #03e3fc;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.headerLabel = QLabel(self.headerFrame)
        self.headerLabel.setObjectName(u"headerLabel")
        sizePolicy.setHeightForWidth(self.headerLabel.sizePolicy().hasHeightForWidth())
        self.headerLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setPointSize(12)
        font.setBold(True)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet(u"#headerLabel{\n"
"	color: rgb(188, 0, 3);\n"
"	font-family: Georgia;\n"
"}")
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.headerLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.discordBtn = QPushButton(self.headerFrame)
        self.discordBtn.setObjectName(u"discordBtn")
        sizePolicy.setHeightForWidth(self.discordBtn.sizePolicy().hasHeightForWidth())
        self.discordBtn.setSizePolicy(sizePolicy)
        self.discordBtn.setMinimumSize(QSize(0, 0))
        self.discordBtn.setStyleSheet(u"#discordBtn{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#discordBtn:pressed{\n"
"	background: #03e3fc;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/discord.png", QSize(), QIcon.Normal, QIcon.Off)
        self.discordBtn.setIcon(icon)
        self.discordBtn.setIconSize(QSize(36, 48))
        self.discordBtn.setFlat(False)

        self.horizontalLayout.addWidget(self.discordBtn)

        self.websiteBtn = QPushButton(self.headerFrame)
        self.websiteBtn.setObjectName(u"websiteBtn")
        sizePolicy.setHeightForWidth(self.websiteBtn.sizePolicy().hasHeightForWidth())
        self.websiteBtn.setSizePolicy(sizePolicy)
        self.websiteBtn.setMinimumSize(QSize(0, 0))
        self.websiteBtn.setStyleSheet(u"#websiteBtn{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#websiteBtn:pressed{\n"
"	background: #03e3fc;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/logo_64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.websiteBtn.setIcon(icon1)
        self.websiteBtn.setIconSize(QSize(30, 48))

        self.horizontalLayout.addWidget(self.websiteBtn)

        self.youtubeBtn = QPushButton(self.headerFrame)
        self.youtubeBtn.setObjectName(u"youtubeBtn")
        sizePolicy.setHeightForWidth(self.youtubeBtn.sizePolicy().hasHeightForWidth())
        self.youtubeBtn.setSizePolicy(sizePolicy)
        self.youtubeBtn.setMinimumSize(QSize(0, 0))
        self.youtubeBtn.setStyleSheet(u"#youtubeBtn{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#youtubeBtn:pressed{\n"
"	background: #03e3fc;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/youtubeV3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.youtubeBtn.setIcon(icon2)
        self.youtubeBtn.setIconSize(QSize(36, 48))

        self.horizontalLayout.addWidget(self.youtubeBtn)

        self.headerHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.headerHSpacer)

        self.minimiseBtn = QPushButton(self.headerFrame)
        self.minimiseBtn.setObjectName(u"minimiseBtn")
        sizePolicy.setHeightForWidth(self.minimiseBtn.sizePolicy().hasHeightForWidth())
        self.minimiseBtn.setSizePolicy(sizePolicy)
        self.minimiseBtn.setStyleSheet(u"#minimiseBtn{\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"#minimiseBtn:pressed{\n"
"	background: #03e3fc;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimiseBtn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.minimiseBtn)

        self.closeBtn = QPushButton(self.headerFrame)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setStyleSheet(u"#closeBtn{\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"#closeBtn:pressed{\n"
"	background: red;\n"
"}\n"
"\n"
"#closeBtn:pressed{\n"
"	background: red;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon4)

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout.addWidget(self.headerFrame)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"#mainFrame{\n"
"	background: rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	opacity: 100;\n"
"	border: 2px solid #03e3fc;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.mainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(400, 10, 231, 101))
        self.frame.setStyleSheet(u"#frame{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 6)
        self.blankMapRadioBtn = QRadioButton(self.frame)
        self.blankMapRadioBtn.setObjectName(u"blankMapRadioBtn")
        sizePolicy.setHeightForWidth(self.blankMapRadioBtn.sizePolicy().hasHeightForWidth())
        self.blankMapRadioBtn.setSizePolicy(sizePolicy)
        self.blankMapRadioBtn.setLayoutDirection(Qt.RightToLeft)
        self.blankMapRadioBtn.setAutoFillBackground(False)
        self.blankMapRadioBtn.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")

        self.verticalLayout_2.addWidget(self.blankMapRadioBtn, 0, Qt.AlignLeft)

        self.setupMapRadioBtn = QRadioButton(self.frame)
        self.setupMapRadioBtn.setObjectName(u"setupMapRadioBtn")
        sizePolicy.setHeightForWidth(self.setupMapRadioBtn.sizePolicy().hasHeightForWidth())
        self.setupMapRadioBtn.setSizePolicy(sizePolicy)
        self.setupMapRadioBtn.setLayoutDirection(Qt.RightToLeft)
        self.setupMapRadioBtn.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.setupMapRadioBtn.setChecked(True)

        self.verticalLayout_2.addWidget(self.setupMapRadioBtn, 0, Qt.AlignLeft)

        self.customMap = QRadioButton(self.frame)
        self.customMap.setObjectName(u"customMap")
        sizePolicy.setHeightForWidth(self.customMap.sizePolicy().hasHeightForWidth())
        self.customMap.setSizePolicy(sizePolicy)
        self.customMap.setLayoutDirection(Qt.RightToLeft)
        self.customMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")

        self.verticalLayout_2.addWidget(self.customMap, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton_5 = QToolButton(self.frame_2)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(0, 21))
        self.toolButton_5.setMaximumSize(QSize(16777215, 21))
        self.toolButton_5.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_2.addWidget(self.toolButton_5)

        self.custMapFileTextBox = QLineEdit(self.frame_2)
        self.custMapFileTextBox.setObjectName(u"custMapFileTextBox")
        sizePolicy.setHeightForWidth(self.custMapFileTextBox.sizePolicy().hasHeightForWidth())
        self.custMapFileTextBox.setSizePolicy(sizePolicy)
        self.custMapFileTextBox.setMinimumSize(QSize(185, 23))
        self.custMapFileTextBox.setMaximumSize(QSize(185, 23))
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        font1.setPointSize(11)
        self.custMapFileTextBox.setFont(font1)
        self.custMapFileTextBox.setStyleSheet(u"#custMapFileTextBox{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#custMapFileTextBox:focus{\n"
"}")
        self.custMapFileTextBox.setMaxLength(250)
        self.custMapFileTextBox.setAlignment(Qt.AlignCenter)
        self.custMapFileTextBox.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.custMapFileTextBox)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignRight)

        self.frame_3 = QFrame(self.mainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 100, 231, 181))
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.mainMenuBtnCheckBox = QCheckBox(self.frame_3)
        self.mainMenuBtnCheckBox.setObjectName(u"mainMenuBtnCheckBox")
        self.mainMenuBtnCheckBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mainMenuBtnCheckBox.sizePolicy().hasHeightForWidth())
        self.mainMenuBtnCheckBox.setSizePolicy(sizePolicy)
        self.mainMenuBtnCheckBox.setLayoutDirection(Qt.LeftToRight)
        self.mainMenuBtnCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"    \n"
"}")

        self.verticalLayout_3.addWidget(self.mainMenuBtnCheckBox, 0, Qt.AlignLeft)

        self.custBtnNameTextBox = QLineEdit(self.frame_3)
        self.custBtnNameTextBox.setObjectName(u"custBtnNameTextBox")
        self.custBtnNameTextBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.custBtnNameTextBox.sizePolicy().hasHeightForWidth())
        self.custBtnNameTextBox.setSizePolicy(sizePolicy)
        self.custBtnNameTextBox.setMinimumSize(QSize(185, 23))
        self.custBtnNameTextBox.setMaximumSize(QSize(16777215, 23))
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(11)
        font2.setStrikeOut(False)
        self.custBtnNameTextBox.setFont(font2)
        self.custBtnNameTextBox.setAcceptDrops(False)
        self.custBtnNameTextBox.setStyleSheet(u"#custBtnNameTextBox{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#mapnameTextBox_4:focus{\n"
"}")
        self.custBtnNameTextBox.setMaxLength(250)
        self.custBtnNameTextBox.setAlignment(Qt.AlignCenter)
        self.custBtnNameTextBox.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.custBtnNameTextBox, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainMenuMaterial = QLineEdit(self.frame_4)
        self.mainMenuMaterial.setObjectName(u"mainMenuMaterial")
        self.mainMenuMaterial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mainMenuMaterial.sizePolicy().hasHeightForWidth())
        self.mainMenuMaterial.setSizePolicy(sizePolicy)
        self.mainMenuMaterial.setMinimumSize(QSize(185, 23))
        self.mainMenuMaterial.setMaximumSize(QSize(185, 23))
        font3 = QFont()
        font3.setFamilies([u"Georgia"])
        font3.setPointSize(9)
        font3.setStrikeOut(False)
        self.mainMenuMaterial.setFont(font3)
        self.mainMenuMaterial.setStyleSheet(u"#mainMenuMaterial{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#mainMenuMaterial:focus{\n"
"}")
        self.mainMenuMaterial.setMaxLength(250)
        self.mainMenuMaterial.setAlignment(Qt.AlignCenter)
        self.mainMenuMaterial.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.mainMenuMaterial)

        self.toolButton_2 = QToolButton(self.frame_4)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setEnabled(True)
        self.toolButton_2.setMinimumSize(QSize(0, 21))
        self.toolButton_2.setMaximumSize(QSize(16777215, 21))
        font4 = QFont()
        font4.setStrikeOut(False)
        self.toolButton_2.setFont(font4)
        self.toolButton_2.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_3.addWidget(self.toolButton_2)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pauseScreenMaterial = QLineEdit(self.frame_6)
        self.pauseScreenMaterial.setObjectName(u"pauseScreenMaterial")
        self.pauseScreenMaterial.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pauseScreenMaterial.sizePolicy().hasHeightForWidth())
        self.pauseScreenMaterial.setSizePolicy(sizePolicy)
        self.pauseScreenMaterial.setMinimumSize(QSize(185, 23))
        self.pauseScreenMaterial.setMaximumSize(QSize(185, 23))
        self.pauseScreenMaterial.setFont(font3)
        self.pauseScreenMaterial.setToolTipDuration(-1)
        self.pauseScreenMaterial.setStyleSheet(u"#pauseScreenMaterial{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#pauseScreenMaterial:focus{\n"
"}")
        self.pauseScreenMaterial.setMaxLength(250)
        self.pauseScreenMaterial.setAlignment(Qt.AlignCenter)
        self.pauseScreenMaterial.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.pauseScreenMaterial)

        self.toolButton_3 = QToolButton(self.frame_6)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setEnabled(True)
        self.toolButton_3.setMinimumSize(QSize(0, 21))
        self.toolButton_3.setMaximumSize(QSize(16777215, 21))
        self.toolButton_3.setFont(font4)
        self.toolButton_3.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_5.addWidget(self.toolButton_3)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.loadScreenImage = QLineEdit(self.frame_5)
        self.loadScreenImage.setObjectName(u"loadScreenImage")
        self.loadScreenImage.setEnabled(True)
        sizePolicy.setHeightForWidth(self.loadScreenImage.sizePolicy().hasHeightForWidth())
        self.loadScreenImage.setSizePolicy(sizePolicy)
        self.loadScreenImage.setMinimumSize(QSize(185, 23))
        self.loadScreenImage.setMaximumSize(QSize(185, 23))
        self.loadScreenImage.setFont(font3)
        self.loadScreenImage.setStyleSheet(u"#loadScreenImage{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#loadScreenImage:focus{\n"
"}")
        self.loadScreenImage.setMaxLength(250)
        self.loadScreenImage.setAlignment(Qt.AlignCenter)
        self.loadScreenImage.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.loadScreenImage)

        self.toolButton_4 = QToolButton(self.frame_5)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setEnabled(True)
        self.toolButton_4.setMinimumSize(QSize(0, 21))
        self.toolButton_4.setMaximumSize(QSize(16777215, 21))
        self.toolButton_4.setFont(font4)
        self.toolButton_4.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_4.addWidget(self.toolButton_4)


        self.verticalLayout_3.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.missionScreenImage = QLineEdit(self.frame_10)
        self.missionScreenImage.setObjectName(u"missionScreenImage")
        self.missionScreenImage.setEnabled(True)
        sizePolicy.setHeightForWidth(self.missionScreenImage.sizePolicy().hasHeightForWidth())
        self.missionScreenImage.setSizePolicy(sizePolicy)
        self.missionScreenImage.setMinimumSize(QSize(185, 23))
        self.missionScreenImage.setMaximumSize(QSize(185, 23))
        self.missionScreenImage.setFont(font3)
        self.missionScreenImage.setStyleSheet(u"#missionScreenImage{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#missionScreenImage:focus{\n"
"}")
        self.missionScreenImage.setMaxLength(250)
        self.missionScreenImage.setAlignment(Qt.AlignCenter)
        self.missionScreenImage.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.missionScreenImage)

        self.toolButton_6 = QToolButton(self.frame_10)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(True)
        self.toolButton_6.setMinimumSize(QSize(0, 21))
        self.toolButton_6.setMaximumSize(QSize(16777215, 21))
        self.toolButton_6.setFont(font4)
        self.toolButton_6.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_8.addWidget(self.toolButton_6)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.frame_8 = QFrame(self.mainFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 10, 231, 81))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"	border: 2px solid #03e3fc;\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 6)
        self.mapnameTextBox = QLineEdit(self.frame_8)
        self.mapnameTextBox.setObjectName(u"mapnameTextBox")
        sizePolicy1.setHeightForWidth(self.mapnameTextBox.sizePolicy().hasHeightForWidth())
        self.mapnameTextBox.setSizePolicy(sizePolicy1)
        self.mapnameTextBox.setMinimumSize(QSize(0, 26))
        self.mapnameTextBox.setMaximumSize(QSize(16777215, 16777215))
        self.mapnameTextBox.setFont(font1)
        self.mapnameTextBox.setAcceptDrops(False)
        self.mapnameTextBox.setStyleSheet(u"#mapnameTextBox{\n"
"	color: black;\n"
"	background-color: #03e3fc;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#mapnameTextBox_4:focus{\n"
"}")
        self.mapnameTextBox.setMaxLength(250)
        self.mapnameTextBox.setAlignment(Qt.AlignCenter)
        self.mapnameTextBox.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.mapnameTextBox)

        self.createMapbtn = QPushButton(self.frame_8)
        self.createMapbtn.setObjectName(u"createMapbtn")
        sizePolicy1.setHeightForWidth(self.createMapbtn.sizePolicy().hasHeightForWidth())
        self.createMapbtn.setSizePolicy(sizePolicy1)
        self.createMapbtn.setMinimumSize(QSize(0, 31))
        self.createMapbtn.setMaximumSize(QSize(16777215, 31))
        font5 = QFont()
        font5.setFamilies([u"Georgia"])
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.createMapbtn.setFont(font5)
        self.createMapbtn.setStyleSheet(u"#createMapbtn{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #03e3fc;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#createMapbtn:pressed{\n"
"	background: #ff47ff;\n"
"}\n"
"\n"
"#createMapbtn:hover{\n"
"	border: 2px solid rgb(85,170,255);\n"
"}")

        self.verticalLayout_5.addWidget(self.createMapbtn)

        self.frame_11 = QFrame(self.mainFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(250, 10, 141, 121))
        self.frame_11.setLayoutDirection(Qt.LeftToRight)
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 4px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.prototypeMap = QRadioButton(self.frame_11)
        self.prototypeMap.setObjectName(u"prototypeMap")
        sizePolicy.setHeightForWidth(self.prototypeMap.sizePolicy().hasHeightForWidth())
        self.prototypeMap.setSizePolicy(sizePolicy)
        self.prototypeMap.setLayoutDirection(Qt.LeftToRight)
        self.prototypeMap.setAutoFillBackground(False)
        self.prototypeMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.prototypeMap.setCheckable(True)
        self.prototypeMap.setChecked(True)

        self.verticalLayout_8.addWidget(self.prototypeMap)

        self.asylumMap = QRadioButton(self.frame_11)
        self.asylumMap.setObjectName(u"asylumMap")
        self.asylumMap.setEnabled(True)
        sizePolicy.setHeightForWidth(self.asylumMap.sizePolicy().hasHeightForWidth())
        self.asylumMap.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Georgia"])
        font6.setStrikeOut(False)
        self.asylumMap.setFont(font6)
        self.asylumMap.setLayoutDirection(Qt.LeftToRight)
        self.asylumMap.setAutoFillBackground(False)
        self.asylumMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.asylumMap.setCheckable(True)
        self.asylumMap.setChecked(False)

        self.verticalLayout_8.addWidget(self.asylumMap)

        self.sumpfMap = QRadioButton(self.frame_11)
        self.sumpfMap.setObjectName(u"sumpfMap")
        self.sumpfMap.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sumpfMap.sizePolicy().hasHeightForWidth())
        self.sumpfMap.setSizePolicy(sizePolicy)
        self.sumpfMap.setFont(font6)
        self.sumpfMap.setLayoutDirection(Qt.LeftToRight)
        self.sumpfMap.setAutoFillBackground(False)
        self.sumpfMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.sumpfMap.setCheckable(True)
        self.sumpfMap.setChecked(False)

        self.verticalLayout_8.addWidget(self.sumpfMap)

        self.factoryMap = QRadioButton(self.frame_11)
        self.factoryMap.setObjectName(u"factoryMap")
        self.factoryMap.setEnabled(True)
        sizePolicy.setHeightForWidth(self.factoryMap.sizePolicy().hasHeightForWidth())
        self.factoryMap.setSizePolicy(sizePolicy)
        self.factoryMap.setFont(font6)
        self.factoryMap.setLayoutDirection(Qt.LeftToRight)
        self.factoryMap.setAutoFillBackground(False)
        self.factoryMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.factoryMap.setCheckable(True)
        self.factoryMap.setChecked(False)

        self.verticalLayout_8.addWidget(self.factoryMap)

        self.line = QFrame(self.frame_11)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(129, 0))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.allInOneMap = QRadioButton(self.frame_11)
        self.allInOneMap.setObjectName(u"allInOneMap")
        sizePolicy.setHeightForWidth(self.allInOneMap.sizePolicy().hasHeightForWidth())
        self.allInOneMap.setSizePolicy(sizePolicy)
        self.allInOneMap.setLayoutDirection(Qt.LeftToRight)
        self.allInOneMap.setAutoFillBackground(False)
        self.allInOneMap.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.allInOneMap.setCheckable(False)
        self.allInOneMap.setChecked(False)

        self.verticalLayout_8.addWidget(self.allInOneMap)

        self.advModeBtn = QPushButton(self.mainFrame)
        self.advModeBtn.setObjectName(u"advModeBtn")
        self.advModeBtn.setEnabled(True)
        self.advModeBtn.setGeometry(QRect(400, 120, 231, 31))
        sizePolicy.setHeightForWidth(self.advModeBtn.sizePolicy().hasHeightForWidth())
        self.advModeBtn.setSizePolicy(sizePolicy)
        self.advModeBtn.setMinimumSize(QSize(217, 31))
        self.advModeBtn.setMaximumSize(QSize(16777215, 16777215))
        self.advModeBtn.setFont(font5)
        self.advModeBtn.setStyleSheet(u"#advModeBtn{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: rgb(0, 255, 0);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#advModeBtn:pressed{\n"
"	background: #ff47ff;\n"
"}\n"
"\n"
"#advModeBtn:hover{\n"
"	border: 2px solid rgb(85,170,255);\n"
"}")
        self.advModeBtn.setCheckable(True)
        self.advModeBtn.setChecked(False)
        self.advModeBtn.setAutoDefault(False)
        self.advModeBtn.setFlat(False)
        self.advancedFrame = QFrame(self.mainFrame)
        self.advancedFrame.setObjectName(u"advancedFrame")
        self.advancedFrame.setGeometry(QRect(10, 290, 621, 161))
        sizePolicy.setHeightForWidth(self.advancedFrame.sizePolicy().hasHeightForWidth())
        self.advancedFrame.setSizePolicy(sizePolicy)
        self.advancedFrame.setStyleSheet(u"#advancedFrame{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.advancedFrame.setFrameShape(QFrame.StyledPanel)
        self.advancedFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.advancedFrame)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.frame_16 = QFrame(self.advancedFrame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(155, 16777215))
        self.frame_16.setStyleSheet(u"#frame_16{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.startWeap = QLineEdit(self.frame_16)
        self.startWeap.setObjectName(u"startWeap")
        sizePolicy.setHeightForWidth(self.startWeap.sizePolicy().hasHeightForWidth())
        self.startWeap.setSizePolicy(sizePolicy)
        self.startWeap.setMinimumSize(QSize(0, 23))
        self.startWeap.setMaximumSize(QSize(16777215, 23))
        self.startWeap.setFont(font1)
        self.startWeap.setStyleSheet(u"#startWeap{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#startWeap:focus{\n"
"}")
        self.startWeap.setMaxLength(250)
        self.startWeap.setAlignment(Qt.AlignCenter)
        self.startWeap.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.startWeap)

        self.switchWeap = QLineEdit(self.frame_16)
        self.switchWeap.setObjectName(u"switchWeap")
        sizePolicy.setHeightForWidth(self.switchWeap.sizePolicy().hasHeightForWidth())
        self.switchWeap.setSizePolicy(sizePolicy)
        self.switchWeap.setMinimumSize(QSize(0, 23))
        self.switchWeap.setMaximumSize(QSize(16777215, 23))
        self.switchWeap.setFont(font1)
        self.switchWeap.setStyleSheet(u"#switchWeap{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#switchWeap:focus{\n"
"}")
        self.switchWeap.setMaxLength(250)
        self.switchWeap.setAlignment(Qt.AlignCenter)
        self.switchWeap.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.switchWeap)

        self.laststandWeap = QLineEdit(self.frame_16)
        self.laststandWeap.setObjectName(u"laststandWeap")
        sizePolicy.setHeightForWidth(self.laststandWeap.sizePolicy().hasHeightForWidth())
        self.laststandWeap.setSizePolicy(sizePolicy)
        self.laststandWeap.setMinimumSize(QSize(0, 23))
        self.laststandWeap.setMaximumSize(QSize(16777215, 23))
        self.laststandWeap.setFont(font1)
        self.laststandWeap.setStyleSheet(u"#laststandWeap{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#laststandWeap:focus{\n"
"}")
        self.laststandWeap.setMaxLength(250)
        self.laststandWeap.setAlignment(Qt.AlignCenter)
        self.laststandWeap.setDragEnabled(False)
        self.laststandWeap.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.laststandWeap)

        self.score = QLineEdit(self.frame_16)
        self.score.setObjectName(u"score")
        sizePolicy.setHeightForWidth(self.score.sizePolicy().hasHeightForWidth())
        self.score.setSizePolicy(sizePolicy)
        self.score.setMinimumSize(QSize(0, 23))
        self.score.setMaximumSize(QSize(16777215, 23))
        self.score.setFont(font1)
        self.score.setStyleSheet(u"#score{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#score:focus{\n"
"}")
        self.score.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.score)


        self.horizontalLayout_12.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.advancedFrame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(190, 16777215))
        self.frame_15.setStyleSheet(u"#frame_15{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.stockBoxSetup = QRadioButton(self.frame_15)
        self.stockBoxSetup.setObjectName(u"stockBoxSetup")
        self.stockBoxSetup.setEnabled(True)
        self.stockBoxSetup.setGeometry(QRect(10, 10, 111, 16))
        sizePolicy.setHeightForWidth(self.stockBoxSetup.sizePolicy().hasHeightForWidth())
        self.stockBoxSetup.setSizePolicy(sizePolicy)
        self.stockBoxSetup.setFont(font6)
        self.stockBoxSetup.setLayoutDirection(Qt.LeftToRight)
        self.stockBoxSetup.setAutoFillBackground(False)
        self.stockBoxSetup.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.stockBoxSetup.setCheckable(True)
        self.stockBoxSetup.setChecked(True)
        self.customBoxSetup = QRadioButton(self.frame_15)
        self.customBoxSetup.setObjectName(u"customBoxSetup")
        self.customBoxSetup.setEnabled(True)
        self.customBoxSetup.setGeometry(QRect(10, 50, 124, 16))
        sizePolicy.setHeightForWidth(self.customBoxSetup.sizePolicy().hasHeightForWidth())
        self.customBoxSetup.setSizePolicy(sizePolicy)
        self.customBoxSetup.setFont(font6)
        self.customBoxSetup.setLayoutDirection(Qt.LeftToRight)
        self.customBoxSetup.setAutoFillBackground(False)
        self.customBoxSetup.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.customBoxSetup.setCheckable(True)
        self.customBoxSetup.setChecked(False)
        self.randBoxSetup = QRadioButton(self.frame_15)
        self.randBoxSetup.setObjectName(u"randBoxSetup")
        self.randBoxSetup.setEnabled(True)
        self.randBoxSetup.setGeometry(QRect(10, 30, 111, 16))
        sizePolicy.setHeightForWidth(self.randBoxSetup.sizePolicy().hasHeightForWidth())
        self.randBoxSetup.setSizePolicy(sizePolicy)
        self.randBoxSetup.setFont(font6)
        self.randBoxSetup.setLayoutDirection(Qt.LeftToRight)
        self.randBoxSetup.setAutoFillBackground(False)
        self.randBoxSetup.setStyleSheet(u"QRadioButton{\n"
"	color: #fff;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QRadioButton:focus{\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"}")
        self.randBoxSetup.setCheckable(True)
        self.randBoxSetup.setChecked(False)
        self.playerViewModel = QLineEdit(self.frame_15)
        self.playerViewModel.setObjectName(u"playerViewModel")
        self.playerViewModel.setEnabled(True)
        self.playerViewModel.setGeometry(QRect(10, 78, 146, 23))
        sizePolicy.setHeightForWidth(self.playerViewModel.sizePolicy().hasHeightForWidth())
        self.playerViewModel.setSizePolicy(sizePolicy)
        self.playerViewModel.setMinimumSize(QSize(0, 23))
        self.playerViewModel.setMaximumSize(QSize(146, 23))
        self.playerViewModel.setFont(font2)
        self.playerViewModel.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.playerViewModel.setMaxLength(250)
        self.playerViewModel.setAlignment(Qt.AlignCenter)
        self.playerViewModel.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.frame_15)

        self.frame_7 = QFrame(self.advancedFrame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 145))
        self.frame_7.setMaximumSize(QSize(285, 16777215))
        self.frame_7.setLayoutDirection(Qt.LeftToRight)
        self.frame_7.setStyleSheet(u"#frame_7{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 6, 0, 6)
        self.enableFogCheckBox = QCheckBox(self.frame_7)
        self.enableFogCheckBox.setObjectName(u"enableFogCheckBox")
        sizePolicy.setHeightForWidth(self.enableFogCheckBox.sizePolicy().hasHeightForWidth())
        self.enableFogCheckBox.setSizePolicy(sizePolicy)
        self.enableFogCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.enableFogCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"    \n"
"}")
        self.enableFogCheckBox.setChecked(True)

        self.verticalLayout_4.addWidget(self.enableFogCheckBox)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.usingCustomVisionFile = QCheckBox(self.frame_13)
        self.usingCustomVisionFile.setObjectName(u"usingCustomVisionFile")
        sizePolicy.setHeightForWidth(self.usingCustomVisionFile.sizePolicy().hasHeightForWidth())
        self.usingCustomVisionFile.setSizePolicy(sizePolicy)
        self.usingCustomVisionFile.setLayoutDirection(Qt.LeftToRight)
        self.usingCustomVisionFile.setStyleSheet(u"QCheckBox{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"    \n"
"}")
        self.usingCustomVisionFile.setChecked(False)

        self.horizontalLayout_10.addWidget(self.usingCustomVisionFile)

        self.toolButton = QToolButton(self.frame_13)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_10.addWidget(self.toolButton)

        self.visionFileTextBox = QLineEdit(self.frame_13)
        self.visionFileTextBox.setObjectName(u"visionFileTextBox")
        sizePolicy.setHeightForWidth(self.visionFileTextBox.sizePolicy().hasHeightForWidth())
        self.visionFileTextBox.setSizePolicy(sizePolicy)
        self.visionFileTextBox.setMinimumSize(QSize(150, 23))
        self.visionFileTextBox.setMaximumSize(QSize(150, 23))
        self.visionFileTextBox.setFont(font1)
        self.visionFileTextBox.setAcceptDrops(False)
        self.visionFileTextBox.setStyleSheet(u"QLineEdit{\n"
"	color:  black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	padding-left: 5px;\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.visionFileTextBox.setMaxLength(250)
        self.visionFileTextBox.setAlignment(Qt.AlignCenter)
        self.visionFileTextBox.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.visionFileTextBox)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.addMiniMapCheckBox = QCheckBox(self.frame_7)
        self.addMiniMapCheckBox.setObjectName(u"addMiniMapCheckBox")
        sizePolicy.setHeightForWidth(self.addMiniMapCheckBox.sizePolicy().hasHeightForWidth())
        self.addMiniMapCheckBox.setSizePolicy(sizePolicy)
        self.addMiniMapCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.addMiniMapCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"    \n"
"}")

        self.verticalLayout_4.addWidget(self.addMiniMapCheckBox)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.toolButton_7 = QToolButton(self.frame_14)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setStyleSheet(u"QToolButton{\n"
"	color: #03e3fc;\n"
"	background-color: #848080;\n"
"	border-radius: 7px;\n"
"	padding: 7px;\n"
"	width: 7px;\n"
"	height: 7px;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"	background: #03e3fc;\n"
"}")

        self.horizontalLayout_11.addWidget(self.toolButton_7)

        self.miniMapTextBox = QLineEdit(self.frame_14)
        self.miniMapTextBox.setObjectName(u"miniMapTextBox")
        sizePolicy.setHeightForWidth(self.miniMapTextBox.sizePolicy().hasHeightForWidth())
        self.miniMapTextBox.setSizePolicy(sizePolicy)
        self.miniMapTextBox.setMinimumSize(QSize(150, 23))
        self.miniMapTextBox.setMaximumSize(QSize(16777215, 23))
        self.miniMapTextBox.setFont(font1)
        self.miniMapTextBox.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"	background-color: #b5b5b5;\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.miniMapTextBox.setMaxLength(250)
        self.miniMapTextBox.setAlignment(Qt.AlignCenter)
        self.miniMapTextBox.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.miniMapTextBox)


        self.verticalLayout_4.addWidget(self.frame_14, 0, Qt.AlignRight)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(220, 19))
        self.frame_9.setMaximumSize(QSize(16777215, 19))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(21)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.FovSlider = QSlider(self.frame_9)
        self.FovSlider.setObjectName(u"FovSlider")
        sizePolicy.setHeightForWidth(self.FovSlider.sizePolicy().hasHeightForWidth())
        self.FovSlider.setSizePolicy(sizePolicy)
        self.FovSlider.setMinimumSize(QSize(150, 19))
        self.FovSlider.setMaximumSize(QSize(140, 19))
        self.FovSlider.setLayoutDirection(Qt.LeftToRight)
        self.FovSlider.setMinimum(60)
        self.FovSlider.setMaximum(120)
        self.FovSlider.setSingleStep(5)
        self.FovSlider.setSliderPosition(65)
        self.FovSlider.setTracking(True)
        self.FovSlider.setOrientation(Qt.Horizontal)
        self.FovSlider.setTickPosition(QSlider.TicksBelow)
        self.FovSlider.setTickInterval(5)

        self.horizontalLayout_6.addWidget(self.FovSlider)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_12.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.mainFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(400, 162, 231, 121))
        self.frame_12.setStyleSheet(u"#frame_12{\n"
"	border: 2px solid #ff020f;\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 6)
        self.removeAppData = QCheckBox(self.frame_12)
        self.removeAppData.setObjectName(u"removeAppData")
        sizePolicy.setHeightForWidth(self.removeAppData.sizePolicy().hasHeightForWidth())
        self.removeAppData.setSizePolicy(sizePolicy)
        self.removeAppData.setLayoutDirection(Qt.RightToLeft)
        self.removeAppData.setStyleSheet(u"QCheckBox{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"}\n"
"\n"
"QCheckBox:focus{\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #03e3fc;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	border: 2px solid rgb(85,170,255);\n"
"    background-color: grey;\n"
"    \n"
"}")

        self.verticalLayout_9.addWidget(self.removeAppData)

        self.deleteMapTextBox = QLineEdit(self.frame_12)
        self.deleteMapTextBox.setObjectName(u"deleteMapTextBox")
        sizePolicy1.setHeightForWidth(self.deleteMapTextBox.sizePolicy().hasHeightForWidth())
        self.deleteMapTextBox.setSizePolicy(sizePolicy1)
        self.deleteMapTextBox.setMinimumSize(QSize(0, 28))
        self.deleteMapTextBox.setMaximumSize(QSize(16777215, 26))
        self.deleteMapTextBox.setFont(font1)
        self.deleteMapTextBox.setStyleSheet(u"#deleteMapTextBox{\n"
"	color: black;\n"
"	background-color: rgba(255, 0, 4, 1);\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 5px;\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#deleteMapTextBox:focus{\n"
"}")
        self.deleteMapTextBox.setMaxLength(250)
        self.deleteMapTextBox.setAlignment(Qt.AlignCenter)
        self.deleteMapTextBox.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.deleteMapTextBox)

        self.deleteMapBtn = QPushButton(self.frame_12)
        self.deleteMapBtn.setObjectName(u"deleteMapBtn")
        sizePolicy1.setHeightForWidth(self.deleteMapBtn.sizePolicy().hasHeightForWidth())
        self.deleteMapBtn.setSizePolicy(sizePolicy1)
        self.deleteMapBtn.setMinimumSize(QSize(0, 20))
        self.deleteMapBtn.setMaximumSize(QSize(16777215, 31))
        self.deleteMapBtn.setFont(font5)
        self.deleteMapBtn.setStyleSheet(u"#deleteMapBtn{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #ff020f;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}\n"
"\n"
"#deleteMapBtn:pressed{\n"
"	background: #ff47ff;\n"
"}\n"
"\n"
"#deleteMapBtn:hover{\n"
"	border: 2px solid rgb(85,170,255);\n"
"}")

        self.verticalLayout_9.addWidget(self.deleteMapBtn)

        self.creditsFrame = QFrame(self.mainFrame)
        self.creditsFrame.setObjectName(u"creditsFrame")
        self.creditsFrame.setGeometry(QRect(250, 140, 141, 141))
        self.creditsFrame.setStyleSheet(u"#creditsFrame{\n"
"	border: 2px solid rgb(168, 175, 217);\n"
"	border-radius: 15px;\n"
"	color: #fff;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")
        self.creditsFrame.setFrameShape(QFrame.StyledPanel)
        self.creditsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.creditsFrame)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 6, 3, 6)
        self.label_2 = QLabel(self.creditsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: #03e3fc;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.creditsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_5 = QLabel(self.creditsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_8 = QLabel(self.creditsFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_6 = QLabel(self.creditsFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.creditsFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_9 = QLabel(self.creditsFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_4 = QLabel(self.creditsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(85,170,255);\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.mainFrame)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy2)
        self.footerFrame.setMinimumSize(QSize(0, 50))
        self.footerFrame.setMaximumSize(QSize(16777215, 50))
        self.footerFrame.setStyleSheet(u"#footerFrame{\n"
"	background: rgb(37,39,48);\n"
"	border-radius: 20px;\n"
"	opacity: 100;\n"
"	border: 2px solid #03e3fc;\n"
"}")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.buildTimeFrame = QFrame(self.footerFrame)
        self.buildTimeFrame.setObjectName(u"buildTimeFrame")
        self.buildTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.buildTimeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.buildTimeFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 6, -1, 6)
        self.buildLabel = QLabel(self.buildTimeFrame)
        self.buildLabel.setObjectName(u"buildLabel")
        sizePolicy.setHeightForWidth(self.buildLabel.sizePolicy().hasHeightForWidth())
        self.buildLabel.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"Georgia"])
        font7.setPointSize(8)
        font7.setBold(True)
        self.buildLabel.setFont(font7)
        self.buildLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_7.addWidget(self.buildLabel)

        self.dateTimeLabel = QLabel(self.buildTimeFrame)
        self.dateTimeLabel.setObjectName(u"dateTimeLabel")
        sizePolicy.setHeightForWidth(self.dateTimeLabel.sizePolicy().hasHeightForWidth())
        self.dateTimeLabel.setSizePolicy(sizePolicy)
        self.dateTimeLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-family: Georgia;\n"
"}")

        self.verticalLayout_7.addWidget(self.dateTimeLabel)


        self.horizontalLayout_9.addWidget(self.buildTimeFrame, 0, Qt.AlignLeft)

        self.discordFrame = QFrame(self.footerFrame)
        self.discordFrame.setObjectName(u"discordFrame")
        self.discordFrame.setFrameShape(QFrame.StyledPanel)
        self.discordFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.discordFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 9, 0)
        self.commandLinkButton = QCommandLinkButton(self.discordFrame)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy1.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy1)
        self.commandLinkButton.setMaximumSize(QSize(120, 35))
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.horizontalLayout_7.addWidget(self.commandLinkButton)

        self.commandLinkButton_2 = QCommandLinkButton(self.discordFrame)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setMaximumSize(QSize(16777215, 35))
        self.commandLinkButton_2.setStyleSheet(u"QCommandLinkButton{\n"
"	color: #fff;\n"
"	background-color: rgb(34,36,44);\n"
"	font-family: Georgia;\n"
"}")

        self.horizontalLayout_7.addWidget(self.commandLinkButton_2)


        self.horizontalLayout_9.addWidget(self.discordFrame)


        self.verticalLayout.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.advModeBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.headerLabel.setText(QCoreApplication.translate("MainWindow", u"CME - WaW Script Placer", None))
#if QT_CONFIG(tooltip)
        self.discordBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Join CME Discord</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.discordBtn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.discordBtn.setText("")
#if QT_CONFIG(shortcut)
        self.discordBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.websiteBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Join CME Website</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.websiteBtn.setText("")
#if QT_CONFIG(shortcut)
        self.websiteBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.youtubeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Join CME YouTube</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.youtubeBtn.setText("")
#if QT_CONFIG(shortcut)
        self.youtubeBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.minimiseBtn.setText("")
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.blankMapRadioBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Will provide a blank template .map file with only worldspawn settings applied.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blankMapRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Blank Map", None))
#if QT_CONFIG(tooltip)
        self.setupMapRadioBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Will provide a simple template .map file with a few things like spawners, window barriers, mystery box, explodable barrels etc to get you going.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.setupMapRadioBtn.setText(QCoreApplication.translate("MainWindow", u"Setup Map", None))
#if QT_CONFIG(tooltip)
        self.customMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">This option allows you to add a pre-existing .map file to this new map.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.customMap.setText(QCoreApplication.translate("MainWindow", u"Custom Map", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.custMapFileTextBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full .map file path.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.custMapFileTextBox.setText("")
        self.custMapFileTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom .map File", None))
#if QT_CONFIG(tooltip)
        self.mainMenuBtnCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Toggle to open the Custom Button text box.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mainMenuBtnCheckBox.setText(QCoreApplication.translate("MainWindow", u"Main Menu Button", None))
#if QT_CONFIG(tooltip)
        self.custBtnNameTextBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Enter a cool &quot;start map&quot; button name.</span></p><p><span style=\" font-size:8pt;\">e.g &quot;Witness Hell!&quot;</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.custBtnNameTextBox.setText("")
        self.custBtnNameTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Button Text", None))
#if QT_CONFIG(tooltip)
        self.mainMenuMaterial.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full material file path.</span></p><p><img src=\":/images/images/mainMenuScreen.png\"/></p><p><span style=\" font-size:8pt;\">#####################################################</span></p><p><span style=\" font-size:8pt;\">Main Menu Screen only requires:</span></p><p><span style=\" font-size:8pt;\">.iwi file to be placed in mods&gt;images folder</span></p><p><span style=\" font-size:8pt;\">To be placed in mod.csv:</span></p><p><span style=\" font-size:8pt;\">// Doesnt need to be a specific material name</span></p><p><span style=\" font-size:8pt;\">// Doesnt need to be precached.</span></p><p><span style=\" font-size:8pt;\">material,material_name</span></p><p><span style=\" font-size:8pt;\">// main.menu calls on bg.inc &amp; no edits made to it.</span></p><p><span style=\" font-size:8pt;\">menufile,ui/main.menu</span></p><p><span style=\" font-size:8pt;\">// we add #include &quot;ui/blurredbg.inc&quot; to bottom of bg.inc</span></p><p><s"
                        "pan style=\" font-size:8pt;\">menufile,ui/bg.inc</span></p><p><span style=\" font-size:8pt;\">// bg.inc calls on blurredbg.inc</span></p><p><span style=\" font-size:8pt;\">menufile,ui/blurredbg.inc</span></p><p><span style=\" font-size:8pt;\">#####################################################</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mainMenuMaterial.setText("")
        self.mainMenuMaterial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Main Menu Screen Material", None))
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.pauseScreenMaterial.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full material file path.<br/></span><img src=\":/images/images/pauseScreenImage.png\"/></p><p><span style=\" font-size:8pt;\">#####################################################</span></p><p><span style=\" font-size:8pt;\">Pause Screen only requires:</span></p><p><span style=\" font-size:8pt;\">Material name to be called: menu_map_mapname</span></p><p><span style=\" font-size:8pt;\">Doesnt need to be precached.</span></p><p><span style=\" font-size:8pt;\">.iwi file to be placed in mods&gt;images folder</span></p><p><span style=\" font-size:8pt;\">To be placed in mod.csv:</span></p><p><span style=\" font-size:8pt;\">material,menu_map_mapname</span></p><p><span style=\" font-size:8pt;\">#####################################################</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pauseScreenMaterial.setText("")
        self.pauseScreenMaterial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pause Screen Material", None))
#if QT_CONFIG(tooltip)
        self.toolButton_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.loadScreenImage.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full material file path.</span></p><p><img src=\":/images/images/loadScreenImage.png\"/></p><p><span style=\" font-size:8pt;\">#####################################################</span></p><p><span style=\" font-size:8pt;\">Load Screen only requires:</span></p><p><span style=\" font-size:8pt;\">Material name to be called: loadscreen_mapname</span></p><p><span style=\" font-size:8pt;\">Doesnt need to be precached.</span></p><p><span style=\" font-size:8pt;\">.iwi file to be placed in mods&gt;images folder</span></p><p><span style=\" font-size:8pt;\">To be placed in mod.csv:</span></p><p><span style=\" font-size:8pt;\">material,loadscreen_mapname</span></p><p><span style=\" font-size:8pt;\">// .map is an empty file</span></p><p><span style=\" font-size:8pt;\">mapname_load.map in map_source folder</span></p><p><span style=\" font-size:8pt;\">mapname.csv in mods&gt;mapname&gt;maps folder</span></p><p><span style=\" font-size:8pt;\">mapname_"
                        "load.csv in zone_source folder</span></p><p><span style=\" font-size:8pt;\">mapname.csv content:</span></p><p><span style=\" font-size:8pt;\">victoryBackdrop,$default</span></p><p><span style=\" font-size:8pt;\">defeatBackdrop,defeat</span></p><p><span style=\" font-size:8pt;\">levelBriefing,loadscreen_CHANGE_TO_MAPNAME</span></p><p><span style=\" font-size:8pt;\">mapname_load.csv content:</span></p><p><span style=\" font-size:8pt;\">ignore,code_post_gfx</span></p><p><span style=\" font-size:8pt;\">ignore,common</span></p><p><span style=\" font-size:8pt;\">ui_map,maps/CHANGE_TO_MAPNAME.csv</span></p><p><span style=\" font-size:8pt;\">#####################################################</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loadScreenImage.setText("")
        self.loadScreenImage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Load Screen Material", None))
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.missionScreenImage.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full material file path.</span></p><p><img src=\":/images/images/missionScreen.png\"/></p><p><span style=\" font-size:8pt;\">#####################################################</span></p><p><span style=\" font-size:8pt;\">Mission Screen only requires:</span></p><p><span style=\" font-size:8pt;\">Material name to be called: mission_screen_mapname</span></p><p><span style=\" font-size:8pt;\">Doesnt need to be precached.</span></p><p><span style=\" font-size:8pt;\">.iwi file to be placed in mods&gt;images folder</span></p><p><span style=\" font-size:8pt;\">To be placed in mod.csv:</span></p><p><span style=\" font-size:8pt;\">stringtable,maps/mapsTable.csv</span></p><p><span style=\" font-size:8pt;\">material,mission_screen_mapname</span></p><p><span style=\" font-size:8pt;\">mapsTable content:</span></p><p><span style=\" font-size:8pt;\"># Map Data Table,,,,,,,</span></p><p><span style=\" font-size:8pt;\">a0,b1,c2,d3,e4,f5,g6,h7,i8,j9</spa"
                        "n></p><p><span style=\" font-size:8pt;\">maxnum_map,20</span></p><p><span style=\" font-size:8pt;\">#mapname,#allies characters,#axis characters,#mapname,#mapimage,#index,#description,#level order coop,#gametype,#mis_01</span></p><p><span style=\" font-size:8pt;\">CHANGE_TO_MAPNAME,desert,desert,CHANGE_TO_MAPNAME,mission_screen_CHANGE_TO_MAPNAME,3,MOD_DESC,21,zom,17</span></p><p><span style=\" font-size:8pt;\">#####################################################</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.missionScreenImage.setText("")
        self.missionScreenImage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mission Screen Material", None))
#if QT_CONFIG(tooltip)
        self.toolButton_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.mapnameTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Mapname", None))
        self.createMapbtn.setText(QCoreApplication.translate("MainWindow", u"Create Map", None))
#if QT_CONFIG(shortcut)
        self.createMapbtn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.prototypeMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Default selection.</span></p><p><span style=\" font-size:8pt;\">Scripts: </span><span style=\" font-size:8pt; font-weight:700;\">nazi_zombie_prototype</span></p><p><span style=\" font-size:8pt;\">Includes the following:</span></p><p><span style=\" font-size:8pt;\">Wall Weapons:</span></p><p><span style=\" font-size:8pt;\">kar98</span></p><p><span style=\" font-size:8pt;\">m1carbine</span></p><p><span style=\" font-size:8pt;\">thompson</span></p><p><span style=\" font-size:8pt;\">double-barrel</span></p><p><span style=\" font-size:8pt;\">bar</span></p><p><span style=\" font-size:8pt;\">trench</span></p><p><span style=\" font-size:8pt;\">double-barrel sawed-off</span></p><p><span style=\" font-size:8pt;\">grenades</span></p><p><span style=\" font-size:8pt;\"><br/>Weapon cabinate with scoped sniper</span></p><p><span style=\" font-size:8pt;\">Mysetry box</span></p><p><br/><span style=\" font-size:8pt;\">Ambient:</span></p><p><span style=\" font-size:8pt;\">Fog"
                        "</span></p><p><span style=\" font-size:8pt;\">Fire</span></p><p><span style=\" font-size:8pt;\">Explodable barrels</span></p><p><span style=\" font-size:8pt;\">Lamps</span></p><p><span style=\" font-size:8pt;\">Lights with spotlight &amp; fx</span></p><p><span style=\" font-size:8pt;\">Broken light sparking fx<br/></span></p><p><span style=\" font-size:8pt;\">Zombie spawners in different rooms activated by purchasing doors</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.prototypeMap.setText(QCoreApplication.translate("MainWindow", u"Nacht der Untoten", None))
#if QT_CONFIG(tooltip)
        self.asylumMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Optional selection.</span></p><p><span style=\" font-size:8pt;\">Scripts: </span><span style=\" font-size:8pt; font-weight:700;\">nazi_zombie_asylum</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.asylumMap.setText(QCoreApplication.translate("MainWindow", u"Zombie Verr\u00fcckt", None))
#if QT_CONFIG(tooltip)
        self.sumpfMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Not available yet.</span></p><p><span style=\" font-size:8pt;\">Optional selection.</span></p><p><span style=\" font-size:8pt;\">Scripts: </span><span style=\" font-size:8pt; font-weight:700;\">nazi_zombie_sumpf</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sumpfMap.setText(QCoreApplication.translate("MainWindow", u"Shi No Numa", None))
#if QT_CONFIG(tooltip)
        self.factoryMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Not available yet.</span></p><p><span style=\" font-size:8pt;\">Optional selection.</span></p><p><span style=\" font-size:8pt;\">Scripts: </span><span style=\" font-size:8pt; font-weight:700;\">nazi_zombie_factory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.factoryMap.setText(QCoreApplication.translate("MainWindow", u"Der Riese", None))
#if QT_CONFIG(tooltip)
        self.allInOneMap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Can't be changed yet.</span></p><p><span style=\" font-size:8pt;\">Default selection.</span></p><p><span style=\" font-size:8pt;\">Scripts: </span><span style=\" font-size:8pt; font-weight:700;\">Stock</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.allInOneMap.setText(QCoreApplication.translate("MainWindow", u"All in one", None))
#if QT_CONFIG(tooltip)
        self.advModeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:400; font-style:normal;\">Note: Not available yet.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.advModeBtn.setText(QCoreApplication.translate("MainWindow", u"Advanced Mode", None))
#if QT_CONFIG(tooltip)
        self.startWeap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Enter the starting weapon you wish to start with.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.startWeap.setText("")
        self.startWeap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Starting Weapon", None))
#if QT_CONFIG(tooltip)
        self.switchWeap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Enter the weapon you wish to automatically switch to upon entering the game.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.switchWeap.setText("")
        self.switchWeap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Switch Weapon", None))
#if QT_CONFIG(tooltip)
        self.laststandWeap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Enter the weapon you wish to use when in laststand.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.laststandWeap.setText("")
        self.laststandWeap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laststand Weapon", None))
#if QT_CONFIG(tooltip)
        self.score.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Enter the starting score(points) you wish to start with.</span></p><p><span style=\" font-size:8pt;\">Note: If left blank it will remain as the default value of 500.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.score.setText("")
        self.score.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Score", None))
#if QT_CONFIG(tooltip)
        self.stockBoxSetup.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">This will give you the weapons that are mentioned in the stock map-specific mapname.gsc file.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stockBoxSetup.setText(QCoreApplication.translate("MainWindow", u"Stock Box Setup", None))
#if QT_CONFIG(tooltip)
        self.customBoxSetup.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">This will allow you to select any/all weapons from the stock map-specific _zombiemode_weapons.gsc file. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.customBoxSetup.setText(QCoreApplication.translate("MainWindow", u"Custom Box Setup", None))
#if QT_CONFIG(tooltip)
        self.randBoxSetup.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">This will give you random weapons.</span></p><p><span style=\" font-size:8pt;\">It will pick a random number between 15-35 and then randomly select that quantity of weapons from the stock map-specific _zombiemode_weapons.gsc file. </span></p><p><span style=\" font-size:8pt;\">WARNING: You could end up with all poor weapons as no weight system is setup yet.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.randBoxSetup.setText(QCoreApplication.translate("MainWindow", u"Rand Box Setup", None))
        self.playerViewModel.setText("")
        self.playerViewModel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Player Viewmodel", None))
#if QT_CONFIG(tooltip)
        self.enableFogCheckBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Enabled by default.</span></p><p><span style=\" font-size:8pt;\">Toggle to disable.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.enableFogCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable Fog?", None))
#if QT_CONFIG(tooltip)
        self.usingCustomVisionFile.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: If enabled, this means that you're using a custom vision file so said file will be copied to your mods folder and the file call will be placed in mod.csv.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.usingCustomVisionFile.setText(QCoreApplication.translate("MainWindow", u"Custom?", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.visionFileTextBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Enter the vision file you wish to use.</span></p><p><span style=\" font-size:8pt;\">Note: Requires the full vision file path.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.visionFileTextBox.setText("")
        self.visionFileTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vision File", None))
        self.addMiniMapCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable Mini Map?", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.miniMapTextBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Requires the full material file path.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.miniMapTextBox.setText("")
        self.miniMapTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mini Map Material", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FOV: 65", None))
#if QT_CONFIG(tooltip)
        self.FovSlider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Select the FOV you want by dragging the slider.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.removeAppData.setText(QCoreApplication.translate("MainWindow", u"Remove AppData?", None))
#if QT_CONFIG(tooltip)
        self.deleteMapTextBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">Note: Enter the mapname you wish to delete.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deleteMapTextBox.setText("")
        self.deleteMapTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Enter Mapname", None))
#if QT_CONFIG(tooltip)
        self.deleteMapBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; font-style:normal;\">Note: Make sure the map you're trying to delete is not selected on the mods launcher on either compile or build tab as this can result in the mods folder being replaced.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deleteMapBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Map", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Credits:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CME Community", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"NAKSHATRA_12", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mythical", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"UGX/SajeOne", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Bunz1102", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sniperbolt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mr Hanky/Jacmac", None))
#if QT_CONFIG(tooltip)
        self.buildLabel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Current version build number</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.buildLabel.setText(QCoreApplication.translate("MainWindow", u"Build Version: 1.0", None))
        self.dateTimeLabel.setText(QCoreApplication.translate("MainWindow", u"date_time", None))
#if QT_CONFIG(tooltip)
        self.commandLinkButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Will load up UGX's discord server.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"UGX Discord", None))
#if QT_CONFIG(tooltip)
        self.commandLinkButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Will load up NAKSHATRA_12's discord server.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"NAKSHATRA_12 Discord", None))
    # retranslateUi

