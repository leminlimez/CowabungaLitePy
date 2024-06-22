# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_CowabungaLite(object):
    def setupUi(self, CowabungaLite):
        if not CowabungaLite.objectName():
            CowabungaLite.setObjectName(u"CowabungaLite")
        CowabungaLite.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CowabungaLite.sizePolicy().hasHeightForWidth())
        CowabungaLite.setSizePolicy(sizePolicy)
        CowabungaLite.setMinimumSize(QSize(1000, 600))
        CowabungaLite.setMaximumSize(QSize(1000, 600))
        CowabungaLite.setStyleSheet(u"QWidget {\n"
"    color: #FFFFFF;\n"
"    background-color: transparent;\n"
"	spacing: 0px;\n"
"}\n"
"\n"
"QWidget:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget [cls=central] {\n"
"    background-color: #1e1e1e;\n"
"	border-radius: 0px;\n"
"	border: 1px solid #4B4B4B;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	min-height: 35px;\n"
"	icon-size: 16px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton[cls=sidebarBtn] {\n"
"    background-color: transparent;\n"
"	icon-size: 24px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #2860ca;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	spacing: 8px;\n"
"	font-size: 14px;\n"
"}\n"
""
                        "\n"
"QLineEdit {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #FFFFFF;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 8px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #3b3b3b;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background: #535353;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page,\n"
"QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background-color: #3b3b3b;\n"
"    height: 4px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #535353;\n"
"    width: 8px;\n"
"    margin: -8px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #3b82f7;\n"
"}\n"
"\n"
"QSl"
                        "ider::tick:horizontal {\n"
"    background-color: #535353;\n"
"    width: 1px;\n"
"}\n"
"")
        self.centralwidget = QWidget(CowabungaLite)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.deviceBar = QWidget(self.centralwidget)
        self.deviceBar.setObjectName(u"deviceBar")
        self.horizontalLayout_4 = QHBoxLayout(self.deviceBar)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_2 = QWidget(self.deviceBar)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_19.setSpacing(1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_3 = QWidget(self.horizontalWidget_2)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.toolButton_6 = QToolButton(self.horizontalWidget_3)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)
        self.toolButton_6.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/phone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_6.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.toolButton_6)

        self.devicePicker = QComboBox(self.horizontalWidget_3)
        self.devicePicker.setObjectName(u"devicePicker")
        self.devicePicker.setStyleSheet(u"#devicePicker {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"    min-height: 38px;\n"
"	min-width: 35px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"	min-height: 38px;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"#devicePicker QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.devicePicker.setDuplicatesEnabled(True)

        self.horizontalLayout_15.addWidget(self.devicePicker)


        self.horizontalLayout_19.addWidget(self.horizontalWidget_3)

        self.refreshBtn = QToolButton(self.horizontalWidget_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/arrow-clockwise.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshBtn.setIcon(icon1)
        self.refreshBtn.setCheckable(False)
        self.refreshBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_19.addWidget(self.refreshBtn)


        self.horizontalLayout_4.addWidget(self.horizontalWidget_2)

        self.titleBar = QToolButton(self.deviceBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy2)
        self.titleBar.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.titleBar)


        self.verticalLayout_11.addWidget(self.deviceBar)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_18 = QHBoxLayout(self.body)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.body)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy3)
        self.sidebar.setMinimumSize(QSize(300, 0))
        self.sidebar.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 0)
        self.homePageBtn = QToolButton(self.sidebar)
        self.homePageBtn.setObjectName(u"homePageBtn")
        sizePolicy2.setHeightForWidth(self.homePageBtn.sizePolicy().hasHeightForWidth())
        self.homePageBtn.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/house.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homePageBtn.setIcon(icon2)
        self.homePageBtn.setCheckable(True)
        self.homePageBtn.setChecked(True)
        self.homePageBtn.setAutoExclusive(True)
        self.homePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.homePageBtn)

        self.explorePageBtn = QToolButton(self.sidebar)
        self.explorePageBtn.setObjectName(u"explorePageBtn")
        sizePolicy2.setHeightForWidth(self.explorePageBtn.sizePolicy().hasHeightForWidth())
        self.explorePageBtn.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/compass.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.explorePageBtn.setIcon(icon3)
        self.explorePageBtn.setCheckable(True)
        self.explorePageBtn.setAutoExclusive(True)
        self.explorePageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.explorePageBtn)

        self.locSimPageBtn = QToolButton(self.sidebar)
        self.locSimPageBtn.setObjectName(u"locSimPageBtn")
        sizePolicy2.setHeightForWidth(self.locSimPageBtn.sizePolicy().hasHeightForWidth())
        self.locSimPageBtn.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/geo-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.locSimPageBtn.setIcon(icon4)
        self.locSimPageBtn.setCheckable(True)
        self.locSimPageBtn.setAutoExclusive(True)
        self.locSimPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.locSimPageBtn)

        self.sidebarDiv1 = QFrame(self.sidebar)
        self.sidebarDiv1.setObjectName(u"sidebarDiv1")
        self.sidebarDiv1.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv1.setFrameShadow(QFrame.Plain)
        self.sidebarDiv1.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv1)

        self.customOperationsPageBtn = QToolButton(self.sidebar)
        self.customOperationsPageBtn.setObjectName(u"customOperationsPageBtn")
        sizePolicy2.setHeightForWidth(self.customOperationsPageBtn.sizePolicy().hasHeightForWidth())
        self.customOperationsPageBtn.setSizePolicy(sizePolicy2)
        icon5 = QIcon()
        icon5.addFile(u":/icon/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.customOperationsPageBtn.setIcon(icon5)
        self.customOperationsPageBtn.setCheckable(True)
        self.customOperationsPageBtn.setAutoExclusive(True)
        self.customOperationsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.customOperationsPageBtn)

        self.themesPageBtn = QToolButton(self.sidebar)
        self.themesPageBtn.setObjectName(u"themesPageBtn")
        sizePolicy2.setHeightForWidth(self.themesPageBtn.sizePolicy().hasHeightForWidth())
        self.themesPageBtn.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/brush.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.themesPageBtn.setIcon(icon6)
        self.themesPageBtn.setCheckable(True)
        self.themesPageBtn.setAutoExclusive(True)
        self.themesPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.themesPageBtn.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.themesPageBtn)

        self.statusBarPageBtn = QToolButton(self.sidebar)
        self.statusBarPageBtn.setObjectName(u"statusBarPageBtn")
        sizePolicy2.setHeightForWidth(self.statusBarPageBtn.sizePolicy().hasHeightForWidth())
        self.statusBarPageBtn.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/icon/wifi.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.statusBarPageBtn.setIcon(icon7)
        self.statusBarPageBtn.setCheckable(True)
        self.statusBarPageBtn.setAutoExclusive(True)
        self.statusBarPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.statusBarPageBtn)

        self.springboardOptionsPageBtn = QToolButton(self.sidebar)
        self.springboardOptionsPageBtn.setObjectName(u"springboardOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.springboardOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.springboardOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icon/app-indicator.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.springboardOptionsPageBtn.setIcon(icon8)
        self.springboardOptionsPageBtn.setCheckable(True)
        self.springboardOptionsPageBtn.setAutoExclusive(True)
        self.springboardOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.springboardOptionsPageBtn)

        self.internalOptionsPageBtn = QToolButton(self.sidebar)
        self.internalOptionsPageBtn.setObjectName(u"internalOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.internalOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.internalOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/icon/hdd.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.internalOptionsPageBtn.setIcon(icon9)
        self.internalOptionsPageBtn.setCheckable(True)
        self.internalOptionsPageBtn.setAutoExclusive(True)
        self.internalOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.internalOptionsPageBtn)

        self.setupOptionsPageBtn = QToolButton(self.sidebar)
        self.setupOptionsPageBtn.setObjectName(u"setupOptionsPageBtn")
        sizePolicy2.setHeightForWidth(self.setupOptionsPageBtn.sizePolicy().hasHeightForWidth())
        self.setupOptionsPageBtn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/icon/gear.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setupOptionsPageBtn.setIcon(icon10)
        self.setupOptionsPageBtn.setCheckable(True)
        self.setupOptionsPageBtn.setAutoExclusive(True)
        self.setupOptionsPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.setupOptionsPageBtn)

        self.sidebarDiv2 = QFrame(self.sidebar)
        self.sidebarDiv2.setObjectName(u"sidebarDiv2")
        self.sidebarDiv2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.sidebarDiv2.setFrameShadow(QFrame.Plain)
        self.sidebarDiv2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.sidebarDiv2)

        self.applyPageBtn = QToolButton(self.sidebar)
        self.applyPageBtn.setObjectName(u"applyPageBtn")
        sizePolicy2.setHeightForWidth(self.applyPageBtn.sizePolicy().hasHeightForWidth())
        self.applyPageBtn.setSizePolicy(sizePolicy2)
        icon11 = QIcon()
        icon11.addFile(u":/icon/check-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.applyPageBtn.setIcon(icon11)
        self.applyPageBtn.setCheckable(True)
        self.applyPageBtn.setAutoExclusive(True)
        self.applyPageBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.applyPageBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_18.addWidget(self.sidebar)

        self.main = QWidget(self.body)
        self.main.setObjectName(u"main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy4)
        self._3 = QVBoxLayout(self.main)
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(9, 0, 0, 0)
        self.pages = QStackedWidget(self.main)
        self.pages.setObjectName(u"pages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_2 = QVBoxLayout(self.homePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.homePage)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.toolButton_9 = QToolButton(self.horizontalWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setEnabled(False)
        self.toolButton_9.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_9.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_9)

        self.verticalWidget = QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.phoneNameLbl = QLabel(self.verticalWidget)
        self.phoneNameLbl.setObjectName(u"phoneNameLbl")
        font = QFont()
        font.setBold(False)
        self.phoneNameLbl.setFont(font)

        self.verticalLayout_3.addWidget(self.phoneNameLbl)

        self.phoneVersionLbl = QLabel(self.verticalWidget)
        self.phoneVersionLbl.setObjectName(u"phoneVersionLbl")
        self.phoneVersionLbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.phoneVersionLbl.setTextFormat(Qt.RichText)
        self.phoneVersionLbl.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.phoneVersionLbl)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.line_4 = QFrame(self.homePage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalWidget1 = QWidget(self.homePage)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_27.setSpacing(50)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.bigMilkBtn = QToolButton(self.horizontalWidget1)
        self.bigMilkBtn.setObjectName(u"bigMilkBtn")
        self.bigMilkBtn.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"	padding: 0px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/cowliteicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bigMilkBtn.setIcon(icon12)
        self.bigMilkBtn.setIconSize(QSize(120, 200))

        self.horizontalLayout_27.addWidget(self.bigMilkBtn)

        self.verticalWidget1 = QWidget(self.horizontalWidget1)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_26 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_11)

        self.label_2 = QLabel(self.verticalWidget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"}")

        self.verticalLayout_26.addWidget(self.label_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_12)

        self.patreonBtn = QToolButton(self.verticalWidget1)
        self.patreonBtn.setObjectName(u"patreonBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icon/star.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.patreonBtn.setIcon(icon13)
        self.patreonBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_26.addWidget(self.patreonBtn)

        self.discordBtn = QToolButton(self.verticalWidget1)
        self.discordBtn.setObjectName(u"discordBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icon/discord.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.discordBtn.setIcon(icon14)
        self.discordBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_26.addWidget(self.discordBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)


        self.horizontalLayout_27.addWidget(self.verticalWidget1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.horizontalWidget1)

        self.verticalWidget_2 = QWidget(self.homePage)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_25.setSpacing(15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 30, 0, 30)
        self.horizontalWidget2 = QWidget(self.verticalWidget_2)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.leminBtn = QToolButton(self.horizontalWidget2)
        self.leminBtn.setObjectName(u"leminBtn")
        self.leminBtn.setEnabled(True)
        self.leminBtn.setMinimumSize(QSize(150, 35))
        self.leminBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/credits/LeminLimez.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminBtn.setIcon(icon15)
        self.leminBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.leminBtn)

        self.leminGitHubBtn = QToolButton(self.horizontalWidget2)
        self.leminGitHubBtn.setObjectName(u"leminGitHubBtn")
        self.leminGitHubBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icon/github.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminGitHubBtn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.leminGitHubBtn)

        self.leminTwitterBtn = QToolButton(self.horizontalWidget2)
        self.leminTwitterBtn.setObjectName(u"leminTwitterBtn")
        self.leminTwitterBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icon/twitter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminTwitterBtn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.leminTwitterBtn)

        self.leminKoFiBtn = QToolButton(self.horizontalWidget2)
        self.leminKoFiBtn.setObjectName(u"leminKoFiBtn")
        self.leminKoFiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icon/currency-dollar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.leminKoFiBtn.setIcon(icon18)

        self.horizontalLayout_6.addWidget(self.leminKoFiBtn)

        self.toolButton_14 = QToolButton(self.horizontalWidget2)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy2)
        self.toolButton_14.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.toolButton_14)


        self.verticalLayout_25.addWidget(self.horizontalWidget2)

        self.horizontalWidget_21 = QWidget(self.verticalWidget_2)
        self.horizontalWidget_21.setObjectName(u"horizontalWidget_21")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.avangelistaBtn = QToolButton(self.horizontalWidget_21)
        self.avangelistaBtn.setObjectName(u"avangelistaBtn")
        self.avangelistaBtn.setEnabled(True)
        self.avangelistaBtn.setMinimumSize(QSize(150, 35))
        self.avangelistaBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/credits/Avangelista.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.avangelistaBtn.setIcon(icon19)
        self.avangelistaBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.avangelistaBtn)

        self.avangelistaGitHubBtn = QToolButton(self.horizontalWidget_21)
        self.avangelistaGitHubBtn.setObjectName(u"avangelistaGitHubBtn")
        self.avangelistaGitHubBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        self.avangelistaGitHubBtn.setIcon(icon16)

        self.horizontalLayout_2.addWidget(self.avangelistaGitHubBtn)

        self.avangelistaTwitterBtn = QToolButton(self.horizontalWidget_21)
        self.avangelistaTwitterBtn.setObjectName(u"avangelistaTwitterBtn")
        self.avangelistaTwitterBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        self.avangelistaTwitterBtn.setIcon(icon17)

        self.horizontalLayout_2.addWidget(self.avangelistaTwitterBtn)

        self.avangelistaKoFiBtn = QToolButton(self.horizontalWidget_21)
        self.avangelistaKoFiBtn.setObjectName(u"avangelistaKoFiBtn")
        self.avangelistaKoFiBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")
        self.avangelistaKoFiBtn.setIcon(icon18)

        self.horizontalLayout_2.addWidget(self.avangelistaKoFiBtn)

        self.toolButton_5 = QToolButton(self.horizontalWidget_21)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy2)
        self.toolButton_5.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.toolButton_5)


        self.verticalLayout_25.addWidget(self.horizontalWidget_21)

        self.horizontalWidget3 = QWidget(self.verticalWidget_2)
        self.horizontalWidget3.setObjectName(u"horizontalWidget3")
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.toolButton_15 = QToolButton(self.horizontalWidget3)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setEnabled(False)
        self.toolButton_15.setMinimumSize(QSize(150, 35))
        self.toolButton_15.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.toolButton_15)

        self.iTechBtn = QToolButton(self.horizontalWidget3)
        self.iTechBtn.setObjectName(u"iTechBtn")
        sizePolicy2.setHeightForWidth(self.iTechBtn.sizePolicy().hasHeightForWidth())
        self.iTechBtn.setSizePolicy(sizePolicy2)
        self.iTechBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.iTechBtn)

        self.libiBtn = QToolButton(self.horizontalWidget3)
        self.libiBtn.setObjectName(u"libiBtn")
        sizePolicy2.setHeightForWidth(self.libiBtn.sizePolicy().hasHeightForWidth())
        self.libiBtn.setSizePolicy(sizePolicy2)
        self.libiBtn.setStyleSheet(u"QToolButton {\n"
"	border-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.libiBtn)

        self.qtBtn = QToolButton(self.horizontalWidget3)
        self.qtBtn.setObjectName(u"qtBtn")
        sizePolicy2.setHeightForWidth(self.qtBtn.sizePolicy().hasHeightForWidth())
        self.qtBtn.setSizePolicy(sizePolicy2)
        self.qtBtn.setStyleSheet(u"QToolButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	background: none;\n"
"	border: 1px solid #3b3b3b;\n"
"	border-left: none;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_24.addWidget(self.qtBtn)


        self.verticalLayout_25.addWidget(self.horizontalWidget3)


        self.verticalLayout_2.addWidget(self.verticalWidget_2)

        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.homePage)
        self.explorePage = QWidget()
        self.explorePage.setObjectName(u"explorePage")
        self.verticalLayout_31 = QVBoxLayout(self.explorePage)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.explorePageHeader = QWidget(self.explorePage)
        self.explorePageHeader.setObjectName(u"explorePageHeader")
        self.horizontalLayout_31 = QHBoxLayout(self.explorePageHeader)
        self.horizontalLayout_31.setSpacing(10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, -1, 0, -1)
        self.toolButton_16 = QToolButton(self.explorePageHeader)
        self.toolButton_16.setObjectName(u"toolButton_16")
        self.toolButton_16.setEnabled(False)
        self.toolButton_16.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_16.setIcon(icon3)

        self.horizontalLayout_31.addWidget(self.toolButton_16)

        self.verticalWidget_9 = QWidget(self.explorePageHeader)
        self.verticalWidget_9.setObjectName(u"verticalWidget_9")
        self.verticalLayout_30 = QVBoxLayout(self.verticalWidget_9)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.exploreLbl = QLabel(self.verticalWidget_9)
        self.exploreLbl.setObjectName(u"exploreLbl")
        self.exploreLbl.setFont(font)

        self.verticalLayout_30.addWidget(self.exploreLbl)

        self.exploreSubLbl = QLabel(self.verticalWidget_9)
        self.exploreSubLbl.setObjectName(u"exploreSubLbl")

        self.verticalLayout_30.addWidget(self.exploreSubLbl)


        self.horizontalLayout_31.addWidget(self.verticalWidget_9)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_13)


        self.verticalLayout_31.addWidget(self.explorePageHeader)

        self.line_3 = QFrame(self.explorePage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_31.addWidget(self.line_3)

        self.exploreThemesCnt = QWidget(self.explorePage)
        self.exploreThemesCnt.setObjectName(u"exploreThemesCnt")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.exploreThemesCnt.sizePolicy().hasHeightForWidth())
        self.exploreThemesCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_31.addWidget(self.exploreThemesCnt)

        self.pages.addWidget(self.explorePage)
        self.locSimPage = QWidget()
        self.locSimPage.setObjectName(u"locSimPage")
        self.verticalLayout_28 = QVBoxLayout(self.locSimPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader = QWidget(self.locSimPage)
        self.locSimPageHeader.setObjectName(u"locSimPageHeader")
        self.horizontalLayout_28 = QHBoxLayout(self.locSimPageHeader)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, 0, -1)
        self.toolButton_13 = QToolButton(self.locSimPageHeader)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setEnabled(False)
        self.toolButton_13.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_13.setIcon(icon4)

        self.horizontalLayout_28.addWidget(self.toolButton_13)

        self.verticalWidget_8 = QWidget(self.locSimPageHeader)
        self.verticalWidget_8.setObjectName(u"verticalWidget_8")
        self.verticalLayout_27 = QVBoxLayout(self.verticalWidget_8)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_2 = QLabel(self.verticalWidget_8)
        self.statusBarLbl_2.setObjectName(u"statusBarLbl_2")
        self.statusBarLbl_2.setFont(font)

        self.verticalLayout_27.addWidget(self.statusBarLbl_2)

        self.label_4 = QLabel(self.verticalWidget_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_27.addWidget(self.label_4)


        self.horizontalLayout_28.addWidget(self.verticalWidget_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_11)

        self.loadLocSimBtn = QToolButton(self.locSimPageHeader)
        self.loadLocSimBtn.setObjectName(u"loadLocSimBtn")

        self.horizontalLayout_28.addWidget(self.loadLocSimBtn)


        self.verticalLayout_28.addWidget(self.locSimPageHeader)

        self.line_2 = QFrame(self.locSimPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_28.addWidget(self.line_2)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_14)

        self.locSimCnt = QWidget(self.locSimPage)
        self.locSimCnt.setObjectName(u"locSimCnt")
        self.locSimPageContent = QVBoxLayout(self.locSimCnt)
        self.locSimPageContent.setObjectName(u"locSimPageContent")
        self.locSimPageContent.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget2 = QWidget(self.locSimCnt)
        self.verticalWidget2.setObjectName(u"verticalWidget2")
        self.verticalLayout_29 = QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_7)

        self.latitudeTxt = QLineEdit(self.verticalWidget2)
        self.latitudeTxt.setObjectName(u"latitudeTxt")
        self.latitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.latitudeTxt)

        self.label_11 = QLabel(self.verticalWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_11)

        self.longitudeTxt = QLineEdit(self.verticalWidget2)
        self.longitudeTxt.setObjectName(u"longitudeTxt")
        self.longitudeTxt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.longitudeTxt)

        self.horizontalWidget4 = QWidget(self.verticalWidget2)
        self.horizontalWidget4.setObjectName(u"horizontalWidget4")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.setLocationBtn = QToolButton(self.horizontalWidget4)
        self.setLocationBtn.setObjectName(u"setLocationBtn")

        self.horizontalLayout_3.addWidget(self.setLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget4)

        self.horizontalWidget_22 = QWidget(self.verticalWidget2)
        self.horizontalWidget_22.setObjectName(u"horizontalWidget_22")
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalWidget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.resetLocationBtn = QToolButton(self.horizontalWidget_22)
        self.resetLocationBtn.setObjectName(u"resetLocationBtn")

        self.horizontalLayout_29.addWidget(self.resetLocationBtn)


        self.verticalLayout_29.addWidget(self.horizontalWidget_22)


        self.locSimPageContent.addWidget(self.verticalWidget2)


        self.verticalLayout_28.addWidget(self.locSimCnt)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_13)

        self.pages.addWidget(self.locSimPage)
        self.themesPage = QWidget()
        self.themesPage.setObjectName(u"themesPage")
        self.verticalLayout_23 = QVBoxLayout(self.themesPage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_8 = QWidget(self.themesPage)
        self.horizontalWidget_8.setObjectName(u"horizontalWidget_8")
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 9, 0, 9)
        self.themesBtn = QToolButton(self.horizontalWidget_8)
        self.themesBtn.setObjectName(u"themesBtn")
        self.themesBtn.setEnabled(True)
        self.themesBtn.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.themesBtn.setIcon(icon6)

        self.horizontalLayout_23.addWidget(self.themesBtn)

        self.verticalWidget_7 = QWidget(self.horizontalWidget_8)
        self.verticalWidget_7.setObjectName(u"verticalWidget_7")
        self.verticalLayout_21 = QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.themesLbl = QLabel(self.verticalWidget_7)
        self.themesLbl.setObjectName(u"themesLbl")
        self.themesLbl.setFont(font)

        self.verticalLayout_21.addWidget(self.themesLbl)

        self.themesEnabledChk = QCheckBox(self.verticalWidget_7)
        self.themesEnabledChk.setObjectName(u"themesEnabledChk")

        self.verticalLayout_21.addWidget(self.themesEnabledChk)


        self.horizontalLayout_23.addWidget(self.verticalWidget_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)

        self.horizontalWidget5 = QWidget(self.horizontalWidget_8)
        self.horizontalWidget5.setObjectName(u"horizontalWidget5")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.importThemeBtn = QToolButton(self.horizontalWidget5)
        self.importThemeBtn.setObjectName(u"importThemeBtn")
        self.importThemeBtn.setEnabled(False)
        self.importThemeBtn.setStyleSheet(u"QToolButton {\n"
"	background: none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.importThemeBtn)

        self.importThemeFolderBtn = QToolButton(self.horizontalWidget5)
        self.importThemeFolderBtn.setObjectName(u"importThemeFolderBtn")
        icon20 = QIcon()
        icon20.addFile(u":/icon/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importThemeFolderBtn.setIcon(icon20)

        self.horizontalLayout_26.addWidget(self.importThemeFolderBtn)

        self.importThemeZipBtn = QToolButton(self.horizontalWidget5)
        self.importThemeZipBtn.setObjectName(u"importThemeZipBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icon/file-earmark-zip.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importThemeZipBtn.setIcon(icon21)

        self.horizontalLayout_26.addWidget(self.importThemeZipBtn)


        self.horizontalLayout_23.addWidget(self.horizontalWidget5)


        self.verticalLayout_23.addWidget(self.horizontalWidget_8)

        self.line_15 = QFrame(self.themesPage)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_23.addWidget(self.line_15)

        self.themesPageContent = QWidget(self.themesPage)
        self.themesPageContent.setObjectName(u"themesPageContent")
        self.themesPageContent.setEnabled(False)
        self.verticalLayout_22 = QVBoxLayout(self.themesPageContent)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.themesCnt = QWidget(self.themesPageContent)
        self.themesCnt.setObjectName(u"themesCnt")

        self.verticalLayout_22.addWidget(self.themesCnt)

        self.line = QFrame(self.themesPageContent)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_22.addWidget(self.line)

        self.label_3 = QLabel(self.themesPageContent)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_22.addWidget(self.label_3)

        self.iconsCnt = QWidget(self.themesPageContent)
        self.iconsCnt.setObjectName(u"iconsCnt")

        self.verticalLayout_22.addWidget(self.iconsCnt)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.horizontalWidget6 = QWidget(self.themesPageContent)
        self.horizontalWidget6.setObjectName(u"horizontalWidget6")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalWidget6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.hideNamesBtn = QToolButton(self.horizontalWidget6)
        self.hideNamesBtn.setObjectName(u"hideNamesBtn")
        sizePolicy2.setHeightForWidth(self.hideNamesBtn.sizePolicy().hasHeightForWidth())
        self.hideNamesBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.hideNamesBtn)

        self.borderAllBtn = QToolButton(self.horizontalWidget6)
        self.borderAllBtn.setObjectName(u"borderAllBtn")
        sizePolicy2.setHeightForWidth(self.borderAllBtn.sizePolicy().hasHeightForWidth())
        self.borderAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.borderAllBtn)

        self.addAllBtn = QToolButton(self.horizontalWidget6)
        self.addAllBtn.setObjectName(u"addAllBtn")
        sizePolicy2.setHeightForWidth(self.addAllBtn.sizePolicy().hasHeightForWidth())
        self.addAllBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.addAllBtn)


        self.verticalLayout_22.addWidget(self.horizontalWidget6)


        self.verticalLayout_23.addWidget(self.themesPageContent)

        self.pages.addWidget(self.themesPage)
        self.statusBarPage = QWidget()
        self.statusBarPage.setObjectName(u"statusBarPage")
        self.verticalLayout_4 = QVBoxLayout(self.statusBarPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageHeader = QWidget(self.statusBarPage)
        self.statusBarPageHeader.setObjectName(u"statusBarPageHeader")
        self.horizontalLayout_5 = QHBoxLayout(self.statusBarPageHeader)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.toolButton_8 = QToolButton(self.statusBarPageHeader)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(False)
        self.toolButton_8.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_8.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.toolButton_8)

        self.verticalWidget_21 = QWidget(self.statusBarPageHeader)
        self.verticalWidget_21.setObjectName(u"verticalWidget_21")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl = QLabel(self.verticalWidget_21)
        self.statusBarLbl.setObjectName(u"statusBarLbl")
        self.statusBarLbl.setFont(font)

        self.verticalLayout_5.addWidget(self.statusBarLbl)

        self.statusBarEnabledChk = QCheckBox(self.verticalWidget_21)
        self.statusBarEnabledChk.setObjectName(u"statusBarEnabledChk")

        self.verticalLayout_5.addWidget(self.statusBarEnabledChk)


        self.horizontalLayout_5.addWidget(self.verticalWidget_21)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.statusBarPageHeader)

        self.line_8 = QFrame(self.statusBarPage)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_4.addWidget(self.line_8)

        self.scrollArea = QScrollArea(self.statusBarPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 1200))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(650, 1200))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(650, 1200))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.statusBarPageContent = QWidget(self.scrollAreaWidgetContents)
        self.statusBarPageContent.setObjectName(u"statusBarPageContent")
        self.statusBarPageContent.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.statusBarPageContent)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.statusBarPageContent)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.horizontalWidget7 = QWidget(self.statusBarPageContent)
        self.horizontalWidget7.setObjectName(u"horizontalWidget7")
        sizePolicy4.setHeightForWidth(self.horizontalWidget7.sizePolicy().hasHeightForWidth())
        self.horizontalWidget7.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget7)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pDefaultRdo = QRadioButton(self.horizontalWidget7)
        self.pDefaultRdo.setObjectName(u"pDefaultRdo")
        self.pDefaultRdo.setChecked(True)

        self.horizontalLayout_7.addWidget(self.pDefaultRdo)

        self.pShowRdo = QRadioButton(self.horizontalWidget7)
        self.pShowRdo.setObjectName(u"pShowRdo")

        self.horizontalLayout_7.addWidget(self.pShowRdo)

        self.pHideRdo = QRadioButton(self.horizontalWidget7)
        self.pHideRdo.setObjectName(u"pHideRdo")

        self.horizontalLayout_7.addWidget(self.pHideRdo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.horizontalWidget7)

        self.pCarrierChk = QCheckBox(self.statusBarPageContent)
        self.pCarrierChk.setObjectName(u"pCarrierChk")

        self.verticalLayout_8.addWidget(self.pCarrierChk)

        self.pCarrierTxt = QLineEdit(self.statusBarPageContent)
        self.pCarrierTxt.setObjectName(u"pCarrierTxt")

        self.verticalLayout_8.addWidget(self.pCarrierTxt)

        self.pBadgeChk = QCheckBox(self.statusBarPageContent)
        self.pBadgeChk.setObjectName(u"pBadgeChk")

        self.verticalLayout_8.addWidget(self.pBadgeChk)

        self.pBadgeTxt = QLineEdit(self.statusBarPageContent)
        self.pBadgeTxt.setObjectName(u"pBadgeTxt")

        self.verticalLayout_8.addWidget(self.pBadgeTxt)

        self.pTypeChk = QCheckBox(self.statusBarPageContent)
        self.pTypeChk.setObjectName(u"pTypeChk")

        self.verticalLayout_8.addWidget(self.pTypeChk)

        self.pTypeDrp = QComboBox(self.statusBarPageContent)
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.addItem("")
        self.pTypeDrp.setObjectName(u"pTypeDrp")
        self.pTypeDrp.setMinimumSize(QSize(0, 0))
        self.pTypeDrp.setMaximumSize(QSize(150, 16777215))
        self.pTypeDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.pTypeDrp.setMaxVisibleItems(15)

        self.verticalLayout_8.addWidget(self.pTypeDrp)

        self.pStrengthChk = QCheckBox(self.statusBarPageContent)
        self.pStrengthChk.setObjectName(u"pStrengthChk")

        self.verticalLayout_8.addWidget(self.pStrengthChk)

        self.horizontalWidget8 = QWidget(self.statusBarPageContent)
        self.horizontalWidget8.setObjectName(u"horizontalWidget8")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalWidget8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pStrengthLbl = QLabel(self.horizontalWidget8)
        self.pStrengthLbl.setObjectName(u"pStrengthLbl")
        self.pStrengthLbl.setMinimumSize(QSize(50, 0))
        self.pStrengthLbl.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.pStrengthLbl)

        self.pStrengthSld = QSlider(self.horizontalWidget8)
        self.pStrengthSld.setObjectName(u"pStrengthSld")
        self.pStrengthSld.setMaximum(4)
        self.pStrengthSld.setSingleStep(0)
        self.pStrengthSld.setPageStep(0)
        self.pStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.pStrengthSld)


        self.verticalLayout_8.addWidget(self.horizontalWidget8)

        self.line_9 = QFrame(self.statusBarPageContent)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_9)

        self.label_10 = QLabel(self.statusBarPageContent)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.horizontalWidget9 = QWidget(self.statusBarPageContent)
        self.horizontalWidget9.setObjectName(u"horizontalWidget9")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget9)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sDefaultRdo = QRadioButton(self.horizontalWidget9)
        self.sDefaultRdo.setObjectName(u"sDefaultRdo")
        self.sDefaultRdo.setChecked(True)

        self.horizontalLayout_8.addWidget(self.sDefaultRdo)

        self.sShowRdo = QRadioButton(self.horizontalWidget9)
        self.sShowRdo.setObjectName(u"sShowRdo")

        self.horizontalLayout_8.addWidget(self.sShowRdo)

        self.sHideRdo = QRadioButton(self.horizontalWidget9)
        self.sHideRdo.setObjectName(u"sHideRdo")

        self.horizontalLayout_8.addWidget(self.sHideRdo)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addWidget(self.horizontalWidget9)

        self.sCarrierChk = QCheckBox(self.statusBarPageContent)
        self.sCarrierChk.setObjectName(u"sCarrierChk")

        self.verticalLayout_8.addWidget(self.sCarrierChk)

        self.sCarrierTxt = QLineEdit(self.statusBarPageContent)
        self.sCarrierTxt.setObjectName(u"sCarrierTxt")

        self.verticalLayout_8.addWidget(self.sCarrierTxt)

        self.sBadgeChk = QCheckBox(self.statusBarPageContent)
        self.sBadgeChk.setObjectName(u"sBadgeChk")

        self.verticalLayout_8.addWidget(self.sBadgeChk)

        self.sBadgeTxt = QLineEdit(self.statusBarPageContent)
        self.sBadgeTxt.setObjectName(u"sBadgeTxt")

        self.verticalLayout_8.addWidget(self.sBadgeTxt)

        self.sTypeChk = QCheckBox(self.statusBarPageContent)
        self.sTypeChk.setObjectName(u"sTypeChk")

        self.verticalLayout_8.addWidget(self.sTypeChk)

        self.sTypeDrp = QComboBox(self.statusBarPageContent)
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.addItem("")
        self.sTypeDrp.setObjectName(u"sTypeDrp")
        self.sTypeDrp.setMinimumSize(QSize(0, 0))
        self.sTypeDrp.setMaximumSize(QSize(150, 16777215))
        self.sTypeDrp.setStyleSheet(u"QComboBox {\n"
"	background-color: #3b3b3b;\n"
"    border: none;\n"
"    color: #e8e8e8;\n"
"    font-size: 14px;\n"
"	padding-left: 8px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icon/caret-down-fill.svg);\n"
"	icon-size: 16px;\n"
"    subcontrol-position: right center;\n"
"	margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #3b3b3b;\n"
"    outline: none;\n"
"	margin-top: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color: #3b3b3b;\n"
"	color: #e8e8e8;\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #535353;\n"
"    color: #ffffff;\n"
"}")
        self.sTypeDrp.setMaxVisibleItems(15)

        self.verticalLayout_8.addWidget(self.sTypeDrp)

        self.sStrengthChk = QCheckBox(self.statusBarPageContent)
        self.sStrengthChk.setObjectName(u"sStrengthChk")

        self.verticalLayout_8.addWidget(self.sStrengthChk)

        self.horizontalWidget10 = QWidget(self.statusBarPageContent)
        self.horizontalWidget10.setObjectName(u"horizontalWidget10")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalWidget10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.sStrengthLbl = QLabel(self.horizontalWidget10)
        self.sStrengthLbl.setObjectName(u"sStrengthLbl")
        self.sStrengthLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.sStrengthLbl)

        self.sStrengthSld = QSlider(self.horizontalWidget10)
        self.sStrengthSld.setObjectName(u"sStrengthSld")
        self.sStrengthSld.setMaximum(4)
        self.sStrengthSld.setSingleStep(0)
        self.sStrengthSld.setPageStep(0)
        self.sStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.sStrengthSld)


        self.verticalLayout_8.addWidget(self.horizontalWidget10)

        self.line_7 = QFrame(self.statusBarPageContent)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_7)

        self.timeChk = QCheckBox(self.statusBarPageContent)
        self.timeChk.setObjectName(u"timeChk")

        self.verticalLayout_8.addWidget(self.timeChk)

        self.timeTxt = QLineEdit(self.statusBarPageContent)
        self.timeTxt.setObjectName(u"timeTxt")

        self.verticalLayout_8.addWidget(self.timeTxt)

        self.breadcrumbChk = QCheckBox(self.statusBarPageContent)
        self.breadcrumbChk.setObjectName(u"breadcrumbChk")

        self.verticalLayout_8.addWidget(self.breadcrumbChk)

        self.breadcrumbTxt = QLineEdit(self.statusBarPageContent)
        self.breadcrumbTxt.setObjectName(u"breadcrumbTxt")

        self.verticalLayout_8.addWidget(self.breadcrumbTxt)

        self.batteryDetailChk = QCheckBox(self.statusBarPageContent)
        self.batteryDetailChk.setObjectName(u"batteryDetailChk")

        self.verticalLayout_8.addWidget(self.batteryDetailChk)

        self.batteryDetailTxt = QLineEdit(self.statusBarPageContent)
        self.batteryDetailTxt.setObjectName(u"batteryDetailTxt")

        self.verticalLayout_8.addWidget(self.batteryDetailTxt)

        self.batteryCapacityChk = QCheckBox(self.statusBarPageContent)
        self.batteryCapacityChk.setObjectName(u"batteryCapacityChk")

        self.verticalLayout_8.addWidget(self.batteryCapacityChk)

        self.horizontalWidget11 = QWidget(self.statusBarPageContent)
        self.horizontalWidget11.setObjectName(u"horizontalWidget11")
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalWidget11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.batteryCapacityLbl = QLabel(self.horizontalWidget11)
        self.batteryCapacityLbl.setObjectName(u"batteryCapacityLbl")
        self.batteryCapacityLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_11.addWidget(self.batteryCapacityLbl)

        self.batteryCapacitySld = QSlider(self.horizontalWidget11)
        self.batteryCapacitySld.setObjectName(u"batteryCapacitySld")
        self.batteryCapacitySld.setMaximum(100)
        self.batteryCapacitySld.setSingleStep(0)
        self.batteryCapacitySld.setPageStep(0)
        self.batteryCapacitySld.setTracking(True)
        self.batteryCapacitySld.setOrientation(Qt.Horizontal)
        self.batteryCapacitySld.setInvertedAppearance(False)
        self.batteryCapacitySld.setInvertedControls(False)
        self.batteryCapacitySld.setTickInterval(5)

        self.horizontalLayout_11.addWidget(self.batteryCapacitySld)


        self.verticalLayout_8.addWidget(self.horizontalWidget11)

        self.wifiStrengthChk = QCheckBox(self.statusBarPageContent)
        self.wifiStrengthChk.setObjectName(u"wifiStrengthChk")

        self.verticalLayout_8.addWidget(self.wifiStrengthChk)

        self.horizontalWidget12 = QWidget(self.statusBarPageContent)
        self.horizontalWidget12.setObjectName(u"horizontalWidget12")
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalWidget12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.wifiStrengthLbl = QLabel(self.horizontalWidget12)
        self.wifiStrengthLbl.setObjectName(u"wifiStrengthLbl")
        self.wifiStrengthLbl.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_12.addWidget(self.wifiStrengthLbl)

        self.wifiStrengthSld = QSlider(self.horizontalWidget12)
        self.wifiStrengthSld.setObjectName(u"wifiStrengthSld")
        self.wifiStrengthSld.setMaximum(3)
        self.wifiStrengthSld.setSingleStep(0)
        self.wifiStrengthSld.setPageStep(0)
        self.wifiStrengthSld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.wifiStrengthSld)


        self.verticalLayout_8.addWidget(self.horizontalWidget12)

        self.numericWifiChk = QCheckBox(self.statusBarPageContent)
        self.numericWifiChk.setObjectName(u"numericWifiChk")

        self.verticalLayout_8.addWidget(self.numericWifiChk)

        self.numericCellChk = QCheckBox(self.statusBarPageContent)
        self.numericCellChk.setObjectName(u"numericCellChk")

        self.verticalLayout_8.addWidget(self.numericCellChk)

        self.label_5 = QLabel(self.statusBarPageContent)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.line_10 = QFrame(self.statusBarPageContent)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line_10)

        self.hideDNDChk = QCheckBox(self.statusBarPageContent)
        self.hideDNDChk.setObjectName(u"hideDNDChk")

        self.verticalLayout_8.addWidget(self.hideDNDChk)

        self.hideAirplaneChk = QCheckBox(self.statusBarPageContent)
        self.hideAirplaneChk.setObjectName(u"hideAirplaneChk")

        self.verticalLayout_8.addWidget(self.hideAirplaneChk)

        self.hideWifiChk = QCheckBox(self.statusBarPageContent)
        self.hideWifiChk.setObjectName(u"hideWifiChk")

        self.verticalLayout_8.addWidget(self.hideWifiChk)

        self.hideBatteryChk = QCheckBox(self.statusBarPageContent)
        self.hideBatteryChk.setObjectName(u"hideBatteryChk")

        self.verticalLayout_8.addWidget(self.hideBatteryChk)

        self.hideBluetoothChk = QCheckBox(self.statusBarPageContent)
        self.hideBluetoothChk.setObjectName(u"hideBluetoothChk")

        self.verticalLayout_8.addWidget(self.hideBluetoothChk)

        self.hideAlarmChk = QCheckBox(self.statusBarPageContent)
        self.hideAlarmChk.setObjectName(u"hideAlarmChk")

        self.verticalLayout_8.addWidget(self.hideAlarmChk)

        self.hideLocationChk = QCheckBox(self.statusBarPageContent)
        self.hideLocationChk.setObjectName(u"hideLocationChk")

        self.verticalLayout_8.addWidget(self.hideLocationChk)

        self.hideRotationChk = QCheckBox(self.statusBarPageContent)
        self.hideRotationChk.setObjectName(u"hideRotationChk")

        self.verticalLayout_8.addWidget(self.hideRotationChk)

        self.hideAirPlayChk = QCheckBox(self.statusBarPageContent)
        self.hideAirPlayChk.setObjectName(u"hideAirPlayChk")

        self.verticalLayout_8.addWidget(self.hideAirPlayChk)

        self.hideCarPlayChk = QCheckBox(self.statusBarPageContent)
        self.hideCarPlayChk.setObjectName(u"hideCarPlayChk")

        self.verticalLayout_8.addWidget(self.hideCarPlayChk)

        self.hideVPNChk = QCheckBox(self.statusBarPageContent)
        self.hideVPNChk.setObjectName(u"hideVPNChk")

        self.verticalLayout_8.addWidget(self.hideVPNChk)

        self.label_12 = QLabel(self.statusBarPageContent)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.verticalLayout_9.addWidget(self.statusBarPageContent)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.pages.addWidget(self.statusBarPage)
        self.customOperationsPage = QWidget()
        self.customOperationsPage.setObjectName(u"customOperationsPage")
        self.verticalLayout_20 = QVBoxLayout(self.customOperationsPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_7 = QWidget(self.customOperationsPage)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 9, 0, 9)
        self.toolButton_12 = QToolButton(self.horizontalWidget_7)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(False)
        self.toolButton_12.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_12.setIcon(icon5)
        self.toolButton_12.setIconSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButton_12)

        self.verticalWidget_6 = QWidget(self.horizontalWidget_7)
        self.verticalWidget_6.setObjectName(u"verticalWidget_6")
        self.verticalLayout_18 = QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.customOperationsLbl = QLabel(self.verticalWidget_6)
        self.customOperationsLbl.setObjectName(u"customOperationsLbl")
        self.customOperationsLbl.setFont(font)

        self.verticalLayout_18.addWidget(self.customOperationsLbl)

        self.label_14 = QLabel(self.verticalWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_18.addWidget(self.label_14)


        self.horizontalLayout_22.addWidget(self.verticalWidget_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_9)


        self.verticalLayout_20.addWidget(self.horizontalWidget_7)

        self.line_14 = QFrame(self.customOperationsPage)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_20.addWidget(self.line_14)

        self.customOperationsPageContent = QWidget(self.customOperationsPage)
        self.customOperationsPageContent.setObjectName(u"customOperationsPageContent")
        self.customOperationsPageContent.setEnabled(False)
        self.verticalLayout_19 = QVBoxLayout(self.customOperationsPageContent)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.customOpsTopBtns = QHBoxLayout()
#ifndef Q_OS_MAC
        self.customOpsTopBtns.setSpacing(-1)
#endif
        self.customOpsTopBtns.setObjectName(u"customOpsTopBtns")
        self.customOpsTopBtns.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.customOpsTopBtns.addItem(self.horizontalSpacer_17)

        self.importOperationBtn = QToolButton(self.customOperationsPageContent)
        self.importOperationBtn.setObjectName(u"importOperationBtn")
        self.importOperationBtn.setEnabled(False)
        icon22 = QIcon()
        icon22.addFile(u":/icon/import.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importOperationBtn.setIcon(icon22)
        self.importOperationBtn.setIconSize(QSize(20, 20))
        self.importOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.importOperationBtn, 0, Qt.AlignLeft)

        self.newOperationBtn = QToolButton(self.customOperationsPageContent)
        self.newOperationBtn.setObjectName(u"newOperationBtn")
        self.newOperationBtn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.newOperationBtn.sizePolicy().hasHeightForWidth())
        self.newOperationBtn.setSizePolicy(sizePolicy2)
        self.newOperationBtn.setMinimumSize(QSize(0, 35))
        icon23 = QIcon()
        icon23.addFile(u":/icon/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newOperationBtn.setIcon(icon23)
        self.newOperationBtn.setIconSize(QSize(16, 16))
        self.newOperationBtn.setCheckable(False)
        self.newOperationBtn.setAutoExclusive(True)
        self.newOperationBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.customOpsTopBtns.addWidget(self.newOperationBtn, 0, Qt.AlignLeft)


        self.verticalLayout_19.addLayout(self.customOpsTopBtns)

        self.operationsCnt = QWidget(self.customOperationsPageContent)
        self.operationsCnt.setObjectName(u"operationsCnt")
        self.operationsCnt.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.operationsCnt.sizePolicy().hasHeightForWidth())
        self.operationsCnt.setSizePolicy(sizePolicy5)

        self.verticalLayout_19.addWidget(self.operationsCnt)


        self.verticalLayout_20.addWidget(self.customOperationsPageContent)

        self.pages.addWidget(self.customOperationsPage)
        self.springboardOptionsPage = QWidget()
        self.springboardOptionsPage.setObjectName(u"springboardOptionsPage")
        self.verticalLayout_10 = QVBoxLayout(self.springboardOptionsPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_4 = QWidget(self.springboardOptionsPage)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 9, 0, 9)
        self.toolButton_7 = QToolButton(self.horizontalWidget_4)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_7.setIcon(icon8)

        self.horizontalLayout_13.addWidget(self.toolButton_7)

        self.verticalWidget_3 = QWidget(self.horizontalWidget_4)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.springboardOptionsLbl = QLabel(self.verticalWidget_3)
        self.springboardOptionsLbl.setObjectName(u"springboardOptionsLbl")
        self.springboardOptionsLbl.setFont(font)

        self.verticalLayout_7.addWidget(self.springboardOptionsLbl)

        self.springboardOptionsEnabledChk = QCheckBox(self.verticalWidget_3)
        self.springboardOptionsEnabledChk.setObjectName(u"springboardOptionsEnabledChk")

        self.verticalLayout_7.addWidget(self.springboardOptionsEnabledChk)


        self.horizontalLayout_13.addWidget(self.verticalWidget_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addWidget(self.horizontalWidget_4)

        self.line_11 = QFrame(self.springboardOptionsPage)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_10.addWidget(self.line_11)

        self.springboardOptionsPageContent = QWidget(self.springboardOptionsPage)
        self.springboardOptionsPageContent.setObjectName(u"springboardOptionsPageContent")
        self.springboardOptionsPageContent.setEnabled(False)
        self.springboardOptionsPageContent.setMaximumSize(QSize(650, 16777215))
        self._2 = QVBoxLayout(self.springboardOptionsPageContent)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.springboardOptionsPageContent)
        self.label_8.setObjectName(u"label_8")

        self._2.addWidget(self.label_8)

        self.horizontalWidget13 = QWidget(self.springboardOptionsPageContent)
        self.horizontalWidget13.setObjectName(u"horizontalWidget13")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalWidget13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.UIAnimSpeedLbl = QLabel(self.horizontalWidget13)
        self.UIAnimSpeedLbl.setObjectName(u"UIAnimSpeedLbl")
        self.UIAnimSpeedLbl.setMinimumSize(QSize(75, 0))
        self.UIAnimSpeedLbl.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_14.addWidget(self.UIAnimSpeedLbl)

        self.UIAnimSpeedSld = QSlider(self.horizontalWidget13)
        self.UIAnimSpeedSld.setObjectName(u"UIAnimSpeedSld")
        self.UIAnimSpeedSld.setMinimum(1)
        self.UIAnimSpeedSld.setMaximum(200)
        self.UIAnimSpeedSld.setSingleStep(0)
        self.UIAnimSpeedSld.setPageStep(0)
        self.UIAnimSpeedSld.setValue(100)
        self.UIAnimSpeedSld.setOrientation(Qt.Horizontal)
        self.UIAnimSpeedSld.setTickInterval(5)

        self.horizontalLayout_14.addWidget(self.UIAnimSpeedSld)


        self._2.addWidget(self.horizontalWidget13)

        self.label_13 = QLabel(self.springboardOptionsPageContent)
        self.label_13.setObjectName(u"label_13")

        self._2.addWidget(self.label_13)

        self.footnoteTxt = QLineEdit(self.springboardOptionsPageContent)
        self.footnoteTxt.setObjectName(u"footnoteTxt")

        self._2.addWidget(self.footnoteTxt)

        self.line_6 = QFrame(self.springboardOptionsPageContent)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.Shape.HLine)

        self._2.addWidget(self.line_6)

        self.disableLockRespringChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableLockRespringChk.setObjectName(u"disableLockRespringChk")

        self._2.addWidget(self.disableLockRespringChk)

        self.disableDimmingChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableDimmingChk.setObjectName(u"disableDimmingChk")

        self._2.addWidget(self.disableDimmingChk)

        self.disableBatteryAlertsChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableBatteryAlertsChk.setObjectName(u"disableBatteryAlertsChk")

        self._2.addWidget(self.disableBatteryAlertsChk)

        self.disableCrumbChk = QCheckBox(self.springboardOptionsPageContent)
        self.disableCrumbChk.setObjectName(u"disableCrumbChk")

        self._2.addWidget(self.disableCrumbChk)

        self.enableSupervisionTextChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableSupervisionTextChk.setObjectName(u"enableSupervisionTextChk")

        self._2.addWidget(self.enableSupervisionTextChk)

        self.line_16 = QFrame(self.springboardOptionsPageContent)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setFrameShape(QFrame.Shape.HLine)

        self._2.addWidget(self.line_16)

        self.enableWiFiDebuggerChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableWiFiDebuggerChk.setObjectName(u"enableWiFiDebuggerChk")

        self._2.addWidget(self.enableWiFiDebuggerChk)

        self.enableShutdownSoundChk = QCheckBox(self.springboardOptionsPageContent)
        self.enableShutdownSoundChk.setObjectName(u"enableShutdownSoundChk")

        self._2.addWidget(self.enableShutdownSoundChk)

        self.allowAirDropEveryoneChk = QCheckBox(self.springboardOptionsPageContent)
        self.allowAirDropEveryoneChk.setObjectName(u"allowAirDropEveryoneChk")

        self._2.addWidget(self.allowAirDropEveryoneChk)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._2.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addWidget(self.springboardOptionsPageContent)

        self.pages.addWidget(self.springboardOptionsPage)
        self.internalOptionsPage = QWidget()
        self.internalOptionsPage.setObjectName(u"internalOptionsPage")
        self.verticalLayout_14 = QVBoxLayout(self.internalOptionsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_5 = QWidget(self.internalOptionsPage)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 9, 0, 9)
        self.toolButton_10 = QToolButton(self.horizontalWidget_5)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(False)
        self.toolButton_10.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_10.setIcon(icon9)

        self.horizontalLayout_20.addWidget(self.toolButton_10)

        self.verticalWidget_4 = QWidget(self.horizontalWidget_5)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalLayout_12 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.internalOptionsLbl = QLabel(self.verticalWidget_4)
        self.internalOptionsLbl.setObjectName(u"internalOptionsLbl")
        self.internalOptionsLbl.setFont(font)

        self.verticalLayout_12.addWidget(self.internalOptionsLbl)

        self.internalOptionsEnabledChk = QCheckBox(self.verticalWidget_4)
        self.internalOptionsEnabledChk.setObjectName(u"internalOptionsEnabledChk")

        self.verticalLayout_12.addWidget(self.internalOptionsEnabledChk)


        self.horizontalLayout_20.addWidget(self.verticalWidget_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.horizontalWidget_5)

        self.line_12 = QFrame(self.internalOptionsPage)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_14.addWidget(self.line_12)

        self.internalOptionsPageContent = QWidget(self.internalOptionsPage)
        self.internalOptionsPageContent.setObjectName(u"internalOptionsPageContent")
        self.internalOptionsPageContent.setEnabled(False)
        self.verticalLayout_13 = QVBoxLayout(self.internalOptionsPageContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.buildVersionChk = QCheckBox(self.internalOptionsPageContent)
        self.buildVersionChk.setObjectName(u"buildVersionChk")

        self.verticalLayout_13.addWidget(self.buildVersionChk)

        self.RTLChk = QCheckBox(self.internalOptionsPageContent)
        self.RTLChk.setObjectName(u"RTLChk")

        self.verticalLayout_13.addWidget(self.RTLChk)

        self.div = QFrame(self.internalOptionsPageContent)
        self.div.setObjectName(u"div")
        self.div.setEnabled(False)
        self.div.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.div.setFrameShadow(QFrame.Plain)
        self.div.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_13.addWidget(self.div)

        self.metalHUDChk = QCheckBox(self.internalOptionsPageContent)
        self.metalHUDChk.setObjectName(u"metalHUDChk")

        self.verticalLayout_13.addWidget(self.metalHUDChk)

        self.accessoryChk = QCheckBox(self.internalOptionsPageContent)
        self.accessoryChk.setObjectName(u"accessoryChk")

        self.verticalLayout_13.addWidget(self.accessoryChk)

        self.iMessageChk = QCheckBox(self.internalOptionsPageContent)
        self.iMessageChk.setObjectName(u"iMessageChk")

        self.verticalLayout_13.addWidget(self.iMessageChk)

        self.IDSChk = QCheckBox(self.internalOptionsPageContent)
        self.IDSChk.setObjectName(u"IDSChk")

        self.verticalLayout_13.addWidget(self.IDSChk)

        self.VCChk = QCheckBox(self.internalOptionsPageContent)
        self.VCChk.setObjectName(u"VCChk")

        self.verticalLayout_13.addWidget(self.VCChk)

        self.line_17 = QFrame(self.internalOptionsPageContent)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_13.addWidget(self.line_17)

        self.appStoreChk = QCheckBox(self.internalOptionsPageContent)
        self.appStoreChk.setObjectName(u"appStoreChk")

        self.verticalLayout_13.addWidget(self.appStoreChk)

        self.notesChk = QCheckBox(self.internalOptionsPageContent)
        self.notesChk.setObjectName(u"notesChk")

        self.verticalLayout_13.addWidget(self.notesChk)

        self.line_18 = QFrame(self.internalOptionsPageContent)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_13.addWidget(self.line_18)

        self.showTouchesChk = QCheckBox(self.internalOptionsPageContent)
        self.showTouchesChk.setObjectName(u"showTouchesChk")

        self.verticalLayout_13.addWidget(self.showTouchesChk)

        self.hideRespringChk = QCheckBox(self.internalOptionsPageContent)
        self.hideRespringChk.setObjectName(u"hideRespringChk")

        self.verticalLayout_13.addWidget(self.hideRespringChk)

        self.enableWakeVibrateChk = QCheckBox(self.internalOptionsPageContent)
        self.enableWakeVibrateChk.setObjectName(u"enableWakeVibrateChk")

        self.verticalLayout_13.addWidget(self.enableWakeVibrateChk)

        self.line_19 = QFrame(self.internalOptionsPageContent)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_13.addWidget(self.line_19)

        self.pasteSoundChk = QCheckBox(self.internalOptionsPageContent)
        self.pasteSoundChk.setObjectName(u"pasteSoundChk")

        self.verticalLayout_13.addWidget(self.pasteSoundChk)

        self.notifyPastesChk = QCheckBox(self.internalOptionsPageContent)
        self.notifyPastesChk.setObjectName(u"notifyPastesChk")

        self.verticalLayout_13.addWidget(self.notifyPastesChk)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.verticalLayout_14.addWidget(self.internalOptionsPageContent)

        self.pages.addWidget(self.internalOptionsPage)
        self.setupOptionsPage = QWidget()
        self.setupOptionsPage.setObjectName(u"setupOptionsPage")
        self.verticalLayout_17 = QVBoxLayout(self.setupOptionsPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget_6 = QWidget(self.setupOptionsPage)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 9, 0, 9)
        self.toolButton_11 = QToolButton(self.horizontalWidget_6)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(False)
        self.toolButton_11.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_11.setIcon(icon10)

        self.horizontalLayout_21.addWidget(self.toolButton_11)

        self.verticalWidget_5 = QWidget(self.horizontalWidget_6)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalLayout_15 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.setupOptionsLbl = QLabel(self.verticalWidget_5)
        self.setupOptionsLbl.setObjectName(u"setupOptionsLbl")
        self.setupOptionsLbl.setFont(font)

        self.verticalLayout_15.addWidget(self.setupOptionsLbl)

        self.setupOptionsEnabledChk = QCheckBox(self.verticalWidget_5)
        self.setupOptionsEnabledChk.setObjectName(u"setupOptionsEnabledChk")

        self.verticalLayout_15.addWidget(self.setupOptionsEnabledChk)


        self.horizontalLayout_21.addWidget(self.verticalWidget_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addWidget(self.horizontalWidget_6)

        self.line_13 = QFrame(self.setupOptionsPage)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_17.addWidget(self.line_13)

        self.setupOptionsPageContent = QWidget(self.setupOptionsPage)
        self.setupOptionsPageContent.setObjectName(u"setupOptionsPageContent")
        self.setupOptionsPageContent.setEnabled(False)
        self.verticalLayout_16 = QVBoxLayout(self.setupOptionsPageContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.skipSetupChk = QCheckBox(self.setupOptionsPageContent)
        self.skipSetupChk.setObjectName(u"skipSetupChk")

        self.verticalLayout_16.addWidget(self.skipSetupChk)

        self.enableSupervisionChk = QCheckBox(self.setupOptionsPageContent)
        self.enableSupervisionChk.setObjectName(u"enableSupervisionChk")

        self.verticalLayout_16.addWidget(self.enableSupervisionChk)

        self.organizationNameTxt = QLineEdit(self.setupOptionsPageContent)
        self.organizationNameTxt.setObjectName(u"organizationNameTxt")

        self.verticalLayout_16.addWidget(self.organizationNameTxt)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)


        self.verticalLayout_17.addWidget(self.setupOptionsPageContent)

        self.pages.addWidget(self.setupOptionsPage)
        self.applyPage = QWidget()
        self.applyPage.setObjectName(u"applyPage")
        self.verticalLayout_6 = QVBoxLayout(self.applyPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget3 = QWidget(self.applyPage)
        self.verticalWidget3.setObjectName(u"verticalWidget3")
        self.verticalLayout_24 = QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.locSimPageHeader_2 = QWidget(self.verticalWidget3)
        self.locSimPageHeader_2.setObjectName(u"locSimPageHeader_2")
        self.horizontalLayout_33 = QHBoxLayout(self.locSimPageHeader_2)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, -1, 0, -1)
        self.toolButton_18 = QToolButton(self.locSimPageHeader_2)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setEnabled(False)
        self.toolButton_18.setStyleSheet(u"QToolButton {\n"
"	icon-size: 24px;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"	padding-right: 5px;\n"
"	border-radius: 0px;\n"
"}")
        self.toolButton_18.setIcon(icon11)

        self.horizontalLayout_33.addWidget(self.toolButton_18)

        self.verticalWidget_11 = QWidget(self.locSimPageHeader_2)
        self.verticalWidget_11.setObjectName(u"verticalWidget_11")
        self.verticalLayout_33 = QVBoxLayout(self.verticalWidget_11)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.statusBarLbl_5 = QLabel(self.verticalWidget_11)
        self.statusBarLbl_5.setObjectName(u"statusBarLbl_5")
        self.statusBarLbl_5.setFont(font)

        self.verticalLayout_33.addWidget(self.statusBarLbl_5)

        self.label_16 = QLabel(self.verticalWidget_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_33.addWidget(self.label_16)


        self.horizontalLayout_33.addWidget(self.verticalWidget_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_15)


        self.verticalLayout_24.addWidget(self.locSimPageHeader_2)

        self.line_5 = QFrame(self.verticalWidget3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"QFrame {\n"
"	color: #414141;\n"
"}")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_24.addWidget(self.line_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.label_6 = QLabel(self.verticalWidget3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_6)

        self.enabledTweaksLbl = QLabel(self.verticalWidget3)
        self.enabledTweaksLbl.setObjectName(u"enabledTweaksLbl")
        self.enabledTweaksLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.enabledTweaksLbl)

        self.horizontalWidget14 = QWidget(self.verticalWidget3)
        self.horizontalWidget14.setObjectName(u"horizontalWidget14")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalWidget14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 20, 0, 0)
        self.applyTweaksBtn = QToolButton(self.horizontalWidget14)
        self.applyTweaksBtn.setObjectName(u"applyTweaksBtn")
        self.applyTweaksBtn.setIcon(icon11)
        self.applyTweaksBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_17.addWidget(self.applyTweaksBtn)


        self.verticalLayout_24.addWidget(self.horizontalWidget14)

        self.statusLbl = QLabel(self.verticalWidget3)
        self.statusLbl.setObjectName(u"statusLbl")
        self.statusLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.statusLbl)

        self.restoreProgressBar = QProgressBar(self.verticalWidget3)
        self.restoreProgressBar.setObjectName(u"restoreProgressBar")
        sizePolicy.setHeightForWidth(self.restoreProgressBar.sizePolicy().hasHeightForWidth())
        self.restoreProgressBar.setSizePolicy(sizePolicy)
        self.restoreProgressBar.setMinimumSize(QSize(150, 0))
        self.restoreProgressBar.setValue(0)
        self.restoreProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.restoreProgressBar, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_2)

        self.horizontalWidget15 = QWidget(self.verticalWidget3)
        self.horizontalWidget15.setObjectName(u"horizontalWidget15")
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_14)

        self.removeTweaksBtn = QToolButton(self.horizontalWidget15)
        self.removeTweaksBtn.setObjectName(u"removeTweaksBtn")

        self.horizontalLayout_25.addWidget(self.removeTweaksBtn)

        self.deepCleanBtn = QToolButton(self.horizontalWidget15)
        self.deepCleanBtn.setObjectName(u"deepCleanBtn")

        self.horizontalLayout_25.addWidget(self.deepCleanBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)


        self.verticalLayout_24.addWidget(self.horizontalWidget15)


        self.verticalLayout_6.addWidget(self.verticalWidget3)

        self.pages.addWidget(self.applyPage)

        self._3.addWidget(self.pages)


        self.horizontalLayout_18.addWidget(self.main)


        self.verticalLayout_11.addWidget(self.body)

        CowabungaLite.setCentralWidget(self.centralwidget)

        self.retranslateUi(CowabungaLite)

        self.devicePicker.setCurrentIndex(-1)
        self.pages.setCurrentIndex(0)
        self.pTypeDrp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CowabungaLite)
    # setupUi

    def retranslateUi(self, CowabungaLite):
        CowabungaLite.setWindowTitle(QCoreApplication.translate("CowabungaLite", u"Cowabunga Lite", None))
        self.centralwidget.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"central", None))
        self.devicePicker.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"None", None))
        self.refreshBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"btn", None))
        self.titleBar.setText(QCoreApplication.translate("CowabungaLite", u"Cowabunga Lite", None))
        self.homePageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Home", None))
        self.homePageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.explorePageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Explore", None))
        self.explorePageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.locSimPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Location Simulation", None))
        self.locSimPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.customOperationsPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Custom Operations", None))
        self.customOperationsPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.themesPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Icon Theming", None))
        self.themesPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.statusBarPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Status Bar", None))
        self.statusBarPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.springboardOptionsPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Springboard Options", None))
        self.springboardOptionsPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.internalOptionsPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Internal Options", None))
        self.internalOptionsPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.setupOptionsPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Setup Options", None))
        self.setupOptionsPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.applyPageBtn.setText(QCoreApplication.translate("CowabungaLite", u"    Apply", None))
        self.applyPageBtn.setProperty("cls", QCoreApplication.translate("CowabungaLite", u"sidebarBtn", None))
        self.phoneNameLbl.setText(QCoreApplication.translate("CowabungaLite", u"Phone", None))
        self.phoneVersionLbl.setText(QCoreApplication.translate("CowabungaLite", u"<a style=\"text-decoration:none; color: white\" href=\"#\">Version</a>", None))
        self.bigMilkBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.label_2.setText(QCoreApplication.translate("CowabungaLite", u"Cowabunga Lite", None))
        self.patreonBtn.setText(QCoreApplication.translate("CowabungaLite", u"  Star the Project on GitHub", None))
        self.discordBtn.setText(QCoreApplication.translate("CowabungaLite", u"  Join the Discord", None))
        self.leminBtn.setText(QCoreApplication.translate("CowabungaLite", u"  LeminLimez", None))
        self.leminGitHubBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.leminTwitterBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.leminKoFiBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.toolButton_14.setText(QCoreApplication.translate("CowabungaLite", u"Main Developer, Cowabunga MDC Developer", None))
        self.avangelistaBtn.setText(QCoreApplication.translate("CowabungaLite", u"  Avangelista", None))
        self.avangelistaGitHubBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.avangelistaTwitterBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.avangelistaKoFiBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.toolButton_5.setText(QCoreApplication.translate("CowabungaLite", u"Old Windows UI, Backup Generator, App Getter", None))
        self.toolButton_15.setText(QCoreApplication.translate("CowabungaLite", u"Additional Thanks", None))
        self.iTechBtn.setText(QCoreApplication.translate("CowabungaLite", u"iTechExpert", None))
        self.libiBtn.setText(QCoreApplication.translate("CowabungaLite", u"pymobiledevice3", None))
        self.qtBtn.setText(QCoreApplication.translate("CowabungaLite", u"Qt Creator", None))
        self.label.setText(QCoreApplication.translate("CowabungaLite", u"Cowabunga Lite (Python) - Version 1.0.0", None))
        self.exploreLbl.setText(QCoreApplication.translate("CowabungaLite", u"Explore", None))
        self.exploreSubLbl.setText("")
        self.statusBarLbl_2.setText(QCoreApplication.translate("CowabungaLite", u"Location Simulation", None))
        self.label_4.setText("")
        self.loadLocSimBtn.setText(QCoreApplication.translate("CowabungaLite", u"Start Location Simulation", None))
        self.label_7.setText(QCoreApplication.translate("CowabungaLite", u"Latitude", None))
        self.latitudeTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"XXX.XXXXX", None))
        self.label_11.setText(QCoreApplication.translate("CowabungaLite", u"Longitude", None))
        self.longitudeTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"XXX.XXXXX", None))
        self.setLocationBtn.setText(QCoreApplication.translate("CowabungaLite", u"Set Location", None))
        self.resetLocationBtn.setText(QCoreApplication.translate("CowabungaLite", u"Reset Location", None))
        self.themesLbl.setText(QCoreApplication.translate("CowabungaLite", u"Icon Theming", None))
        self.themesEnabledChk.setText(QCoreApplication.translate("CowabungaLite", u"Modify", None))
        self.importThemeBtn.setText(QCoreApplication.translate("CowabungaLite", u"Import Theme:", None))
        self.importThemeFolderBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.importThemeZipBtn.setText(QCoreApplication.translate("CowabungaLite", u"...", None))
        self.label_3.setText(QCoreApplication.translate("CowabungaLite", u"Customize Individual Apps", None))
        self.hideNamesBtn.setText(QCoreApplication.translate("CowabungaLite", u"Hide/Show All App Names", None))
        self.borderAllBtn.setText(QCoreApplication.translate("CowabungaLite", u"Toggle All \"Border\"", None))
        self.addAllBtn.setText(QCoreApplication.translate("CowabungaLite", u"Toggle All \"Add to Device\"", None))
        self.statusBarLbl.setText(QCoreApplication.translate("CowabungaLite", u"Status Bar", None))
        self.statusBarEnabledChk.setText(QCoreApplication.translate("CowabungaLite", u"Modify", None))
        self.label_9.setText(QCoreApplication.translate("CowabungaLite", u"Primary Cellular", None))
        self.pDefaultRdo.setText(QCoreApplication.translate("CowabungaLite", u"Default", None))
        self.pShowRdo.setText(QCoreApplication.translate("CowabungaLite", u"Force Show", None))
        self.pHideRdo.setText(QCoreApplication.translate("CowabungaLite", u"Force Hide", None))
        self.pCarrierChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Carrier Text", None))
        self.pCarrierTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Carrier Text", None))
        self.pBadgeChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Service Badge Text", None))
        self.pBadgeTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Service Badge Text", None))
        self.pTypeChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Data Network Type", None))
        self.pTypeDrp.setItemText(0, QCoreApplication.translate("CowabungaLite", u"GPRS", None))
        self.pTypeDrp.setItemText(1, QCoreApplication.translate("CowabungaLite", u"EDGE", None))
        self.pTypeDrp.setItemText(2, QCoreApplication.translate("CowabungaLite", u"3G", None))
        self.pTypeDrp.setItemText(3, QCoreApplication.translate("CowabungaLite", u"4G", None))
        self.pTypeDrp.setItemText(4, QCoreApplication.translate("CowabungaLite", u"LTE", None))
        self.pTypeDrp.setItemText(5, QCoreApplication.translate("CowabungaLite", u"Wi-Fi", None))
        self.pTypeDrp.setItemText(6, QCoreApplication.translate("CowabungaLite", u"Personal Hotspot", None))
        self.pTypeDrp.setItemText(7, QCoreApplication.translate("CowabungaLite", u"1x", None))
        self.pTypeDrp.setItemText(8, QCoreApplication.translate("CowabungaLite", u"5G\u1d07", None))
        self.pTypeDrp.setItemText(9, QCoreApplication.translate("CowabungaLite", u"LTE-A", None))
        self.pTypeDrp.setItemText(10, QCoreApplication.translate("CowabungaLite", u"LTE+", None))
        self.pTypeDrp.setItemText(11, QCoreApplication.translate("CowabungaLite", u"5G", None))
        self.pTypeDrp.setItemText(12, QCoreApplication.translate("CowabungaLite", u"5G+", None))
        self.pTypeDrp.setItemText(13, QCoreApplication.translate("CowabungaLite", u"5GUW", None))
        self.pTypeDrp.setItemText(14, QCoreApplication.translate("CowabungaLite", u"5GUC", None))

        self.pStrengthChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Signal Strength", None))
        self.pStrengthLbl.setText(QCoreApplication.translate("CowabungaLite", u"0 Bars", None))
        self.label_10.setText(QCoreApplication.translate("CowabungaLite", u"Secondary Cellular", None))
        self.sDefaultRdo.setText(QCoreApplication.translate("CowabungaLite", u"Default", None))
        self.sShowRdo.setText(QCoreApplication.translate("CowabungaLite", u"Force Show", None))
        self.sHideRdo.setText(QCoreApplication.translate("CowabungaLite", u"Force Hide", None))
        self.sCarrierChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Carrier Text", None))
        self.sCarrierTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Carrier Text", None))
        self.sBadgeChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Service Badge Text", None))
        self.sBadgeTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Service Badge Text", None))
        self.sTypeChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Data Network Type", None))
        self.sTypeDrp.setItemText(0, QCoreApplication.translate("CowabungaLite", u"GPRS", None))
        self.sTypeDrp.setItemText(1, QCoreApplication.translate("CowabungaLite", u"EDGE", None))
        self.sTypeDrp.setItemText(2, QCoreApplication.translate("CowabungaLite", u"3G", None))
        self.sTypeDrp.setItemText(3, QCoreApplication.translate("CowabungaLite", u"4G", None))
        self.sTypeDrp.setItemText(4, QCoreApplication.translate("CowabungaLite", u"LTE", None))
        self.sTypeDrp.setItemText(5, QCoreApplication.translate("CowabungaLite", u"Wi-Fi", None))
        self.sTypeDrp.setItemText(6, QCoreApplication.translate("CowabungaLite", u"Personal Hotspot", None))
        self.sTypeDrp.setItemText(7, QCoreApplication.translate("CowabungaLite", u"1x", None))
        self.sTypeDrp.setItemText(8, QCoreApplication.translate("CowabungaLite", u"5G\u1d07", None))
        self.sTypeDrp.setItemText(9, QCoreApplication.translate("CowabungaLite", u"LTE-A", None))
        self.sTypeDrp.setItemText(10, QCoreApplication.translate("CowabungaLite", u"LTE+", None))
        self.sTypeDrp.setItemText(11, QCoreApplication.translate("CowabungaLite", u"5G", None))
        self.sTypeDrp.setItemText(12, QCoreApplication.translate("CowabungaLite", u"5G+", None))
        self.sTypeDrp.setItemText(13, QCoreApplication.translate("CowabungaLite", u"5GUW", None))
        self.sTypeDrp.setItemText(14, QCoreApplication.translate("CowabungaLite", u"5GUC", None))

        self.sStrengthChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Signal Strength", None))
        self.sStrengthLbl.setText(QCoreApplication.translate("CowabungaLite", u"0 Bars", None))
        self.timeChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Status Bar Time Text*", None))
        self.timeTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Status Bar Time Text", None))
        self.breadcrumbChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Breadcrumb Text", None))
        self.breadcrumbTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Breadcrumb Text", None))
        self.batteryDetailChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Battery Detail Text", None))
        self.batteryDetailTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Battery Detail Text", None))
        self.batteryCapacityChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Battery Icon Capacity", None))
        self.batteryCapacityLbl.setText(QCoreApplication.translate("CowabungaLite", u"0%", None))
        self.wifiStrengthChk.setText(QCoreApplication.translate("CowabungaLite", u"Change Wi-Fi Signal Strength", None))
        self.wifiStrengthLbl.setText(QCoreApplication.translate("CowabungaLite", u"0 Bars", None))
        self.numericWifiChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Numeric Wi-Fi Strength", None))
        self.numericCellChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Numeric Cellular Strength", None))
        self.label_5.setText(QCoreApplication.translate("CowabungaLite", u"*When set to blank on notched devices, this will display the carrier name.", None))
        self.hideDNDChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Do Not Disturb", None))
        self.hideAirplaneChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Airplane Mode", None))
        self.hideWifiChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Wi-Fi^", None))
        self.hideBatteryChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Battery", None))
        self.hideBluetoothChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Bluetooth", None))
        self.hideAlarmChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Alarm", None))
        self.hideLocationChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Location", None))
        self.hideRotationChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Rotation Lock", None))
        self.hideAirPlayChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide AirPlay", None))
        self.hideCarPlayChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide CarPlay", None))
        self.hideVPNChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide VPN", None))
        self.label_12.setText(QCoreApplication.translate("CowabungaLite", u"^Will also hide cellular data indicator.", None))
        self.customOperationsLbl.setText(QCoreApplication.translate("CowabungaLite", u"Custom Operations", None))
        self.label_14.setText("")
        self.importOperationBtn.setText(QCoreApplication.translate("CowabungaLite", u"  Import .cowperation", None))
        self.newOperationBtn.setText(QCoreApplication.translate("CowabungaLite", u"  New Operation", None))
        self.springboardOptionsLbl.setText(QCoreApplication.translate("CowabungaLite", u"Springboard Options", None))
        self.springboardOptionsEnabledChk.setText(QCoreApplication.translate("CowabungaLite", u"Modify", None))
        self.label_8.setText(QCoreApplication.translate("CowabungaLite", u"UI Animation Speed", None))
        self.UIAnimSpeedLbl.setText(QCoreApplication.translate("CowabungaLite", u"1 (Default)", None))
        self.label_13.setText(QCoreApplication.translate("CowabungaLite", u"Lock Screen Footnote Text", None))
        self.footnoteTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Footnote Text", None))
        self.disableLockRespringChk.setText(QCoreApplication.translate("CowabungaLite", u"Disable Lock After Respring", None))
        self.disableDimmingChk.setText(QCoreApplication.translate("CowabungaLite", u"Disable Screen Dimming While Charging", None))
        self.disableBatteryAlertsChk.setText(QCoreApplication.translate("CowabungaLite", u"Disable Low Battery Alerts", None))
        self.disableCrumbChk.setText(QCoreApplication.translate("CowabungaLite", u"Disable Breadcrumbs", None))
        self.enableSupervisionTextChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Supervision Text on Lock Screen", None))
        self.enableWiFiDebuggerChk.setText(QCoreApplication.translate("CowabungaLite", u"Show WiFi Debugger", None))
        self.enableShutdownSoundChk.setText(QCoreApplication.translate("CowabungaLite", u"Play Sound on Shutdown", None))
        self.allowAirDropEveryoneChk.setText(QCoreApplication.translate("CowabungaLite", u"Permanently Allow Receiving AirDrop from Everyone", None))
        self.internalOptionsLbl.setText(QCoreApplication.translate("CowabungaLite", u"Internal Options", None))
        self.internalOptionsEnabledChk.setText(QCoreApplication.translate("CowabungaLite", u"Modify", None))
        self.buildVersionChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Build Version in Status Bar", None))
        self.RTLChk.setText(QCoreApplication.translate("CowabungaLite", u"Force Right-to-Left Layout", None))
        self.metalHUDChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable Metal HUD Debug", None))
        self.accessoryChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable Accessory Developer", None))
        self.iMessageChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable iMessage Debugging", None))
        self.IDSChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable Continuity Debugging", None))
        self.VCChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable FaceTime Debugging", None))
        self.appStoreChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable App Store Debug Gesture", None))
        self.notesChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable Notes Debug Mode", None))
        self.showTouchesChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Touches With Debug Info", None))
        self.hideRespringChk.setText(QCoreApplication.translate("CowabungaLite", u"Hide Respring Icon", None))
        self.enableWakeVibrateChk.setText(QCoreApplication.translate("CowabungaLite", u"Vibrate on Raise-to-Wake", None))
        self.pasteSoundChk.setText(QCoreApplication.translate("CowabungaLite", u"Play Sound on Paste", None))
        self.notifyPastesChk.setText(QCoreApplication.translate("CowabungaLite", u"Show Notifications for System Pastes", None))
        self.setupOptionsLbl.setText(QCoreApplication.translate("CowabungaLite", u"Setup Options", None))
        self.setupOptionsEnabledChk.setText(QCoreApplication.translate("CowabungaLite", u"Modify", None))
        self.skipSetupChk.setText(QCoreApplication.translate("CowabungaLite", u"Skip Setup (Recommended)", None))
        self.enableSupervisionChk.setText(QCoreApplication.translate("CowabungaLite", u"Enable Supervision", None))
        self.organizationNameTxt.setPlaceholderText(QCoreApplication.translate("CowabungaLite", u"Organization Name", None))
        self.statusBarLbl_5.setText(QCoreApplication.translate("CowabungaLite", u"Apply", None))
        self.label_16.setText("")
        self.label_6.setText(QCoreApplication.translate("CowabungaLite", u"Modified Tweaks:", None))
        self.enabledTweaksLbl.setText(QCoreApplication.translate("CowabungaLite", u"None", None))
        self.applyTweaksBtn.setText(QCoreApplication.translate("CowabungaLite", u"  Apply Changes", None))
        self.statusLbl.setText(QCoreApplication.translate("CowabungaLite", u"Ready!", None))
        self.removeTweaksBtn.setText(QCoreApplication.translate("CowabungaLite", u"Remove All Tweaks", None))
        self.deepCleanBtn.setText(QCoreApplication.translate("CowabungaLite", u"Deep Clean", None))
    # retranslateUi

