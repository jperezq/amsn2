import sys
from amsn2.gui import base
import common

try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from ui_contactlist import Ui_ContactList
    from styledwidget import StyledWidget
except ImportError, msg:
    print "Could not import all required modules for the Qt 4 GUI."
    print "ImportError: " + str(msg)
    sys.exit()

class aMSNContactList(StyledWidget, base.aMSNContactList):
    def __init__(self, amsn_core, parent=None):
        StyledWidget.__init__(self, parent)
        self._amsn_core = amsn_core
        self.ui = Ui_ContactList()
        self.ui.setupUi(self)
        self._main_win = self._amsn_core.getMainWindow()
        self.ui.cList.clear()

    def show(self):
        self._main_win.fadeIn(self)
        self._main_win.setWindowTitle('aMSN 2')

    def hide(self):
        pass

    def groupAdded(self, group):
        groupItem = QTreeWidgetItem(self.ui.cList)
        groupItem.setText(0, group.name.toString())
        for contact in group.contacts:
            contactItem = QTreeWidgetItem(groupItem)
            contactItem.setText(0, contact.name.toString())

    def groupAdded(self, group):
        print group.name.toString()
        groupItem = QTreeWidgetItem(self.ui.cList)
        groupItem.setText(0, group.name.toString())
        for contact in group.contacts:
            print "  * " + contact.name.toString()
            contactItem = QTreeWidgetItem(groupItem)
            contactItem.setText(0, contact.name.toString())