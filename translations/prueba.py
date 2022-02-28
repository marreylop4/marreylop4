from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QTranslator, QSettings, QLocale, QLibraryInfo, QCoreApplication, QObject
import sys

from controllers.main_window import TextEditWindow


if __name__=="__main__":
    app = QApplication(sys.argv)



    translator = QTranslator()

    translator.load("qt_"+QLocale.system().name()+".qm", QLibraryInfo.location(QLibraryInfo.TranslationsPath))

    app.installTranslator(translator)



    hello = QPushButton(QPushButton.tr("Hello world!"))

    hello.resize(100, 30)

    hello.show()
    app.exec_()