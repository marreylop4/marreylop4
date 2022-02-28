import markdown
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

from PySide2.QtWebEngineWidgets import QWebEngineView
#MIRAR EL WEBVIEW
from PySide2.QtPrintSupport import (QAbstractPrintDialog, QPrinter,
                                    QPrintDialog, QPrintPreviewDialog)

from views.view_main_window import TextEdit

from controllers.index import IndexWindow

ABOUT = """""".join(["""<p>This is a markdown text editor with preview. The
                     uploaded or created files can be saved in different formats 
                     such as HTML. If you want to know more about markdown here is a link about it:</p>
                     <a href =https://www.markdownguide.org/basic-syntax/#html>Markdown Guide</a> """])


MIME_TYPES = ["text/html", "text/markdown", "text/plain"]






class TextEditWindow(QMainWindow, TextEdit):
    """
    This class is where the functions will be carried out so that the actions of the interface work
    
    Inputs:
        :QMainWindow: this is the type of page of our interface
        :TextEdit: inherited from views.view_main_window class
        

        
    """    
    def __init__(self ):
        """
        This function initializes the methods of this class that sub becesaruis so that the application works correctly       
        
        

        
        """    
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle(QCoreApplication.applicationName())#el titulo de la app


        self._text_edit.setFrameShape(QFrame.StyledPanel)
        self._text_edit.textChanged.connect(self.onTextChanged)
        self.preview.setHtml("start typing on the left pane")
        
        

        self.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.setup_file_actions()
        self.setup_edit_actions()

        about = self.actionAbout
        about.triggered.connect(self.about)

        

        document = self._text_edit.document()
        document.modificationChanged.connect(self.actionSave.setEnabled)
        document.modificationChanged.connect(self.setWindowModified)
        document.undoAvailable.connect(self.actionUndo.setEnabled)
        document.redoAvailable.connect(self.actionRedo.setEnabled)
        self.setWindowModified(document.isModified())
        self.actionSave.setEnabled(document.isModified())
        self.actionUndo.setEnabled(document.isUndoAvailable())
        self.actionRedo.setEnabled(document.isRedoAvailable())

        self.actionCut.setEnabled(False)
        self._text_edit.copyAvailable.connect(self.actionCut.setEnabled)
        self.actionCopy.setEnabled(False)
        self._text_edit.copyAvailable.connect(self.actionCopy.setEnabled)

        QGuiApplication.clipboard().dataChanged.connect(self.clipboard_data_changed)

        self._text_edit.setFocus()
        self.set_current_file_name('')

        
        
    def onTextChanged(self):     
        """
        This function does the preview of the markdown text every 
        time it detects that the text changes    
        

        
        """    
        try:
            html = markdown.markdown(self._text_edit.toPlainText())
        except:
            html = QCoreApplication.tr('Error decoding ')
        self.preview.setHtml(html)
        
    def closeEvent(self, e):
        """
        This function checks if the generated text has been saved before closing the application
        
        Inputs:
            :e: QCloseEvent
        
        """  
        if self.maybe_save():
            e.accept()
        else:
            e.ignore()

    def setup_file_actions(self):
        """
        This function gives the actions to the "File" menu of our interface


        
        """  
        menu = self.menuFile

        new = self.actionNew
        new.triggered.connect(self.file_new)
        new.setPriority(QAction.LowPriority)

        open = self.actionOpen
        open.triggered.connect(self.file_open)

        save = self.actionSave
        save.triggered.connect(self.file_save)
        save.setEnabled(False)
        
        saveAs = self.actionSave_As
        saveAs.triggered.connect(self.file_save_as)
        saveAs.setPriority(QAction.LowPriority)
        
        quit = self.actionQuit
        quit.triggered.connect(self.close)

        menu.addSeparator()
        
        

    def setup_edit_actions(self):
        """
        This function gives the actions to the "Edit" menu of our interface


        
        """  

        undo = self.actionUndo
        undo.triggered.connect(self._text_edit.undo)
        
        redo = self.actionRedo
        redo.triggered.connect(self._text_edit.redo)
        redo.setPriority(QAction.LowPriority)
    

        cut = self.actionCut 
        cut.triggered.connect(self._text_edit.cut)
        cut.setPriority(QAction.LowPriority)
        
        copy = self.actionCopy
        copy.triggered.connect(self._text_edit.copy)
        copy.setPriority(QAction.LowPriority)
        

        paste = self.actionPaste
        paste.triggered.connect(self._text_edit.paste)
        paste.setPriority(QAction.LowPriority)
        
        

    
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

    def maybe_save(self):
        """
        This function checks if the document has had a modification 
        that has not been saved and gives you the option to do so


        
        """ 
        if not self._text_edit.document().isModified() :
            return True

        ret = QMessageBox.warning(self, QCoreApplication.applicationName(),
                                  self.tr( "The document has been modified.\n"
                                  "Do you want to save your changes?"),
                                  QMessageBox.Save | QMessageBox.Discard
                                  | QMessageBox.Cancel)
        if ret == QMessageBox.Save:
            return self.file_save()
        if ret == QMessageBox.Cancel:
            return False
        return True

    def set_current_file_name(self, fileName):
        """
        This function sets the name of the file (it is called in several functions)

        Inputs:
            :fileName: the file name

        
        """ 
        self._file_name = fileName
        self._text_edit.document().setModified(False)

        shown_name = QFileInfo(fileName).fileName() if fileName else "untitled.txt"
        app_name = QCoreApplication.applicationName()
        self.setWindowTitle(f"{shown_name}[*] - {app_name}")
        self.setWindowModified(False)
        
    def set_current_file_format(self, fileFormat):
        """
        This function sets the format of the file (it is called in several functions)

        Inputs:
            :fileFormat: the file format
        
        """ 
        self._file_format = fileFormat
        self._text_edit.document().setModified(False)

        
    @Slot()
    def file_new(self):
        """
        This function deletes everything that is in the editor if 
        the previous one has been saved or discarded and thus be able to start a new one

        
        """ 
        if self.maybe_save():
            self._text_edit.clear()
            self.set_current_file_name("")
            

    @Slot()
    def file_open(self):
        """
        This function opens the files that we have saved on our device to 
        be able to edit them with the application


        """ 
        file_dialog = QFileDialog(self, "Open File...")
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setMimeTypeFilters(["text/markdown", "text/plain"])
        if file_dialog.exec() != QDialog.Accepted:
            return
        fn = file_dialog.selectedFiles()[0]
        native_fn = QDir.toNativeSeparators(fn)
        if self.load_file(fn):
            self.statusBar().showMessage('Opened "{native_fn}"')
        else:
            self.statusBar().showMessage(f'Could not open "{native_fn}"')

    @Slot()
    def file_save(self):
        """
        This function saves all the elements of the file generated
        or uploaded and modified in our application


        
        """ 
        if not self._file_name or self._file_name.startswith(":/"):
            return self.file_save_as()

        writer = QTextDocumentWriter(self._file_name)
       
        if self._file_format == "html":
            document = markdown.markdown(self._text_edit.document().toPlainText())           
            
            with open(self._file_name, 'w') as f:
                f.write(''.join(["<html><head><style>"
                          "</style></head><body>",
                          document,
                          "</body></html>"]))
                success = f
            native_fn = QDir.toNativeSeparators(self._file_name)
            if success:
                self._text_edit.document().setModified(False)
                self.statusBar().showMessage(f'Wrote "{native_fn}"')
            else:
                self.statusBar().showMessage(f'Could not write to file "{native_fn}"')
            return success          
        else:
            document = self._text_edit.document();
            success = writer.write(document)
            native_fn = QDir.toNativeSeparators(self._file_name)
            if success:
                document.setModified(False)
                self.statusBar().showMessage(f'Wrote "{native_fn}"')
            else:
                self.statusBar().showMessage(f'Could not write to file "{native_fn}"')
            return success  
        
        
    @Slot()
    def file_save_as(self):
        """
        This function saves all the elements of the file generated
        or loaded and modified in our application, being able to give it the format and name you want.


        
        """ 
        file_dialog = QFileDialog(self, "Save as...")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)

        mime_types = MIME_TYPES
        file_dialog.setMimeTypeFilters(mime_types)
        file_dialog.setDefaultSuffix("md")
        if file_dialog.exec() != QDialog.Accepted:
            return False
        fn = file_dialog.selectedFiles()[0]
        self.set_current_file_name(fn)
        file_info= QFileInfo(fn)
        self.set_current_file_format( file_info.suffix())
        return self.file_save()
           

    

    @Slot()
    def clipboard_data_changed(self):
        """
        This function takes what is saved in the clipboard and puts it in what the paste action can do


        
        """ 
        md = QGuiApplication.clipboard().mimeData()
        self.actionPaste.setEnabled(md and md.hasText())

    @Slot()
    def about(self):
        """
        This function creates a message box with information about what you can do in the application
        
        """ 
        
        QMessageBox.about(self, "About", ABOUT)
