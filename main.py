import sys
from PyQt5.QtWidgets import QApplication, QWidget

import gui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWidget = QWidget()
    ui = gui.Ui_Form()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())