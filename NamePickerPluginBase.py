from PyQt5.QtWidgets import QWidget
import os
import sys

def load_libs():
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    libs_dir = os.path.join(plugin_dir, 'libs')
    if libs_dir not in sys.path:
        sys.path.insert(0, libs_dir)

class PluginBase:
    def __init__(self):
        self.PATH = os.path.dirname(os.path.abspath(__file__))
        self.filters = []
        self.customKey = []
        self.customKeyDesc = []

    def onStartup(self):
        pass

    def beforePick(self):
        pass

    def afterPick(self,name):
        pass

class SettingBase(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
