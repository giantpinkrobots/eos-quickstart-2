import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QScrollArea, QPushButton, QSpacerItem, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from vars import *

class quickstart(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(820,680)
        self.setMaximumSize(820,680)
        self.setWindowTitle("EndeavourOS Quickstart Installer")
        self.setWindowIcon(QIcon.fromTheme("system-software-install"))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.selectedTerminalApp = ""
        for terminalApp in terminalApps:
            if os.path.isfile(terminalApp.split(" ")[0]):
                self.selectedTerminalApp = terminalApp
                break
        if self.selectedTerminalApp == "":
            info_message = QMessageBox()
            info_message.setText("No supported terminal app found. Exiting.")
            info_message.setWindowTitle("Error")
            info_message.exec_()
            exit()

        self.getInstalledPackages()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.buildToolbox()
        self.layout.addWidget(self.scrollArea)

        spacer = QSpacerItem(0, 20)
        self.layout.addItem(spacer)

        buttonInstall = QPushButton("Apply")
        buttonInstall.clicked.connect(self.install)
        self.layout.addWidget(buttonInstall)

    def install(self):
        self.getInstalledPackages()

        checkedSoftwareList = []
        for toolboxCount in range(self.toolbox.count()):
            checkedSoftware = []
            for listWidgetCount in range(self.toolbox.widget(toolboxCount).count()):
                if self.toolbox.widget(toolboxCount).item(listWidgetCount).checkState() == Qt.Checked:
                    checkedSoftware.append(True)
                else:
                    checkedSoftware.append(False)
            checkedSoftwareList.append(checkedSoftware)
        
        packagesInstall = ""
        packagesRemove = ""
        packagesListIndex = 0
        while packagesListIndex < len(itemsContents_PackageNames):
            packageIndex = 0
            while packageIndex < len(itemsContents_PackageNames[packagesListIndex]):
                if checkedSoftwareList[packagesListIndex][packageIndex] == True:
                    packagesInstall += " " + itemsContents_PackageNames[packagesListIndex][packageIndex]
                else:
                    if self.itemsContents_PackageNames_Installed[packagesListIndex][packageIndex] == [True]:
                        packagesRemove += " " + itemsContents_PackageNames[packagesListIndex][packageIndex]
                packageIndex += 1
            packagesListIndex += 1
        
        print("pacman -Rns --noconfirm" + packagesRemove)
        
        os.popen(self.selectedTerminalApp + " pkexec sh -c \"pacman -Syu --noconfirm --needed" + packagesInstall + ";pacman -Rns --noconfirm" + packagesRemove + ";read -rsp $\'\n\nPress enter to continue.\n\n\'\"").read()
        
        self.getInstalledPackages()
        self.buildToolbox()

    def getInstalledPackages(self):
        self.itemsContents_PackageNames_Installed = []

        packageListOutput = os.popen("pacman -Q | cut -d' ' -f1").read()
        itemsPackageNames_Check_TitlesCounter = 0
        while itemsPackageNames_Check_TitlesCounter < len(itemsTitles):
            itemsPackageNames_Check_ContentsCounter = 0
            self.itemsContents_PackageNames_Installed.append([])
            while itemsPackageNames_Check_ContentsCounter < len(itemsContents[itemsPackageNames_Check_TitlesCounter]):
                self.itemsContents_PackageNames_Installed[itemsPackageNames_Check_TitlesCounter].append([])
                if ("\n" + itemsContents_PackageNames[itemsPackageNames_Check_TitlesCounter][itemsPackageNames_Check_ContentsCounter] + "\n" in packageListOutput):
                    self.itemsContents_PackageNames_Installed[itemsPackageNames_Check_TitlesCounter][itemsPackageNames_Check_ContentsCounter].append(True)
                else:
                    self.itemsContents_PackageNames_Installed[itemsPackageNames_Check_TitlesCounter][itemsPackageNames_Check_ContentsCounter].append(False)
                itemsPackageNames_Check_ContentsCounter += 1
            itemsPackageNames_Check_TitlesCounter += 1
    
    def buildToolbox(self):
        self.toolbox = QToolBox()
        titleCounter = 0
        for iTitles in itemsTitles:
            listWidget = QListWidget()
            contentCounter = 0
            for iContents in itemsContents[titleCounter]:
                listWidgetItem = QListWidgetItem(iContents + " - " + itemsContents_PackageDescriptions[titleCounter][contentCounter])
                listWidgetItem.setFlags(listWidgetItem.flags() | Qt.ItemIsUserCheckable)
                if self.itemsContents_PackageNames_Installed[titleCounter][contentCounter] == [True]:
                    listWidgetItem.setCheckState(Qt.Checked)
                else:
                    listWidgetItem.setCheckState(Qt.Unchecked)
                listWidget.addItem(listWidgetItem)
                contentCounter += 1
            self.toolbox.addItem(listWidget, QIcon.fromTheme(itemsTitles_Icons[titleCounter]), iTitles)
            titleCounter += 1
        
        self.toolbox.setFixedHeight(self.toolbox.sizeHint().height())
        self.scrollArea.setWidget(self.toolbox)

if __name__ == "__main__":
    program = QApplication(sys.argv)
    quickstart = quickstart()
    quickstart.show()
    sys.exit(program.exec_())