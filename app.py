from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTranslator, QSettings, QLocale, QLibraryInfo, QCoreApplication, QObject
import sys

from controllers.main_window import TextEditWindow
from controllers.index import IndexWindow


    
class Main():
    def execute(self):
        """
        This installs the translator for internalization and runs the interface
        
        """
        app=QApplication(sys.argv)
        
        translator = QTranslator(app)
        if translator.load("qt_"+QLocale.system().name()+".qm", QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
            app.installTranslator(translator) 

        window = IndexWindow()
        available_geometry = window.screen().availableGeometry()
        window.resize((available_geometry.width() * 2) / 3,
                (available_geometry.height() * 2) / 3)
        window.move((available_geometry.width() - window.width()) / 2,
                (available_geometry.height() - window.height()) / 2)
        
        
        #window.file_new()

        window.show()
        
        app.exec_()



if __name__=="__main__":
    
    Main().execute()