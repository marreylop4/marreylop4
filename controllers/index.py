from PySide2.QtCore import (QCoreApplication, QDir, QFile, QFileInfo, QMimeData,
                            QMimeDatabase, QUrl, Qt, Slot, QObject, QIODevice, QTranslator)

from PySide2.QtGui import ( QGuiApplication, QClipboard,
                           QCloseEvent, QFont, QFontDatabase, QFontInfo, QIcon,
                           QKeySequence, QPixmap, QTextBlockFormat,
                           QTextCharFormat, QTextCursor, QTextDocumentWriter,
                           QTextList, QTextListFormat, QTextDocument )
from PySide2.QtWidgets import (QApplication, QMainWindow, QColorDialog, QComboBox,
                               QDialog, QFileDialog, QFontComboBox, QStatusBar, QAction, QActionGroup,
                               QTextEdit, QToolBar, QMenu, QMenuBar, QMessageBox, QWidget, QSplitter, QFrame, QHBoxLayout)


from views.index import Index
from controllers.main_window import TextEditWindow

class IndexWindow(QWidget, Index):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.applicationName())#el titulo de la app
        self.index = True
        self.newFile.clicked.connect(TextEditWindow.file_new)
        self.openFile.clicked.connect(TextEditWindow.file_open)

    def load_file(self, f):
        """
        This function loads a file in our application, being able 
        to load markdown and text type files.

        Inputs:
            :f: the selected file
        
        """ 
        if self.maybe_save():
            if not QFile.exists(f):
                return False
            file = QFile(f)
            if not file.open(QFile.ReadOnly):
                return False

        data = file.readAll()
        file_info= QFileInfo(file)
        self.set_current_file_format( file_info.suffix())
        db = QMimeDatabase()
        mime_type_name = db.mimeTypeForFileNameAndData(f, data).name()
        text = data.data().decode('utf8')
        if mime_type_name == "text/markdown":
            self._text_edit.setMarkdown(text)
        else:
            self._text_edit.setPlainText(text)

        self.set_current_file_name(f)
        return True

    @Slot()
    def file_new(self):
        """
        This function deletes everything that is in the editor if 
        the previous one has been saved or discarded and thus be able to start a new one

        
        """ 
        if self.maybe_save():
            self._text_edit.clear()
            self.set_current_file_name("")
            
