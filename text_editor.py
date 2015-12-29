#!/usr/bin/python

#Text - Editor
from ext import *

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Editor(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.filenm = ""		
		self.writerUI()

	def writerToolbar(self):
		self.toolbar = self.addToolBar("Text Actions")

		self.new = QAction(QIcon("icons/new.jpeg"), "New", self)
		self.new.setStatusTip("Create a new document")
		self.new.setShortcut("Ctrl+N")
		self.new.triggered.connect(self.new_doc)

		self.open = QAction(QIcon("icons/open.png"), "Open file", self)
		self.open.setStatusTip("Open the existing document")
		self.open.setShortcut("Ctrl+O")
		self.open.triggered.connect(self.open_doc)

		self.save = QAction(QIcon("icons/save.png"), "Save current file", self)
		self.save.setStatusTip("Save the current document")
		self.save.setShortcut("Ctrl+S")
		self.save.triggered.connect(self.save_doc)

		self.pdf = QAction(QIcon("icons/save.png"), "Export as PDF", self)
		self.pdf.setStatusTip("Converting file to pdf")
		self.pdf.triggered.connect(self.exportPdf)

		self.Print = QAction(QIcon("icons/print.png"), "Print document", self)
		self.Print.setStatusTip("Print the document")
		self.Print.setShortcut("Ctrl+P")
		self.Print.triggered.connect(self.print_doc)		

		self.preview = QAction(QIcon("icons/preview.png"), "Page view", self)
		self.preview.setStatusTip("Preview page before printing")
		self.preview.setShortcut("Ctrl+Shift+O")
		self.preview.triggered.connect(self.preview_doc)

		self.undo = QAction(QIcon("icons/undo.png"), "Undo last action", self)
		self.undo.setStatusTip("Undo the document")
		self.undo.setShortcut("Ctrl+Z")
		self.undo.triggered.connect(self.textArea.undo)

		self.redo = QAction(QIcon("icons/redo.jpg"), "Redo last undone action", self)
		self.redo.setStatusTip("Redo the document")
		self.redo.setShortcut("Ctrl+Y")
		self.redo.triggered.connect(self.textArea.redo)

		self.cut = QAction(QIcon("icons/cut.png"), "Cut the selection", self)
		self.cut.setStatusTip("Delete and Copy text")
		self.cut.setShortcut("Ctrl+X")
		self.cut.triggered.connect(self.textArea.cut)

		self.copy = QAction(QIcon("icons/copy.png"), "Copy the selection", self)
		self.copy.setStatusTip("Copy text")
		self.copy.setShortcut("Ctrl+C")
		self.copy.triggered.connect(self.textArea.copy)

		self.paste = QAction(QIcon("icons/paste.jpeg"), "Paste the clipboard", self)
		self.paste.setStatusTip("Paste text from clipboard")
		self.paste.setShortcut("Ctrl+V")
		self.paste.triggered.connect(self.textArea.paste)

		self.search = QAction(QIcon("icons/serach.jpeg"), "Search for text", self)
		self.search.setStatusTip("Search text from clipboard")
		self.search.setShortcut("Ctrl+Q")
		self.search.triggered.connect(find.Search(self).show)

		self.find = QAction(QIcon("icons/paste.jpeg"), "Find & replace text", self)
		self.find.setStatusTip("Find and replace the text from clipboard")
		self.find.setShortcut("Ctrl+F")
		self.find.triggered.connect(find_n_replace.FindandReplace(self).show)

		bulletlist = QAction(QIcon("icons/bullet.svg"), "Insert bullet List", self)
		bulletlist.setStatusTip("Insert bullet list")
		bulletlist.setShortcut("Ctrl+Shift+B")
		bulletlist.triggered.connect(self.bulletList)

		numberlist = QAction(QIcon("icons/number.png"), "Insert numbered List", self)
		numberlist.setStatusTip("Insert numbered list")
		numberlist.setShortcut("Ctrl+Shift+L")
		numberlist.triggered.connect(self.numberedList)
		# word and symbols count
		wordCount = QAction(QIcon("icons/count.png"), "See word/symbol count", self)
		wordCount.setStatusTip("See word/symbol count")
		wordCount.setShortcut("Ctrl+W")
		# wordCount.triggered.connect(self.wordCount)
		# closing the file
		self.close = QAction(QIcon("icons/close.png"), "Close the File", self)
		self.close.setStatusTip("Closing the file")
		self.close.setShortcut(QKeySequence(Qt.Key_Escape))
		self.close.triggered.connect(self.close_doc)

		self.toolbar.addAction(self.new)
		self.toolbar.addAction(self.open)
		self.toolbar.addAction(self.save)
		# separating line
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.pdf)
		self.toolbar.addAction(self.Print)
		self.toolbar.addAction(self.preview)
		# separating
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.undo)
		self.toolbar.addAction(self.redo)
		# separating
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.cut)
		self.toolbar.addAction(self.copy)
		self.toolbar.addAction(self.paste)
		# separating
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.search)
		self.toolbar.addAction(self.find)
		# separating
		self.toolbar.addSeparator()
		self.toolbar.addAction(bulletlist)
		self.toolbar.addAction(numberlist)		

		# self.toolbar.addAction(wordCount)
		# separating
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.close)	

		self.addToolBarBreak()

	def writerFormatbar(self):
		fontnames = QFontComboBox(self)
		fontnames.currentFontChanged.connect(self.fontFamily)
		# different font sizes
		fontSize = QComboBox(self)
		fontSize.setEditable(True)
		# Minimum number of chars displayed
		fontSize.setMinimumContentsLength(3)
		fontSize.activated.connect(self.FontSize)
		# Typical font sizes
		fsizelist = ['6', '7', '8', '9', '10', '10.5', '11', '12', 
					'13', '14', '15', '16', '18', '20', '22', '24',
					'26', '28', '32', '36', '40', '44', '48', '54',
					'60', '66', '72', '80', '88', '96']

		for i in fsizelist:
				fontSize.addItem(i)
		# set text colour
		fontcolor = QAction(QIcon("icons/fontcolor.png"), "Font Color", self)
		fontcolor.setStatusTip("Change font color")
		fontcolor.triggered.connect(self.fontColor)
		# set background colour
		backcolor = QAction(QIcon("icons/bckcolor.png"), "Background Color", self)
		backcolor.setStatusTip("Change background color")
		backcolor.triggered.connect(self.backColor)
		# bold text
		boldtext = QAction(QIcon("icons/bold.png"), "Bold", self)
		boldtext.triggered.connect(self.bold)
		# italic text
		italictext = QAction(QIcon("icons/italic.png"), "Italic", self)
		italictext.triggered.connect(self.italic)
		# underline the text
		underltext = QAction(QIcon("icons/under.png"), "Underline", self)
		underltext.triggered.connect(self.underline)
		# strike action
		strike = QAction(QIcon("icons/strike.png"), "Strike-out", self)
		strike.triggered.connect(self.strike)	

		superscript = QAction(QIcon("icons/super.png"), "Superscript", self)
		superscript.triggered.connect(self.superScript)

		subscript = QAction(QIcon("icons/sub.png"), "Subscript", self)
		subscript.triggered.connect(self.subScript)
		# different alignments
		alignLeft = QAction(QIcon("icons/left.png"), "Align left", self)
		alignLeft.setShortcut("Ctrl+L")
		alignLeft.triggered.connect(self.alignLeft)

		alignCenter = QAction(QIcon("icons/center.png"), "Centered", self)
		alignCenter.setShortcut("Ctrl+E")
		alignCenter.triggered.connect(self.alignCenter)

		alignRight = QAction(QIcon("icons/right.png"), "Align Right", self)
		alignRight.setShortcut("Ctrl+R")
		alignRight.triggered.connect(self.alignRight)

		alignJustify = QAction(QIcon("icons/justify.png"), "Justified", self)
		alignJustify.setShortcut("Ctrl+J")
		alignJustify.triggered.connect(self.alignJustify)
		# Increase the indent of area
		indent = QAction(QIcon("icons/indent.png"), "Increase Indent", self)
		indent.setShortcut("Ctrl+Tab")
		indent.triggered.connect(self.indent)
		# Decrease the indent of area
		dedent = QAction(QIcon("icons/dedent.png"), "Decrease Indent", self)
		dedent.setShortcut("Shift+Tab")
		dedent.triggered.connect(self.dedent)
		# Change case
		case = QAction(QIcon("icons/case.png"), "Changing case", self)
		case.triggered.connect(self.changeCase)

		self.formatbar = self.addToolBar("Format")
		self.formatbar.addWidget(fontnames)
		self.formatbar.addSeparator()
		self.formatbar.addWidget(fontSize)		
		# separating
		self.formatbar.addSeparator()
		self.formatbar.addAction(boldtext)
		self.formatbar.addAction(italictext)
		self.formatbar.addAction(underltext)
		# separating
		self.formatbar.addSeparator()
		self.formatbar.addAction(strike)
		self.formatbar.addAction(superscript)
		self.formatbar.addAction(subscript)
		# separating
		self.formatbar.addSeparator()
		self.formatbar.addAction(alignLeft)
		self.formatbar.addAction(alignCenter)
		self.formatbar.addAction(alignRight)
		self.formatbar.addAction(alignJustify)
		# separating
		self.formatbar.addSeparator()
		self.formatbar.addAction(case)
		self.formatbar.addAction(indent)
		self.formatbar.addAction(dedent) 
		# separating
		self.formatbar.addSeparator()
		self.formatbar.addAction(fontcolor)
		self.formatbar.addAction(backcolor)
		self.formatbar.addSeparator()			

	def writerMenubar(self):
		menubar = self.menuBar()
		file = menubar.addMenu('&File')
		edit = menubar.addMenu('&Edit')
		view = menubar.addMenu('&View')
		insert = menubar.addMenu('&Insert')

		file.addAction(self.new)
		file.addAction(self.open)
		file.addAction(self.save)
		file.addAction(self.pdf)
		file.addAction(self.Print)
		file.addAction(self.preview)
		file.addAction(self.close)
		edit.addAction(self.undo)
		edit.addAction(self.redo)
		edit.addAction(self.cut)
		edit.addAction(self.copy)
		edit.addAction(self.paste)
		edit.addAction(self.search)
		edit.addAction(self.find)
		# view.addAction(tog_toolbar)
		# view.addAction(tog_formatbar)
		# view.addAction(tog_statusbar)
		# insert.addAction(self.date_n_time)
		# insert.addAction(self.insertImage)
		# insert.addAction(self.table)

	def writerUI(self):
		# set text area
		self.textArea = QTextEdit()
		self.setCentralWidget(self.textArea)
		# calling toolbar method
		self.writerToolbar()
		# calling formatbar method
		self.writerFormatbar()
		# calling menubar method
		self.writerMenubar() 

		self.statusbar = self.statusBar()  # set statusbar
		self.statusbar.setSizeGripEnabled(True)

		self.resize(1030, 800)
		self.move(100, 100)			

		self.textArea.setTabStopWidth(33)  # 8 spaces
		self.textArea.cursorPositionChanged.connect(self.cursorPosition)
		self.setWindowIcon(QIcon("icons/icon.jpg"))
		self.setWindowTitle("Text Editor")

	def new_doc(self):
		# self.textArea.clear()
		newfile = Editor(self)
		newfile.show()

	def open_doc(self):	
			self.filenm = QFileDialog.getOpenFileName(self, 'Open File', ".")
			if self.filenm:
				with open(self.filenm, "rt") as file:
					self.textArea.setText(file.read())            			

	def save_doc(self):
		if not self.filenm:
			self.filenm = QFileDialog.getSaveFileName(self, 'Save File')
			with open(self.filenm, "wt") as file:
				file.write(self.textArea.toHtml())	

	def exportPdf(self):
		printer = QPrinter()
		printer.setOutputFormat(printer.NativeFormat)
		dialog = QPrintDialog(printer)
		dialog.setOption(dialog.PrintToFile)
		if dialog.exec_() == QDialog.Accepted:
			self.textArea.document().print_(dialog.printer())

	def print_doc(self):
		# opening print dialog
			dialog_box = QPrintDialog()
			if dialog_box.exec_() == QDialog.Accepted:
				self.textArea.document().print_(dialog_box.printer())

	def preview_doc(self):
		pageview = QPrintPreviewDialog()
		pageview.paintRequested.connect(self.textArea.print_)
		pageview.exec_()	

	def bulletList(self):
		textcursor = self.textArea.textCursor()
		textcursor.insertList(QTextListFormat.ListDisc)

	def numberedList(self):
		textcursor = self.textArea.textCursor()
		textcursor.insertList(QTextListFormat.ListDecimal)

	def close_doc(self):
		self.hide()		

	def closeEvent(self, event):
		msg_box = QMessageBox.question(self, 'Save the document before closing?',
					"If you don't save, changes will be permanently lost.", 
					QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if msg_box == QMessageBox.Yes:
			event.accept()
			self.save_doc()
		else:
			event.ignore()    

	def fontFamily(self, font):
		font = QtGui.QFont(self.fontFamily.currentFont())
		self.text.setCurrentFont(font)

	def FontSize(self, fontsize):
		self.textArea.setFontPointSize(int(fontsize))

	def fontColor(self):
		# select colour from color dialog
			textcolor = QColorDialog.getColor()
		# Setting new text color
			self.textArea.setTextColor(textcolor)

	def backColor(self):
		bckcolor = QColorDialog.getColor()
		# after selecting,setting new bckcolor 
		self.textArea.setTextBackgroundColor(bckcolor)

	def bold(self):
		b = self.textArea.fontWeight()
		if b is QFont.Normal:
			self.textArea.setFontWeight(QFont.Bold)
		else:
			self.textArea.setFontWeight(QFont.Normal)

	def italic(self):
		i = self.textArea.fontItalic()
		if i is False:
			self.textArea.setFontItalic(True)
		else:
			self.textArea.setFontItalic(False)

	def underline(self):
		u = self.textArea.fontUnderline()
		if u is False:
			self.textArea.setFontUnderline(True) 
		else:
			self.textArea.setFontUnderline(False)

	def strike(self):
		ftxt = self.textArea.currentCharFormat()
		ftxt.setFontStrikeOut(not ftxt.fontStrikeOut())
		self.textArea.setCurrentCharFormat(ftxt)

	def superScript(self):
		ftxt = self.textArea.currentCharFormat()
		alignment = ftxt.verticalAlignment()
		if alignment is QTextCharFormat.AlignNormal:
			ftxt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
		else:
			ftxt.setVerticalAlignment(QTextCharFormat.AlignNormal)
			self.textArea.setCurrentCharFormat(ftxt)

	def subScript(self):
		ftxt = self.textArea.currentCharFormat()
		alignment = ftxt.verticalAlignment()
		if alignment is QTextCharFormat.AlignNormal:
			ftxt.setVerticalAlignment(QTextCharFormat.AlignSubScript)
		else:
			ftxt.setVerticalAlignment(QTextCharFormat.AlignNormal)
			self.textArea.setCurrentCharFormat(ftxt)

	def alignLeft(self):
		self.textArea.setAlignment(Qt.AlignLeft)

	def alignRight(self):
		self.textArea.setAlignment(Qt.AlignRight)

	def alignCenter(self):
		self.textArea.setAlignment(Qt.AlignCenter)

	def alignJustify(self):
		self.textArea.setAlignment(Qt.AlignJustify)

	def changeCase(self):
		ftxt = self.textArea.currentCharFormat()
		fmt1 = QTextCharFormat()
		fmt1.setFontCapitalization(QFont.AllUppercase)
		self.textArea.setCurrentCharFormat(fmt1)

	def indent(self):
		cur = self.textArea.textCursor()
		if cur.hasSelection():
			temp = cur.blockNumber()
			cur.setPosition(cur.selectionEnd())
			# Calculate range of selection
			diff = cur.blockNumber() - temp

			for n in range(diff + 1):
				cursor.movePosition(QTextCursor.StartOfLine)
				cursor.insertText("\t")
				# move back up
				cursor.movePosition(QTextCursor.Up)

			else:
				cursor.insertText("\t")

	def dedent(self):
		cur = self.textArea.textCursor()
		if cur.hasSelection():
			temp = cur.blockNumber()
			cursor.setPosition(cur.selectionEnd())
			# Calculate range of selection
			diff = cur.blockNumber() - temp

			for n in range(diff + 1):
				self.handleDedent(cursor)
				cursor.movePosition(QTextCursor.Up)

			else:
				self.handleDedent(cursor)

	def handleDedent(self, cursor):
		cur.movePosition(QTextCursor.StartOfLine)
		# Grab the current line
		line = cur.block().text()
		# If the line starts with a tab character, delete it
		if line.startsWith("\t"):
		# Delete next character
			cur.deleteChar()
		# delete all spaces until a non-space character is met
		else:
			for char in line[:8]:
				if char != " ":
					break
				cur.deleteChar()

	def cursorPosition(self):
		line = self.textArea.textCursor().blockNumber()
		col = self.textArea.textCursor().columnNumber()
		self.statusbar.showMessage("Ln {}, Col {}".format(line, col))


def main():
	app = QApplication(sys.argv)
	editor = Editor()
	editor.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
