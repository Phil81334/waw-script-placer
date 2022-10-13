########################################################################
## START

# AUTHOR: -Phil81334
# COMMUNITY: CME (CoD Modding Elite)
# DESCRIPTION: WaW Custom Zombie's Script Placer

## END
############################## ---/--/--- ##############################

########################################################################
## START - ADD TO: ui_mainWindow.py

r"""
from os.path import join, dirname, realpath

import level

# Replace: self.headerFrame = QFrame(self.centralwidget)
# With: self.headerFrame = SubClassQFrame(MainWindow)
class SubClassQFrame(QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.clickedOnHeader = False

    def mousePressEvent(self, event):
        self.MainWindow.oldPosition = event.globalPos()
        self.clickedOnHeader = True

    def mouseReleaseEvent(self, event):
        self.clickedOnHeader = False

    def mouseMoveEvent(self, event):
        if self.clickedOnHeader is True:
            delta = QPoint(event.globalPos() - self.MainWindow.oldPosition)
            self.MainWindow.move(self.MainWindow.x() + delta.x(), self.MainWindow.y() + delta.y())
            self.MainWindow.oldPosition = event.globalPos()

# Replace: u":/icons/icons/minus.svg"
# with: join(dirname(realpath(__file__)), "icons/minus.svg")

# Replace: u":/icons/icons/x.svg"
# with: join(dirname(realpath(__file__)), "icons/x.svg")

# Replace: u":/icons/icons/discord.png"
# With: join(dirname(realpath(__file__)), "icons/discord.png")

# Replace: u":/icons/icons/logo_64x64.png"
# With: join(dirname(realpath(__file__)), "icons/logo_64x64.png")

# Replace: u":/icons/icons/youtubeV3.png"
# With: join(dirname(realpath(__file__)), "icons/youtubeV3.png")

# Replace:
# With:
# src=\":/images/images/mainMenuScreen.png\"
# src=\'{join(dirname(realpath(__file__)), 'images/mainMenuScreen.png')}\'

# src=\":/images/images/pauseScreenMaterial.png\"
# src=\'{join(dirname(realpath(__file__)), 'images/pauseScreenMaterial.png')}\'

# src=\":/images/images/loadScreenImage.png\"
# src=\'{join(dirname(realpath(__file__)), 'images/loadScreenImage.png')}\'

# src=\":/images/images/missionScreenImage.png\"
# src=\'{join(dirname(realpath(__file__)), 'images/missionScreenImage.png')}\'
"""

## END - ADD TO: ui_mainWindow.py
############################## ---/--/--- ##############################

########################################################################
## START - IMPORT MODULES

# This Python file uses the following encoding: utf-8
from os import remove, walk, listdir, chmod, mkdir
from os.path import isfile, exists, join, dirname, realpath, expanduser, isdir

from PySide6.QtCore import Qt, QRect, QTimer, QPoint, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame

# open cmd. enter: cd <.ui path>. enter: pyuic5 -x form.ui -o ui_form.py
from ui_form import Ui_MainWindow

# open cmd. enter: cd <.qrc path>. enter: pyrcc5 _icons.qrc -o _icons.py
# open cmd. enter: cd <.qrc path>. enter: pyrcc5 _images.qrc -o _images.py
import icons, images, level

import sys, webbrowser, re, contextlib, time

from logic import Logic

from datetime import datetime
from threading import Thread

from stat import S_IREAD, S_IWUSR
# disable "read-only" on directory file
# chmod(DIRECTORIES_FILE_DIR, S_IWUSR)

# enable "read-only"
# chmod(DIRECTORIES_FILE_DIR, S_IREAD)

## END - IMPORT MODULES
############################## ---/--/--- ##############################

########################################################################
## START - MISC

# use this line for testing
# root_dir = dirname(realpath(__file__))
# print(f"root_dir: {root_dir}")

# use this line when packing into an exe
# root_dir = "./"

## END - MISC
############################## ---/--/--- ##############################

########################################################################
## START - MainWindow CLASS

class MainWindow(QMainWindow):

    ########################################################################
    ## START - __init__ - METHOD

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # advanced mode - hide it to start with
        self.ui.advancedFrame.hide()
        self.resize(self.width(), 421)

        # handles minimising the main window and the custom mystery box window(if open)
        self.ui.minimiseBtn.clicked.connect(self.miniseWindows)
        self.ui.closeBtn.clicked.connect(lambda e: self.close())

        # this handles bringing up the custom mystery box window when user clicks on the minimised main window from taskbar
        self.timer = QTimer()
        # milliseconds (1000 = 1 second | 100 = 0.1 seconds)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.check_state)
        self.timer.start()

        level.DATE_TIME_LABEL = self.ui.dateTimeLabel
        level.DATE_TIME_LABEL.setText('')

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # hide custom menu button text box. we'll unhide it if user chooses this option via checkbox
        self.ui.custBtnNameTextBox.hide()
        # watch for value change
        self.ui.mainMenuBtnCheckBox.stateChanged.connect(self.mainMenuStateChanged)

        # hide custom .map file option. we'll unhide it if user chooses this option via radiobtn
        self.ui.custMapFileTextBox.hide()
        # btn to select dir
        self.ui.toolButton_5.hide()
        # watch for value change
        self.ui.customMap.toggled.connect(self.customMapStateChanged)

        # hide mini-map text box. we'll unhide it if user chooses this option via checkbox
        self.ui.miniMapTextBox.hide()
        self.ui.toolButton_7.hide()

        # watch for value change
        self.ui.addMiniMapCheckBox.stateChanged.connect(self.miniMapStateChanged)

        # fov
        self.ui.FovSlider.valueChanged.connect(self.fovSlider)

        # CME <discord>, <website> & <youtube> hyperlink buttons
        self.ui.discordBtn.clicked.connect(lambda: self.hyperlink("https://discord.gg/w6v6HuFRYD"))
        self.ui.websiteBtn.clicked.connect(lambda: self.hyperlink("https://cme-mods.com/"))
        self.ui.youtubeBtn.clicked.connect(lambda: self.hyperlink("https://www.youtube.com/channel/UC1q44w1Zs1c5xABRjzjj1xA"))
        # NAKSHATRA_12 & UGX Discord
        self.ui.commandLinkButton_2.clicked.connect(lambda: self.hyperlink("https://discord.gg/2BhUg5knkm"))
        self.ui.commandLinkButton.clicked.connect(lambda: self.hyperlink("https://discord.gg/ZkJSfwn62F"))

        ########################################################################
        ## START - Logic - CLASS

        self.logic = Logic(self)

        ## END - Logic - CLASS
        ############################## ---/--/--- ##############################

    ## END - __init__ - METHOD
    ############################## ---/--/--- ##############################

    # Moves MainWindow From Any Point
    # def mousePressEvent(self, event):
    #     self.oldPos = event.globalPos()

    # def mouseMoveEvent(self, event):
    #     delta = QPoint (event.globalPos() - self.oldPos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.oldPos = event.globalPos()

    ########################################################################
    ## START - miniseWindows - METHOD

    def miniseWindows(self):
        if not self.isMinimized():
            self.showMinimized()
            try:
                self.w.showMinimized()
            except:
                pass

    ## END - miniseWindows - METHOD
    ############################## ---/--/--- ##############################

    def check_state(self):
        # if main window is not minimised
        if not self.windowState() == Qt.WindowMinimized:
            # check if second window is minimised.
            # if it is, then restore it.
            try:
                if self.w.windowState() == Qt.WindowMinimized:
                    self.w.setWindowState(Qt.WindowNoState)
            except:
                pass

    ########################################################################
    ## START - mainMenuStateChanged - METHOD

    def mainMenuStateChanged(self):
        if self.ui.mainMenuBtnCheckBox.isChecked():
            self.ui.custBtnNameTextBox.show()
        else:
            if self.ui.custBtnNameTextBox.text():
                self.ui.custBtnNameTextBox.setText("")
            self.ui.custBtnNameTextBox.hide()

    ## END - mainMenuStateChanged - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - customMapStateChanged - METHOD

    def customMapStateChanged(self):
        if self.ui.customMap.isChecked():
            self.ui.custMapFileTextBox.show()
            self.ui.toolButton_5.show()
        else:
            if self.ui.custMapFileTextBox.text():
                self.ui.custMapFileTextBox.setText("")
            self.ui.custMapFileTextBox.hide()
            self.ui.toolButton_5.hide()

    ## END - customMapStateChanged - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - miniMapStateChanged - METHOD

    def miniMapStateChanged(self):
        if self.ui.addMiniMapCheckBox.isChecked():
            self.ui.miniMapTextBox.show()
            self.ui.toolButton_7.show()
        else:
            if self.ui.miniMapTextBox.text():
                self.ui.miniMapTextBox.setText("")
            self.ui.miniMapTextBox.hide()
            self.ui.toolButton_7.hide()

    ## END - miniMapStateChanged - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - fovSlider - METHOD

    def fovSlider(self):
        self.ui.label.setText(f"FOV: {str(self.ui.FovSlider.value())}")

    ## END - fovSlider - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - hyperlink - METHOD

    def hyperlink(self, url):
        try: webbrowser.open_new(url)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Failure, Please check your internet connection")
            msg.exec()
            pass

    ## END - hyperlink - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - closeEvent - METHOD - this is a stock method. just adding to it.

    def closeEvent(self, event):
        msgBox = QMessageBox(QMessageBox.Question, 'Shut Down No-T4M', 'Are you sure you want exit?', buttons=QMessageBox.Yes | QMessageBox.No, parent=self)
        msgBox.setWindowFlags(Qt.FramelessWindowHint)
        msgBox.setGeometry(QRect(200, 150, 0, 0))
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.setStyleSheet("background-color: black; color: red; font-size: 10pt; font-family: Courier New;") #border: 1px solid yellow;
        msgBox.exec()
        reply = msgBox.standardButton(msgBox.clickedButton())
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    ## END - closeEvent - METHOD
    ############################## ---/--/--- ##############################

## END - MainWindow CLASS
############################## ---/--/--- ##############################

########################################################################
## START - threadUpdateDateTime FUNCTION

def threadUpdateDateTime():
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        level.DATE_TIME_LABEL.setText(dt_string)
        time.sleep(1)

def updateDateTime():
    new_thread = Thread(target=threadUpdateDateTime)
    new_thread.start()

## END - threadUpdateDateTime FUNCTION
############################## ---/--/--- ##############################

########################################################################
## START - setWawDir FUNCTION

def setWawDir(self, app):

    # get current dir the program resides
    # dir = dirname(realpath(__file__))
    # dir = "./"
    # testing purposes
    dir = r"E:\SteamLibrary\steamapps\common\Call of Duty World at War"

    # ensure its in the waw root dir
    if "Call of Duty World at War" not in dir:
        # inform user they selected the wrong game
        QMessageBox.about(self, "WARNING", f"Current .exe directory:\n{dir}\n\nEnsure you place the .exe in a 'Call of Duty: World at War' root directory.")
        try:
            sys.exit(app.exec())
        except SystemExit:
            print('Closing app')

    level.WAW_ROOT_DIR = dir

## END - setWawDir FUNCTION
############################## ---/--/--- ##############################

########################################################################
## START - INITIALISE PROGRAM

if __name__ == "__main__":
    print('Starting app')
    app = QApplication(sys.argv)
    window = MainWindow()
    updateDateTime()
    setWawDir(window, app)
    window.show()
    try: sys.exit(app.exec())
    except SystemExit: print('Closing app')

## END - INITIALISE PROGRAM
############################## ---/--/--- ##############################