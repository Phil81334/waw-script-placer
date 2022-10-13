########################################################################
## START - IMPORT MODULES

import os, sys, level, time, random, subprocess
from os import walk, rename, listdir, mkdir, remove, rmdir
from os.path import join, isdir, dirname, realpath, isfile, split, expanduser

from PySide6.QtCore import Qt, QRect, QObject, QPoint, QSize
from PySide6.QtGui import QColor, QScreen
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox, QColorDialog, QStyleFactory, QFileDialog, QComboBox, QVBoxLayout, QWidget, QLabel, QApplication, QSizePolicy

from shutil import copytree, copyfile, move, rmtree
from contextlib import suppress

## END - IMPORT MODULES
############################## ---/--/--- ##############################

########################################################################
## START - MISC

# Open Folder
# FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

# path = join(expanduser('~\AppData'), r"Local\Activision\CoDWaW\mods")
# def explore(path):
#     # explorer would choke on forward slashes
#     path = os.path.normpath(path)

#     if os.path.isdir(path):
#         subprocess.run([FILEBROWSER_PATH, path])
#     elif os.path.isfile(path):
#         subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

## END - MISC
############################## ---/--/--- ##############################

########################################################################
## START - Logic - CLASS

class Logic(QObject):

    ########################################################################
    ## START - __init__ - METHOD

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow

        ##
        ## WIDGET SIGNALS
        ##

        # create map btn
        self.MainWindow.ui.createMapbtn.clicked.connect(self.createMapChecks)

        # delete map
        self.MainWindow.ui.deleteMapBtn.clicked.connect(self.deleteMap)

        # advanced mode (show more options)
        self.MainWindow.ui.advModeBtn.clicked.connect(self.advancedMode)

        # get path for required file
        self.MainWindow.ui.toolButton_5.clicked.connect(lambda: self.addPathToTextBox("customMap"))
        self.MainWindow.ui.toolButton_7.clicked.connect(lambda: self.addPathToTextBox("miniMap"))
        self.MainWindow.ui.toolButton.clicked.connect(lambda: self.addPathToTextBox("vision"))
        self.MainWindow.ui.toolButton_2.clicked.connect(lambda: self.addPathToTextBox("mainMenuScreen"))
        self.MainWindow.ui.toolButton_3.clicked.connect(lambda: self.addPathToTextBox("PauseScreen"))
        self.MainWindow.ui.toolButton_4.clicked.connect(lambda: self.addPathToTextBox("loadScreen"))
        self.MainWindow.ui.toolButton_6.clicked.connect(lambda: self.addPathToTextBox("missionScreen"))

        # mystery box
        self.MainWindow.ui.customBoxSetup.toggled.connect(self.mysteryBoxStateChanged)

    ## END - __init__ - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - createMapChecks - METHOD

    def createMapChecks(self):

        # Has user enterted a mapname?
        if not self.MainWindow.ui.mapnameTextBox.text().strip():
            QMessageBox.about(self.MainWindow, "WARNING", "Ensure you add a 'Map Name'.")
            return

        # Does mapname exist?
        self.mapName = self.MainWindow.ui.mapnameTextBox.text().strip()
        if self.mapnameExists():
            QMessageBox.about(self.MainWindow, "WARNING", self.mapnameErrorMsg)
            return

        # Symbols in mapname?
        if '-' in self.mapName:
            QMessageBox.about(self.MainWindow, "WARNING", "Can only use letters, numbers and underscores in your map name.")
            return

        # Has user enabled 'Custom .map' option?
        # If so, have they entered said dir?
        if self.MainWindow.ui.customMap.isChecked():
            if self.MainWindow.ui.custMapFileTextBox.text().strip():
                path = self.MainWindow.ui.custMapFileTextBox.text().strip()
                if not isfile(path):
                    QMessageBox.about(self.MainWindow, "WARNING", f"{path} - is not a file.")
                    return
                if not path.endswith(".map"):
                    QMessageBox.about(self.MainWindow, "WARNING", f"{path} - is not a .map file.")
                    return
                self.CustomMapFilePath = path
            else:
                QMessageBox.about(self.MainWindow, "WARNING", "You forgot to add a .map file.")
                return

        # Mini Map
        # Has user enabled 'Mini Map' option?
        # If so, have they entered the mini map material file dir?
        if self.MainWindow.ui.addMiniMapCheckBox.isChecked():
            if self.MainWindow.ui.miniMapTextBox.text().strip():
                self.miniMapMaterialFilePath = self.MainWindow.ui.miniMapTextBox.text().strip()
                # make sure its an actual file
                if not self.fileCheck(self.miniMapMaterialFilePath, "raw/materials", "Mini Map"):
                    return

        # Has user enabled 'Custom Menu Button Text'?
        # If so, have they entered said text?
        if self.MainWindow.ui.mainMenuBtnCheckBox.isChecked():
            if self.MainWindow.ui.custBtnNameTextBox.text().strip():
                self.CustomMenuButtonText = self.MainWindow.ui.custBtnNameTextBox.text().strip()
            else:
                QMessageBox.about(self.MainWindow, "WARNING", "You forgot to add the Custom Button Text.")
                return

        # vision file
        if self.MainWindow.ui.usingCustomVisionFile.isChecked():
            if not self.MainWindow.ui.visionFileTextBox.text().strip():
                QMessageBox.about(self.MainWindow, "WARNING", "You selected the 'Custom vision' option but forgot to add a vision file")
                return
        else:
            if self.MainWindow.ui.visionFileTextBox.text().strip():
                visionFilepath = self.MainWindow.ui.visionFileTextBox.text().strip()
                if isfile(visionFilepath):
                    self.visionFile = self.MainWindow.ui.visionFileTextBox.text().strip()
                else:
                    QMessageBox.about(self.MainWindow, "WARNING", "vision file does not exist")
                    return

        # Main Menu Screen Material File Path
        if self.MainWindow.ui.mainMenuMaterial.text().strip():
            self.mainMenuScreenmaterialPath = self.MainWindow.ui.mainMenuMaterial.text().strip()
            if not self.fileCheck(self.mainMenuScreenmaterialPath, "raw/materials", "Main Menu Screen"):
                return

        # Pause Screen Material File Path
        if self.MainWindow.ui.pauseScreenMaterial.text().strip():
            self.pauseScreenMaterialFilePath = self.MainWindow.ui.pauseScreenMaterial.text().strip()
            if not self.fileCheck(self.pauseScreenMaterialFilePath, "raw/materials", 'Pause Screen'):
                return
            materialName = self.pauseScreenMaterialFilePath.split('/')[-1]
            if materialName != f"menu_map_{self.mapName}":
                QMessageBox.about(self.MainWindow, "WARNING", f'The `Pause Screen Image` feature requires the material name to be labelled: menu_map_{self.mapName}')
                return

        # Load Screen Material File Path
        if self.MainWindow.ui.loadScreenImage.text().strip():
            self.loadScreenMaterialFilePath = self.MainWindow.ui.loadScreenImage.text().strip()
            if not self.fileCheck(self.loadScreenMaterialFilePath, "raw/materials", 'Load Screen'):
                return
            materialName = self.loadScreenMaterialFilePath.split('/')[-1]
            if materialName != f"loadscreen_{self.mapName}":
                QMessageBox.about(self.MainWindow, "WARNING", f'The `Load Screen Image` feature requires the material name to be labelled: loadscreen_{self.mapName}')
                return

        # Mission Screen Material File Path
        if self.MainWindow.ui.missionScreenImage.text().strip():
            self.missionScreenMaterialFilePath = self.MainWindow.ui.missionScreenImage.text().strip()
            if not self.fileCheck(self.missionScreenMaterialFilePath, "raw/materials", 'Mission Screen'):
                return
            materialName = self.missionScreenMaterialFilePath.split('/')[-1]
            if materialName != f"mission_screen_{self.mapName}":
                QMessageBox.about(self.MainWindow, "WARNING", f'The `Mission Screen Image` feature requires the material name to be labelled: mission_screen_{self.mapName}')
                return

        # Starting Weapon
        if self.MainWindow.ui.startWeap.text().strip():
            self.startingWeaponName = self.MainWindow.ui.startWeap.text().strip()
            path = join(level.WAW_ROOT_DIR, fr"raw\weapons\sp\{self.startingWeaponName}")
            if not self.fileCheck(path, r"raw\weapons\sp", "Starting Weapon"):
                return

        # Switch Weapon
        if self.MainWindow.ui.switchWeap.text().strip():
            self.switchWeaponName = self.MainWindow.ui.switchWeap.text().strip()
            path = join(level.WAW_ROOT_DIR, fr"raw\weapons\sp\{self.switchWeaponName}")
            if not self.fileCheck(path, r"raw\weapons\sp", "Switch Weapon"):
                return

        # Laststand Weapon
        if self.MainWindow.ui.laststandWeap.text().strip():
            self.laststandWeaponName = self.MainWindow.ui.laststandWeap.text().strip()
            # join(var_path, string_path)
            # join() adds forward slashes to var_path
            path = join(level.WAW_ROOT_DIR, fr"raw\weapons\sp\{self.laststandWeaponName}")
            if not self.fileCheck(path, r"raw\weapons\sp", "Laststand Weapon"):
                return

        self.createMap()

        if not self.MainWindow.ui.stockBoxSetup.isChecked():
            self.MainWindow.ui.stockBoxSetup.setChecked(True)

        try:
            self.MainWindow.w.deleteLater()
        except:
            pass

    ## END - createMapChecks - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - createMap - METHOD

    def createMap(self):

        level.FINAL_MESSAGE = []

        # TEMPLATE FILES
        if self.MainWindow.ui.prototypeMap.isChecked():
            sourceDir = join(dirname(realpath(__file__)), "prototype files")
        elif self.MainWindow.ui.asylumMap.isChecked():
            sourceDir = join(dirname(realpath(__file__)), "asylum files")
        elif self.MainWindow.ui.sumpfMap.isChecked():
            sourceDir = join(dirname(realpath(__file__)), "sumpf files")
        elif self.MainWindow.ui.factoryMap.isChecked():
            sourceDir = join(dirname(realpath(__file__)), "factory files")
        elif self.MainWindow.ui.allInOneMap.isChecked():
            sourceDir = join(dirname(realpath(__file__)), "custom files")

        # shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

        # [1] = copy template tree to a new folder in waw root directory
        # [2] - rename all folders, file names and file contents containing mapname mentions
        # [3] - iterate through any files that require changes to be made via the users choices
        # [4] = remove any uneeded files((as all template files get copied over to target folder) - (totally based on user choices))
        # [5] - copy edited tree to waw's respective folders
        # [6] - delete the folder from step 1

        # [1]
        original = join(sourceDir)
        target = join(level.WAW_ROOT_DIR, f"{self.mapName}_Temp_Script_Placer_Folder")
        try:
            copytree(original, target)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            QMessageBox.about(  self.MainWindow, "ERROR",
                                f"Exc Type: {exc_type}\n\n"
                                f"Exc Object: {exc_obj}\n\n"
                                f"File Name: {fname}\n\n"
                                f"Line Number: {exc_tb.tb_lineno}"  )
            return

        # [2]
        for root, folders, files in walk(target):
            for name in folders:
                oldFolderName = join(root, name)
                newFolderName = oldFolderName.replace("CHANGE_TO_MAPNAME", self.mapName)
                # rename folder
                rename(oldFolderName, newFolderName)

        for root, folders, files in walk(target):
            for name in files:
                oldFileName = join(root, name)
                newFileName = oldFileName.replace("CHANGE_TO_MAPNAME", self.mapName)
                # rename file
                rename(oldFileName, newFileName)
                # replace 'mapname mentions' inside file
                self.replaceOriginalCodeLine(newFileName, "CHANGE_TO_MAPNAME", self.mapName, False)

        # [3]:
        # [3.1]: Custom Main Menu Button Text
        self.customMainMenuButtonText(target)

        # [3.2]: Fog
        self.fog(target)

        # [3.3]: Vision
        self.vision(target)

        # [3.4]: Mini Map
        self.miniMap(target)

        # [3.5]: FOV
        self.fov(target)

        # [3.6]: .map files
        self.mapSource(target)

        # [3.7]: Main Menu Screen
        self.mainMenuScreen(target)

        # [3.8]: Pause Screen
        self.pauseScreen(target)

        # [3.9]: Load Screen
        self.loadScreen(target)

        # [3.9.1]: Mission Screen
        self.missionScreen(target)

        # [3.9.2]: Starting Weapon
        self.startingWeapon(target)

        # [3.9.3]: Switch Weapon
        self.switchWeapon(target)

        # [3.9.4]: Laststand Weapon
        self.laststandWeapon(target)

        # [3.9.5]: Score
        self.setPlayerScore(target)

        # [3.9.6]: Mystery Box
        self.mysteryBoxSetup(target)

        # [4]
        self.deleteUnneededFiles(target)

        # [5]
        try:
            copytree(target, level.WAW_ROOT_DIR, dirs_exist_ok=True)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = split(exc_tb.tb_frame.f_code.co_filename)[1]
            QMessageBox.about(self.MainWindow, "ERROR",
                              f"Exc Type: {exc_type}\n"
                              f"Exc Object: {exc_obj}\n"
                              f"File Name: {fname}\n"
                              f"Line Number: {exc_tb.tb_lineno}")

        # [6]
        rmtree(target)

        level.FINAL_MESSAGE.append(f"Successfully created: {self.mapName}\nCompile map & _patch, Build mod, Run game. Enjoy!")
        level.FINAL_MESSAGE.reverse()
        QMessageBox.about(self.MainWindow, "WARNING", ''.join(level.FINAL_MESSAGE))

    ## END - createMap - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - customMainMenuButtonText - METHOD

    def customMainMenuButtonText(self, target):

        if self.MainWindow.ui.mainMenuBtnCheckBox.isChecked():
            path = join(target, fr"raw\ui\{self.mapName}_main.menu")
            old = 'CHOICE_BUTTON_VIS( 1, "@MENU_SOLO_CAP", SETUP_ACTION_SOLO; LOCAL_ZOMBIE_RESET, when( !localvarBool( ui_hideBack ) ); )'
            new = f'CHOICE_BUTTON_VIS( 1, "{self.CustomMenuButtonText}", exec "map {self.mapName}", when( !localvarBool( ui_hideBack ) ); )'
            self.replaceOriginalCodeLine(path, old, new, True)

            # mod.csv
            path = join(target, f"mods\{self.mapName}\mod.csv")
            with open(path, "a+", encoding="ISO-8859-1") as file:
                file.seek(0)
                data = file.read()
                if len(data) > 0:
                    file.write("\n")
                file.write('// Custom Main Menu Start Button\n'
                           f'menufile,ui/{self.mapName}_main.menu')

    ## END - customMainMenuButtonText - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - fog - METHOD

    def fog(self, target):

        if not self.MainWindow.ui.enableFogCheckBox.isChecked():
            path = join(target, f"mods\{self.mapName}\maps\createart\{self.mapName}_art.gsc")

            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_exp_halfplane", "835");',   '// setdvar("scr_fog_exp_halfplane", "835");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_exp_halfheight", "200");',  '// setdvar("scr_fog_exp_halfheight", "200");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_nearplane", "165");',       '// setdvar("scr_fog_nearplane", "165");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_red", "0.5");',             '// setdvar("scr_fog_red", "0.5");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_green", "0.5");',           '// setdvar("scr_fog_green", "0.5");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_blue", "0.5");',            '// setdvar("scr_fog_blue", "0.5");', True)
            self.replaceOriginalCodeLine(path, 'setdvar("scr_fog_baseheight", "50");',       '// setdvar("scr_fog_baseheight", "50");', True)
            self.replaceOriginalCodeLine(path, "level thread fog_settings();",               "// level thread fog_settings();", True)

    ## END - fog - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - vision - METHOD

    def vision(self, target):

        visionPath = self.MainWindow.ui.visionFileTextBox.text().strip()
        if visionPath:
            # aftermath_blue
            visionName = visionPath.split('/')[-1].split('.')[0]
            # aftermath_blue.vision
            visionFile = visionPath.split('/')[-1].strip()
            # zone_source -> mapname.csv
            path = join(target, f"zone_source\{self.mapName}.csv")
            self.replaceOriginalCodeLine(path, 'rawfile,vision/zombie.vision', f'rawfile,vision/{visionFile}', True)
            # mods -> mapname -> maps -> createart -> mapname_art.gsc
            path = join(target, f"mods\{self.mapName}\maps\createart\{self.mapName}_art.gsc")
            self.replaceOriginalCodeLine(path, 'level thread maps\_utility::set_all_players_visionset( "zombie", 0.1 );', f'level thread maps\_utility::set_all_players_visionset( "{visionName}", 0.1 );', True)
            # if custom option is enabled
            if self.MainWindow.ui.usingCustomVisionFile.isChecked():
                # mods -> mapname -> mod.csv
                path = join(target, f"mods\{self.mapName}\mod.csv")
                with open(path, "a", encoding="ISO-8859-1") as file:
                    file.seek(0)
                    data = file.read()
                    if len(data) > 0:
                        file.write("\n")
                    file.write(f"\nrawfile,vision/{visionFile}")
                # create vision folder and place custom vision file in it
                visionFolder = join(target, fr"mods\{self.mapName}\vision")
                mkdir(visionFolder)
                copyfile(visionPath, join(target, fr"mods\{self.mapName}\vision\{visionFile}"))

    ## END - vision - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - miniMap - METHOD

    def miniMap(self, target):

        if self.MainWindow.ui.addMiniMapCheckBox.isChecked():
            materialName = self.miniMapMaterialFilePath.split('/')[-1]

            # mapname.gsc
            path = join(target, f"mods\{self.mapName}\maps\{self.mapName}.gsc")
            with open(path, "r", encoding="ISO-8859-1") as inFile:
                buf = inFile.readlines()
            powerupsIdentifier = False
            soundsIdentifier = False
            endOfMain = False
            with open(path, "w", encoding="ISO-8859-1") as outFile:
                for line in buf:
                    if line.strip() == "include_powerups();" and not powerupsIdentifier:
                        line = line + f'\n    //precache mini map shader\n    miniMapMaterial = "{materialName}";\n    precacheShader(miniMapMaterial);\n'
                        powerupsIdentifier = True
                    elif line.strip() == "init_sounds();" and not soundsIdentifier:
                        soundsIdentifier = True
                        line = line + '\n    maps\_compass::setupMiniMap(miniMapMaterial);\n\n    dist = distance(getentarray("minimap_corner", "targetname")[0].origin, getentarray("minimap_corner", "targetname")[1].origin);\n    maps\_cme_utility::pass_players(true, ::miniMap, 1, (dist/2), undefined, false);\n'
                    elif line.strip() == "}" and not endOfMain:
                        endOfMain = True
                        line = line + '\nminiMap(param1, param2) {\n\n    // 0 disable, 1 enable\n    self setClientDvar("enable_minimap", param1);\n    self setClientDvar("compassmaxrange", param2);\n}\n'
                    outFile.write(line)

            # edit hud.menu
            # Add mini map #include line to hud.menu (if not already there)
            path = join(level.WAW_ROOT_DIR, r"raw/ui/hud.menu")
            with open(path, 'r', encoding="ISO-8859-1") as file:
                hudContent = file.read()
                if "#include ui/minimap_cod5_nakshatra_12.inc" not in hudContent:
                    # bring file back to 1st line
                    file.seek(0)
                    with open(path, "r", encoding="ISO-8859-1") as file:
                        list_of_lines = file.readlines()
                        for i in range(len(list_of_lines)):
                            if list_of_lines[i].strip() == '{':
                                list_of_lines[i] = list_of_lines[i] + '\n	#include "ui/minimap_cod5_nakshatra_12.inc"\n'
                                break
                    with open(path, "w", encoding="ISO-8859-1") as file:
                        file.writelines(list_of_lines)

            # mod.csv
            list = [
                "// Mini Map Screen",
                f"material,{materialName}",
                "menufile,ui/hud.txt",
                "menufile,ui/hud.menu"
            ]
            self.addmaterialCallAndMoveIwi(target, join(target, f"mods\{self.mapName}\mod.csv"), list, "Mini Map Screen", materialName)

    ## END - miniMap - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - fov - METHOD

    def fov(self, target):

        if self.MainWindow.ui.FovSlider.value() != 65:
            fovValue = self.MainWindow.ui.FovSlider.value()
            path = join(target, f"mods\{self.mapName}\maps\_zombiemode.gsc")

            old = '"cg_fov", "65"'
            x = f'\n"cg_fovMin", "{fovValue}",\n'
            y = f'\n"cg_fovMin", "{fovValue}" );\n'
            with open(path, "r", encoding="ISO-8859-1") as file:
                old = old.strip()
                temp = file.read()
                if old not in temp:
                    QMessageBox.about(self.MainWindow, "WARNING", "Failed to add Fov. Report this to the Author.")
                    return

                file.seek(0)
                listOfLines = file.readlines()
                for i in range(len(listOfLines)):
                    if old in listOfLines[i].strip():
                        if ");" not in listOfLines[i]:
                            listOfLines[i] = listOfLines[i].replace("65", str(fovValue)).strip() + x
                        elif ");" in listOfLines[i]:
                            listOfLines[i] = f'"cg_fov", "{fovValue}", {y}'

            with open(path, "w", encoding="ISO-8859-1") as file:
                file.writelines(listOfLines)

    ## END - fov - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - mapSource - METHOD

    def mapSource(self, target):

        # using Custom .map file so delete the blank and setup templates that were copied over
        if self.MainWindow.ui.customMap.isChecked():
            blank = join(target, f"map_source\{self.mapName}_blank.map")
            setup = join(target, f"map_source\{self.mapName}_setup.map")
            remove(blank)
            remove(setup)
            # Copy custom .map file contents and place in new file
            original = self.CustomMapFilePath
            target = join(level.WAW_ROOT_DIR, f"map_source\{self.mapName}.map")
            copyfile(original, target)
        # using Setup file so delete the blank template that was copied over
        elif self.MainWindow.ui.setupMapRadioBtn.isChecked():
            blank = join(target, f"map_source\{self.mapName}_blank.map")
            remove(blank)
            # rename setup - just removing the '_setup' suffix
            old = join(target, f"map_source\{self.mapName}_setup.map")
            new = join(target, f"map_source\{self.mapName}.map")
            rename(old, new)
        # using Blank file so delete the setup template that was copied over
        if self.MainWindow.ui.blankMapRadioBtn.isChecked():
            setup = join(target, f"map_source\{self.mapName}_setup.map")
            remove(setup)
            # rename setup - just removing the '_blank' suffix
            old = join(target, f"map_source\{self.mapName}_blank.map")
            new = join(target, f"map_source\{self.mapName}.map")
            rename(old, new)

    ## END - mapSource - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - mainMenuScreen - METHOD

    def mainMenuScreen(self, target):

        if self.MainWindow.ui.mainMenuMaterial.text().strip():
            materialName = self.mainMenuScreenmaterialPath.split('/')[-1]

            # bg.inc
            # add rawfile if it doent exist
            bg = join(level.WAW_ROOT_DIR, r"raw\ui\bg.inc")
            copy = join(target, r"raw\ui\bg.inc")
            if not isfile(bg):
                copyfile(copy, bg)

            with open(bg, "a+", encoding="ISO-8859-1") as file:
                file.seek(0)
                content = file.read()
                includeLine = '#include "ui/blurredbg.inc"'
                if includeLine not in content:
                    file.write(includeLine)

            # blurredbg.inc
            # add rawfile if it doent exist
            blurredbg = join(level.WAW_ROOT_DIR, r"raw\ui\blurredbg.inc")
            blurredbgBackUp = join(level.WAW_ROOT_DIR, r"raw\ui\blurredbg.inc.backup")
            copy = join(target, r"raw\ui\blurredbg.inc")
            if not isfile(blurredbg):
                copyfile(copy, blurredbg)
                copyfile(copy, blurredbgBackUp)
            # if it does exist, turn it into a .backup file then add an original copy and edit that.
            else:
                copyfile(blurredbg, blurredbgBackUp)
                copyfile(copy, blurredbg)

            self.replaceOriginalCodeLine(blurredbg, "animbg_blur_back", materialName, True)
            self.replaceOriginalCodeLine(blurredbg, "menu_background_coop", materialName, True)
            self.replaceOriginalCodeLine(blurredbg, "menu_background_mp_tank", materialName, True)

            # mod.csv
            list = [
                "// Main Menu Screen",
                f"material,{materialName}",
                f"menufile,ui/{self.mapName}_main.menu" if self.MainWindow.ui.mainMenuBtnCheckBox.isChecked() else "menufile,ui/main.menu",
                "menufile,ui/bg.inc",
                "menufile,ui/blurredbg.inc"
            ]
            self.addmaterialCallAndMoveIwi(target, join(target, f"mods\{self.mapName}\mod.csv"), list, "Main Menu Screen", materialName)

    ## END - mainMenuScreen - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - pauseScreen - METHOD

    def pauseScreen(self, target):

        if self.MainWindow.ui.pauseScreenMaterial.text().strip():
            materialName = self.pauseScreenMaterialFilePath.split('/')[-1]
            # mod.csv
            list = [
                "// Pause Screen",
                f"material,{materialName}"
            ]
            self.addmaterialCallAndMoveIwi(target, join(target, f"mods\{self.mapName}\mod.csv"), list, "Pause Screen", materialName)

    ## END - pauseScreen - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - loadScreen - METHOD

    def loadScreen(self, target):

        if self.MainWindow.ui.loadScreenImage.text().strip():
            materialName = self.loadScreenMaterialFilePath.split('/')[-1]
            # mod.csv
            list = [
                "// Load Screen",
                f"material,{materialName}"
            ]
            self.addmaterialCallAndMoveIwi(target, join(target, f"mods\{self.mapName}\mod.csv"), list, "Load Screen", materialName)

    ## END - loadScreen - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - missionScreen - METHOD

    def missionScreen(self, target):

        if self.MainWindow.ui.missionScreenImage.text().strip():
            materialName = self.missionScreenMaterialFilePath.split('/')[-1]
            # mod.csv
            list = [
                "// Mission Screen",
                f"material,{materialName}",
                "stringtable,maps/mapsTable.csv"
            ]
            self.addmaterialCallAndMoveIwi(target, join(target, f"mods\{self.mapName}\mod.csv"), list, "Mission Screen", materialName)

    ## END - missionScreen - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - addmaterialCallAndMoveIwi - METHOD

    def addmaterialCallAndMoveIwi(self, target, path, list, featureName, materialName):

            # create images folder in mods folder if not already created by another material feature
            imagesFolder = join(target, fr"mods\{self.mapName}\images")
            if not isdir(imagesFolder):
                mkdir(imagesFolder)

            # copy material .iwi file from raw\images to mods\mapname\images
            src = join(level.WAW_ROOT_DIR, f"raw\images\{materialName}.iwi")
            if isfile(src):
                dst = join(target, f"mods\{self.mapName}\images\{materialName}.iwi")
                copyfile(src, dst)
            else:
                level.FINAL_MESSAGE.append((f"\n\nWARNING - {featureName}:\n"
                                            f"{materialName}.iwi is not located in root\\raw\\images.\n"
                                            "The 'texture name' & 'asset manager material name' do not match.\n"
                                            "You will need to copy the .iwi file from raw\\images to mods\\mapname\\images in order for this material to appear."))

            with open(path, "a+", encoding="ISO-8859-1") as file:
                file.seek(0)
                data = file.read()
                if len(data) > 0:
                    file.write("\n")
                file.write('\n'.join(list))

    ## END - addmaterialCallAndMoveIwi - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - startingWeapon - METHOD

    def startingWeapon(self, target):

        if self.MainWindow.ui.startWeap.text().strip():
            path = join(target, f"mods\{self.mapName}\maps\_loadout.gsc")
            self.addToOriginalCodeLine(path, 'add_weapon( "zombie_colt" );', f'\n		add_weapon( "{self.startingWeaponName}" );', "equals to")

    ## END - startingWeapon - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - switchWeapon - METHOD

    def switchWeapon(self, target):

        if self.MainWindow.ui.switchWeap.text().strip():
            path = join(target, f"mods\{self.mapName}\maps\_loadout.gsc")
            self.replaceOriginalCodeLine(path, 'set_switch_weapon( "zombie_colt" );', f'set_switch_weapon( "{self.switchWeaponName}" );', True)

    ## END - switchWeapon - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - laststandWeapon - METHOD

    def laststandWeapon(self, target):

        if self.MainWindow.ui.laststandWeap.text().strip():
            path = join(target, f"mods\{self.mapName}\maps\_loadout.gsc")
            self.replaceOriginalCodeLine(path, 'set_laststand_pistol( "zombie_colt" );', f'set_laststand_pistol( "{self.laststandWeaponName}" );', True)

    ## END - laststandWeapon - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - setPlayerScore - METHOD

    def setPlayerScore(self, target):

        if self.MainWindow.ui.score.text().strip():
            score = self.MainWindow.ui.score.text().strip()
            path = join(target, f"mods\{self.mapName}\maps\_zombiemode.gsc")
            self.replaceOriginalCodeLine(path, 'set_zombie_var( "zombie_score_start", 				500 );', f'set_zombie_var( "zombie_score_start", 				{score} );', True)

    ## END - setPlayerScore - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - mysteryBoxSetup - METHOD

    def mysteryBoxSetup(self, target):

        # 60 weapons - used for random and custom selection only
        if self.MainWindow.ui.prototypeMap.isChecked():
            weapons = Weapons("prototype")
        # same weapons as prototype
        elif self.MainWindow.ui.asylumMap.isChecked():
            weapons = Weapons("asylum")
        elif self.MainWindow.ui.sumpfMap.isChecked():
            weapons = Weapons("sumpf")
        elif self.MainWindow.ui.factoryMap.isChecked():
            weapons = Weapons("factory")
        elif self.MainWindow.ui.allInOneMap.isChecked():
            weapons = Weapons("custom")

        #############
        ### STOCK ###
        #############
        if self.MainWindow.ui.stockBoxSetup.isChecked():
            # Prototype stock box weapons
            # Technically the m7_launcher is in the stock prototype mapname.gsc mystery box section but it shouldnt be as its only an Alt weapon.
            # So ive removed it from the box list but i will add it manually to mapname.csv when needed.
            stockWeapsList = [
                # Grenade
                "molotov", "stielhandgranate",
                # Pistols
                "sw_357",
                # Semi Auto
                "m1carbine", "m1garand", "gewehr43",
                # Full Auto
                "stg44", "thompson", "mp40",
                # Bolt Action
                "kar98k", "springfield",
                # Scoped
                "ptrs41_zombie", "kar98k_scoped_zombie",
                # Grenade Launcher
                "m1garand_gl",
                # Flamethrower
                "m2_flamethrower_zombie",
                # Shotgun
                "doublebarrel", "doublebarrel_sawed_grip", "shotgun",
                # Bipod
                "fg42_bipod", "mg42_bipod", "30cal_bipod",
                # Heavy MG
                "bar",
                # Rocket Launcher
                "panzerschrek",
                # Special
                "ray_gun"
            ]

            weapArray = sorted(stockWeapsList)

        ##############
        ### RANDOM ###
        ##############
        if self.MainWindow.ui.randBoxSetup.isChecked():
            # box will have a min of 15 weapons in box out of a max of 35
            randNum = random.randint(15, 35)
            minMaxRange = range(0, (len(weapons) -1))
            # for some reason this list isnt iterable and can print the whole list without a for loop
            listOfRandNumsBetweenMinMaxRange = random.sample(minMaxRange, randNum)
            # print(f"randList: {randList}")

            array = []
            for i in range(len(listOfRandNumsBetweenMinMaxRange)):
                x = weapons[listOfRandNumsBetweenMinMaxRange[i]]
                array.append(x)

            weapArray = sorted(array)

        ##############
        ### CUSTOM ###
        ##############
        if self.MainWindow.ui.customBoxSetup.isChecked():
            self.getCustomBoxSelection()
            weapArray = sorted(self.customBoxWeaponSelection)

        ###################
        ### Add to .gsc ###
        ###################
        # add gsc specific code to weapon name
        gsc = []
        for value in weapArray:
            # add first func bracket
            if len(gsc) == 0:
                x = '{'
                gsc.append(x)
            x = f'	include_weapon( "{value}" );'
            gsc.append(x)
        # add last func bracket
        x = '}'
        gsc.append(x)

        path = join(target, f"mods\{self.mapName}\maps\{self.mapName}.gsc")
        self.addToOriginalCodeLine(path, "include_weapons()", '\n'.join(gsc), "equals to")

        ###################
        ### Add to .csv ###
        ###################
        # add csv specific code to weapon name
        csv = []
        for value in weapArray:
            x = f'weapon,sp/{value}'
            csv.append(x)

        # if a _bipod weapon is in list then they will need the following (crouch, stand, prone) files to work
        # copy main list
        # iterate through copy list and append to main list(if needed)
        tempArray = csv.copy()
        for i in tempArray:
            if "bar_bipod" in i:
                x = ['weapon,sp/bar_bipod_crouch', 'weapon,sp/bar_bipod_stand', 'weapon,sp/bar_bipod_prone']
                csv.extend(x)
            if "dp28_bipod" in i:
                x = ['weapon,sp/dp28_bipod_crouch', 'weapon,sp/dp28_bipod_stand', 'weapon,sp/dp28_bipod_prone']
                csv.extend(x)
            if "fg42_bipod" in i:
                x = ['weapon,sp/fg42_bipod_crouch', 'weapon,sp/fg42_bipod_stand', 'weapon,sp/fg42_bipod_prone']
                csv.extend(x)
            if "mg42_bipod" in i:
                x = ['weapon,sp/mg42_bipod_crouch', 'weapon,sp/mg42_bipod_stand', 'weapon,sp/mg42_bipod_prone']
                csv.extend(x)
            if "30cal_bipod" in i:
                x = ['weapon,sp/30cal_bipod_crouch', 'weapon,sp/30cal_bipod_stand', 'weapon,sp/30cal_bipod_prone']
                csv.extend(x)
            if "type99_lmg_bipod" in i:
                x = ['weapon,sp/type99_lmg_bipod_crouch', 'weapon,sp/type99_lmg_bipod_stand', 'weapon,sp/type99_lmg_bipod_prone']
                csv.extend(x)

        # if user changes starting weapon then add it to mapname.csv if its not already in the box.
        # if it isnt in the box adding it as a starting weapon doesnt mean itll be added to the box either.
        if self.MainWindow.ui.startWeap.text():
            csv.append(f"weapon,sp/{self.startingWeaponName}")

        # zombie_colt is the potential starting weapon so include it in mapname.csv
        csv.append('weapon,sp/zombie_colt')

        # doublebarrel_sawed_grip is a wall weapon so include it in mapname.csv
        doublebarrel_sawed_grip = False
        for i in csv:
            if "doublebarrel_sawed_grip" in i:
                doublebarrel_sawed_grip = True
                break
        if not doublebarrel_sawed_grip:
            csv.append('weapon,sp/doublebarrel_sawed_grip')

        # Add these to mapname.csv too. not sure what they are but they're used in stock scripts so follow suite.
        x = ['weapon,sp/napalmblob', 'weapon,sp/napalmbloblight']
        csv.extend(x)

        # m1garand_gl uses `m7_launcher` as an Alt weapon so include it in mapname.csv when needed.
        for i in csv:
            if "m1garand_gl" in i:
                csv.append('weapon,sp/m7_launcher')
                break

        path = join(target, f"zone_source\{self.mapName}.csv")
        self.addToOriginalCodeLine(path, "// WEAPONS", '\n'.join(sorted(csv)), "equals to")

    ## END - mysteryBoxSetup - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - getCustomBoxSelection - METHOD

    def getCustomBoxSelection(self):
        self.customBoxWeaponSelection = []
        for i in range(self.comboBox.count()):
            bool, value = self.comboBox.itemChecked(i)
            if bool:
                # print(value)
                self.customBoxWeaponSelection.append(value)

    # END - getCustomBoxSelection - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - deleteUnneededFiles - METHOD

    def deleteUnneededFiles(self, target):

        # Main Menu Custom Start Map Button
        if not self.MainWindow.ui.mainMenuBtnCheckBox.isChecked():
            x = join(target, fr"raw\ui\{self.mapName}_main.menu")
            remove(x)

        # Main Menu Screen
        remove(join(target, r"raw\ui\bg.inc"))
        remove(join(target, r"raw\ui\blurredbg.inc"))

        # Load Screen
        if not self.MainWindow.ui.loadScreenImage.text():
            remove(join(target, fr"mods\{self.mapName}\maps\{self.mapName}.csv"))
            remove(join(target, fr"map_source\{self.mapName}_load.map"))
            remove(join(target, fr"zone_source\{self.mapName}_load.csv"))

        # Mission Screen
        if not self.MainWindow.ui.missionScreenImage.text():
            remove(join(target, fr"mods\{self.mapName}\maps\mapsTable.csv"))

        # Mini Map
        x = join(target, r"raw\ui\hud.txt")
        remove(x)
        x = join(target, r"raw\ui\hud.menu")
        remove(x)
        x = join(target, r"raw\ui\minimap_cod5_nakshatra_12.inc")
        remove(x)

    ## END - deleteUnneededFiles - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - replaceOriginalCodeLine - METHOD

    def replaceOriginalCodeLine(self, path, old, new, returnAfterFirstMatch):

        with open(path, "r", encoding="ISO-8859-1") as file:
            old = old.strip()
            temp = file.read()
            if old not in temp:
                return False

            file.seek(0)
            list_of_lines = file.readlines()
            matchFound = False
            for i in range(len(list_of_lines)):
                if old in list_of_lines[i].strip():
                    list_of_lines[i] = list_of_lines[i].replace(old, new)
                    matchFound = True
                    if returnAfterFirstMatch:
                        break

        with open(path, "w", encoding="ISO-8859-1") as file:
            file.writelines(list_of_lines)

        if returnAfterFirstMatch and matchFound:
            return True

        if matchFound:
            return True

        return False

    ## END - replaceOriginalCodeLine - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - addToOriginalCodeLine - METHOD

    def addToOriginalCodeLine(self, path, old, new, which):

        with open(path, "r", encoding="ISO-8859-1") as file:
            old = old.strip()
            temp = file.read()
            if old not in temp:
                return

            file.seek(0)
            list_of_lines = file.readlines()
            for i in range(len(list_of_lines)):
                if which == "in":
                    if old in list_of_lines[i].strip():
                        list_of_lines[i] = list_of_lines[i] + new
                        break
                elif which == "equals to":
                    if old == list_of_lines[i].strip():
                        list_of_lines[i] = list_of_lines[i] + new
                        break

        with open(path, "w", encoding="ISO-8859-1") as file:
            file.writelines(list_of_lines)

    ## END - addToOriginalCodeLine - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - fileCheck - METHOD

    def fileCheck(self, path, subDir, featureName):

        # simple file check
        if not isfile(path):
            QMessageBox.about(self.MainWindow, "WARNING", f"{path}\nIs not a file.")
            return False

        # make sure file doesnt have an extension.
        try:
            extension = path.split('.')[1]
            if extension:
                QMessageBox.about(self.MainWindow, "WARNING", f"{path}\nIs not a valid file.")
                return False
        except Exception:
            pass

        # make sure it resides in the correct raw folder (this is the only way i can think of ensuring it is actually a material file and not a weapon file for example)
        if "materials" in subDir:
            x = f"Call of Duty World at War/{subDir}"
        elif "weapons" in subDir:
            x = f"Call of Duty World at War\{subDir}"
        if x not in path:
            QMessageBox.about(self.MainWindow, "WARNING", f"The `{featureName}` feature requires the file to reside in root/{x}.")
            return False

        return True

    ## END - fileCheck - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - mapnameExists - METHOD

    def mapnameExists(self):

        # Quickest way to tell if a mapname already exists:
        # mods folder
        # mods		  -> mapname.gsc
        # map_source  -> mapname.map
        # zone_source -> mapname.csv

        self.mapnameErrorMsg = ""
        paths = self.getAllMapNameDirectories(self.mapName)
        paths.reverse()

        for i in paths:
            if isfile(i):
                self.mapnameErrorMsg = f"Remnants of {self.mapName} exist:\n{i}"
            elif isdir(i):
                self.mapnameErrorMsg = f"Remnants of {self.mapName} exist:\n{i}"

        if self.mapnameErrorMsg != "":
            return True

        return False

    ## END - mapnameExists - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - deleteMap - METHOD

    def deleteMap(self):

        mapName = self.MainWindow.ui.deleteMapTextBox.text().strip()
        if mapName != "":
            paths = self.getAllMapNameDirectories(mapName)

            if self.MainWindow.ui.removeAppData.isChecked():
                # user might want to keep the compiled version
                paths.append(join(expanduser('~\AppData'), fr"Local\Activision\CoDWaW\mods\{mapName}"))

            paths.reverse()

            deleted = []
            for path in paths:
                if isfile(path):
                    deleted.append(f"root{path[len(level.WAW_ROOT_DIR):]}")
                    remove(path)
                elif isdir(path):
                    if "AppData" in path:
                        deleted.append(path)
                    else:
                        deleted.append(f"root{path[len(level.WAW_ROOT_DIR):]}")
                    rmtree(path)

            bgIncRawFile = join(level.WAW_ROOT_DIR, r"raw\ui\bg.inc")
            if isfile(bgIncRawFile):
                with open(bgIncRawFile, "r", encoding="ISO-8859-1") as file:
                    content = file.read()

            # Removed as i no longer use a mapname-specific version of the blurredbg.inc file.
            # includeLine = f'#include "ui/{mapName}_blurredbg.inc"'
            # if includeLine in content:
            #     self.replaceOriginalCodeLine(bgIncRawFile, includeLine, ''.strip(), True)
            #     x = f"root{bgIncRawFile[len(level.WAW_ROOT_DIR):]}"
            #     deleted.append(f'Removed `{includeLine}` from:\n{x}\n')

            if len(deleted) > 0:
                deleted.reverse()
                QMessageBox.about(self.MainWindow, "Successfully Deleted:", '\n'.join(deleted))
            else:
                QMessageBox.about(self.MainWindow, "WARNING", 'Nothing to delete')
            self.MainWindow.ui.deleteMapTextBox.setText("")
            if self.MainWindow.ui.removeAppData.isChecked():
                self.MainWindow.ui.removeAppData.setChecked(False)
        else:
            QMessageBox.about(self.MainWindow, "WARNING", 'You forgot to enter a map name.')

    ## END - deleteMap - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - advancedMode - METHOD

    def advancedMode(self):
        # This is not visually checkable. Only behind the scenes. Its so i can tell if they've previously clicked it rather than using a global var.
        if self.MainWindow.ui.advModeBtn.isChecked():
            self.MainWindow.ui.advancedFrame.show()
            self.MainWindow.resize(self.MainWindow.width(), 591)
        else:
            self.MainWindow.ui.advancedFrame.hide()
            self.MainWindow.resize(self.MainWindow.width(), 421)

            # disabling advanced mode so undo any changes made by user
            # Mini map
            if self.MainWindow.ui.addMiniMapCheckBox.isChecked():
                self.MainWindow.ui.addMiniMapCheckBox.setChecked(False)
            if self.MainWindow.ui.miniMapTextBox.text():
                self.MainWindow.ui.miniMapTextBox.setText("")

            # Fog
            if not self.MainWindow.ui.enableFogCheckBox.isChecked():
                self.MainWindow.ui.enableFogCheckBox.setChecked(True)

            # Vision
            if self.MainWindow.ui.visionFileTextBox.text():
                self.MainWindow.ui.visionFileTextBox.setText("")
            if self.MainWindow.ui.usingCustomVisionFile.isChecked():
                self.MainWindow.ui.usingCustomVisionFile.setChecked(False)

            # Fov
            if self.MainWindow.ui.FovSlider.value() != 65:
                self.MainWindow.ui.FovSlider.setSliderPosition(65)
                self.MainWindow.ui.label.setText("Fov: 65")

            # Start, Switch & Laststand Weapon | Score | Player ViewModel & Player Hands
            if self.MainWindow.ui.startWeap.text():
                self.MainWindow.ui.startWeap.setText("")
            if self.MainWindow.ui.switchWeap.text():
                self.MainWindow.ui.switchWeap.setText("")
            if self.MainWindow.ui.laststandWeap.text():
                self.MainWindow.ui.laststandWeap.setText("")
            if self.MainWindow.ui.score.text():
                self.MainWindow.ui.score.setText("")
            if self.MainWindow.ui.playerViewModel.text():
                self.MainWindow.ui.playerViewModel.setText("")
            if self.MainWindow.ui.playerHands.text():
                self.MainWindow.ui.playerHands.setText("")

            # Mystery Box
            if not self.MainWindow.ui.stockBoxSetup.isChecked():
                self.MainWindow.ui.stockBoxSetup.setChecked(True)
            if self.MainWindow.ui.randBoxSetup.isChecked():
                self.MainWindow.ui.randBoxSetup.setChecked(False)
            if self.MainWindow.ui.customBoxSetup.isChecked():
                self.MainWindow.ui.customBoxSetup.setChecked(False)

    ## END - advancedMode - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - addPathToTextBox - METHOD

    def addPathToTextBox(self, which):

        if which == "customMap":
            path = str(QFileDialog.getOpenFileName(self.MainWindow, "Select .map file."))
            x = path.split(',')[0][2:][:-1]
            self.MainWindow.ui.custMapFileTextBox.setText(x)
            return
        elif which == "vision":
            path = str(QFileDialog.getOpenFileName(self.MainWindow, "Select vision file."))
            x = path.split(',')[0][2:][:-1]
            self.MainWindow.ui.visionFileTextBox.setText(x)
            return

        x = str(QFileDialog.getOpenFileName(self.MainWindow, "Select material file."))
        path = x.split(',')[0][2:][:-1]

        if which == "miniMap":                  self.MainWindow.ui.miniMapTextBox.setText(path)
        elif which == "mainMenuScreen":         self.MainWindow.ui.mainMenuMaterial.setText(path)
        elif which == "PauseScreen":            self.MainWindow.ui.pauseScreenMaterial.setText(path)
        elif which == "loadScreen":             self.MainWindow.ui.loadScreenImage.setText(path)
        elif which == "missionScreen":          self.MainWindow.ui.missionScreenImage.setText(path)

    ## END - addPathToTextBox - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - mysteryBoxStateChanged - METHOD

    def mysteryBoxStateChanged(self):
        if self.MainWindow.ui.customBoxSetup.isChecked():
            self.comboBox = CheckableComboBox(self.MainWindow)
            self.comboBox.setGeometry(10, 70, 221, 41)
            self.comboBox.setObjectName(u"combobox")
            self.comboBox.setStyleSheet(u"#combobox{\n"
                                        "	background-color: rgb(231, 230, 234);\n"
                                        "	border-radius: 7px;\n"
                                        "	padding: 8px;\n"
                                        "}")

            self.MainWindow.w = ComboxBoxWindow(self.comboBox)
            self.MainWindow.w.setObjectName(u"comboWindow")
            self.MainWindow.w.setStyleSheet(u"#comboWindow{\n"
                                "	background: rgb(37,39,48);\n"
                                "	border-radius: 20px;\n"
                                "	opacity: 100;\n"
                                "	border: 2px solid #0800ff;\n"
                                "}")

            self.MainWindow.w.show()
        else:
            try:
                self.MainWindow.w.deleteLater()
            except:
                pass

    ## END - mysteryBoxStateChanged - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - getAllMapNameDirectories - METHOD

    def getAllMapNameDirectories(self, mapName):
        paths = []
        paths.append(join(level.WAW_ROOT_DIR, fr"bin\Launcher\map_settings\{mapName}.cfg"))
        paths.append(join(level.WAW_ROOT_DIR, fr"bin\Launcher\map_settings\{mapName}_patch.cfg"))
        paths.append(join(level.WAW_ROOT_DIR, fr"bin\Launcher\map_settings\{mapName}_load.cfg"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\maps\{mapName}.gsc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\maps\{mapName}_fx.gsc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\maps\createart\{mapName}_art.gsc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\maps\createfx\{mapName}_fx.gsc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\clientscripts\{mapName}.csc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\clientscripts\{mapName}_amb.csc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\clientscripts\{mapName}_fx.csc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"mods\{mapName}\clientscripts\createfx\{mapName}_fx.csc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"map_source\{mapName}.map"))
        paths.append(join(level.WAW_ROOT_DIR, fr"map_source\{mapName}_patch.map"))
        paths.append(join(level.WAW_ROOT_DIR, fr"map_source\{mapName}.bak"))
        paths.append(join(level.WAW_ROOT_DIR, fr"map_source\{mapName}_patch.bak"))
        paths.append(join(level.WAW_ROOT_DIR, fr"map_source\{mapName}_load.map"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\maps\{mapName}.radtrans"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\maps\{mapName}.d3dbsp"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\maps\{mapName}.grid_auto"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\maps\{mapName}.grid_not"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\soundaliases\{mapName}.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\ui\{mapName}_main.menu"))
        paths.append(join(level.WAW_ROOT_DIR, fr"raw\ui\{mapName}_blurredbg.inc"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\{mapName}.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\{mapName}_patch.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\{mapName}_load.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetlist\{mapName}.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetlist\{mapName}_patch.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetlist\{mapName}_load.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}_patch.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}_load.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}_xmodel.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}_load_xmodel.csv"))
        paths.append(join(level.WAW_ROOT_DIR, fr"zone_source\english\assetinfo\{mapName}_patch_xmodel.csv"))
        return paths

    ## END - getAllMapNameDirectories - METHOD
    ############################## ---/--/--- ##############################

    ########################################################################
    ## START - placeHolder - METHOD

    # def placeHolder(self):
        

    ## END - placeHolder - METHOD
    ############################## ---/--/--- ##############################

## END - Logic - CLASS
############################## ---/--/--- ##############################

########################################################################
## START - weapons - FUNCTION

def Weapons(map):

    # This function covers all the weapons in map-specific _zombiemode_weapons file.
    # This is for custom and random mystery box selection.

    # The stock box option will use a weapon list comprised of weapons only mentioned in map-specific mapname.gsc files.
    # The stock list is not in this function.

    weapons = [
        # Pistols
        "walther", "nambu", "sw_357", "tokarev", "zombie_colt",
        # Bolt Action
        "kar98k", "kar98k_bayonet", "mosin_rifle", "mosin_rifle_bayonet", "springfield", "springfield_bayonet", "type99_rifle", "type99_rifle_bayonet",
        # Semi Auto
        "gewehr43", "m1carbine", "m1carbine_bayonet", "m1garand", "m1garand_bayonet", "svt40",
        # Grenades
        "fraggrenade", "molotov", "stick_grenade", "stielhandgranate", "type97_frag",
        # Scoped
        "kar98k_scoped_zombie", "kar98k_scoped_bayonet_zombie", "mosin_rifle_scoped_zombie", "mosin_rifle_scoped_bayonet_zombie",
        "ptrs41_zombie", "springfield_scoped_zombie", "springfield_scoped_bayonet_zombie", "type99_rifle_scoped_zombie", "type99_rifle_scoped_bayonet_zombie",
        # Full Auto
        "mp40", "ppsh", "stg44", "thompson", "type100_smg",
        # Shotguns
        "doublebarrel", "doublebarrel_sawed_grip", "shotgun",
        # Heavy Machineguns
        "30cal", "bar", "dp28", "fg42", "fg42_scoped", "mg42", "type99_lmg",
        # Grenade Launcher
        "m1garand_gl", "mosin_launcher",
        # Bipods
        "30cal_bipod", "bar_bipod", "dp28_bipod", "fg42_bipod", "mg42_bipod", "type99_lmg_bipod",
        # Rocket Launchers
        "bazooka", "panzerschrek",
        # Flamethrower
        "m2_flamethrower_zombie",
        # Special
        "ray_gun"
    ]

    return weapons

## END - weapons - FUNCTION
############################## ---/--/--- ##############################

########################################################################
## START - CheckableComboBox - CLASS

class CheckableComboBox(QComboBox):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self._changed = False

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(250, 35))
        self.setMaximumSize(QSize(250, 35)) # 16777215
        self.adjustSize()

        self.view().pressed.connect(self.handleItemPressed)
        # used for random and custom selection only
        # 60 weapons
        if self.MainWindow.ui.prototypeMap.isChecked():
            weapons = Weapons("prototype")
        # same weapons as prototype
        elif self.MainWindow.ui.asylumMap.isChecked():
            weapons = Weapons("asylum")
        elif self.MainWindow.ui.sumpfMap.isChecked():
            weapons = Weapons("sumpf")
        elif self.MainWindow.ui.factoryMap.isChecked():
            weapons = Weapons("factory")
        elif self.MainWindow.ui.allInOneMap.isChecked():
            weapons = Weapons("custom")

        for i in range(len(weapons)):
            self.addItem(weapons[i])
            self.setItemChecked(i, False)

    def setItemChecked(self, index, checked=False):
        item = self.model().item(index, self.modelColumn()) # QStandardItem object

        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)

        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True


    def hidePopup(self):
        if not self._changed:
            super().hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked, item.text()

## END - CheckableComboBox CLASS
############################## ---/--/--- ##############################

########################################################################
## START - ComboxBoxWindow - CLASS

class ComboxBoxWindow(QWidget):
    def __init__(self, comboBox):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.layout = QVBoxLayout()

        self.label = SubClassQLabel(self)
        self.label.setObjectName(u"comboWindowLabel")
        self.label.setStyleSheet(u"#comboWindowLabel\n"
                                "{\n"
                                "	color: black;\n"
                                "	border-radius: 7px;\n"
                                "	padding: 8px;\n"
                                "   background-color: #03e3fc;\n"
                                "}")

        self.layout.addWidget(self.label)
        self.layout.addWidget(comboBox)
        self.setLayout(self.layout)

        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topRight()) # center # geo.topRight()

## END - ComboxBoxWindow CLASS
############################## ---/--/--- ##############################

########################################################################
## START - SubClassQLabel - CLASS

class SubClassQLabel(QLabel):
    def __init__(self, subWindow):
        super().__init__("Custom Mystery Box Selection")
        self.subWindow = subWindow
        self.clickOnHeader = False

    def mousePressEvent(self, event):
        self.subWindow.oldPosition = event.globalPos()
        self.clickOnHeader = True

    def mouseReleaseEvent(self, event):
        self.clickOnHeader = False

    def mouseMoveEvent(self, event):
        if self.clickOnHeader is True:
            delta = QPoint(event.globalPos() - self.subWindow.oldPosition)
            self.subWindow.move(self.subWindow.x() + delta.x(), self.subWindow.y() + delta.y())
            self.subWindow.oldPosition = event.globalPos()

## END - SubClassQLabel CLASS
############################## ---/--/--- ##############################