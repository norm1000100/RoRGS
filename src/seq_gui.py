"""
--main Gui File--

The gui class creates the functionality for the gui.ui file.

Allows a user to graphically import a seqence, analyze that seqence then
randomize as needed. Not very much error handling implemented so far.

Currently underdevelopment

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde"
__credits__         = "Scott Howes, Braeden Van Der Velde"
__email__           = "showes@unbc.ca, velde@unbc.ca"
__python_version__  = "3.9.0"


#imports
import sys
import os
from seq_analyzer import seq_analyzer
from seq_randomizer import seq_randomizer
from Bio.SeqUtils import GC
from Bio.Seq import Seq
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


#the seq_gui class
class seq_gui(QWidget):


    #constructor
    def __init__(self):
        super(seq_gui, self).__init__()
        loadUi("GUIs/gui.ui", self)
        self._load_connects()
        self.move(20,20)
        self.randomizer = seq_randomizer()


    #loads the connection for the buttons
    def _load_connects(self):

        #bttn_create connects
        self.bttn_openSeq.clicked.connect(self.bttn_openSeq_clicked)
        self.bttn_save.clicked.connect(self.bttn_save_clicked)
        self.bttn_clearSeq.clicked.connect(self.bttn_clearSeq_clicked)
        self.bttn_randomize.clicked.connect(self.bttn_randomize_clicked)
        self.bttn_analyze.clicked.connect(self.bttn_analyze_clicked)


    #creates the functionality for the Open button
    @pyqtSlot()
    def bttn_openSeq_clicked(self):
        path, _ = QFileDialog.getOpenFileName(None, "Load Sequence", "", "Text Files (*.txt)")
        if path:
            file = open(path, "r")
            contents = file.read()
            self.textEdit_seq.setText(contents)


    #creates the functionality for the Save button
    @pyqtSlot()
    def bttn_save_clicked(self):
        path, _ = QFileDialog.getSaveFileName(None, "Save Sequence", "", "*.txt")
        if path:
            file = open(path, "w+")
            contents = self.textEdit_seq.toPlainText()
            file.write(contents)
            file.close()


    #creates the functionality for the clear button
    @pyqtSlot()
    def bttn_clearSeq_clicked(self):
        self.textEdit_seq.clear()


    #creates the functionality for the Randomize button
    @pyqtSlot()
    def bttn_randomize_clicked(self):

        #getting the sequence
        seq = self.textEdit_seq.toPlainText()

        #making seq uppercase
        seq = seq.upper()

        #valid character check
        if self._seqCheck(seq):

            #getting the randomization percentage
            randPercent = int(self.label_rand.text())

            #getting amino chain from original sequence
            proteinSeq = Seq(seq)
            oldAnimoChain = str(proteinSeq.translate())

            #randomiztion process
            newSeq = self.randomizer.randomize(seq, randPercent)

            #getting new amino chain
            newProteinSeq = Seq(newSeq)
            newAnimoChain = str(newProteinSeq.translate())

            #comparing chains
            #and updating textedit field and analyzing
            if newAnimoChain == oldAnimoChain:
                self.textEdit_seq.setText(newSeq)
                self._analyzeSequence(newSeq)
            else:
                self._errorMessage("Animo Acid Chain MisMatch")
                self.textEdit_aminoSeq.setText("Animo Acid Chain MisMatch!")

        else:
            #Error Message
            self._errorMessage("Invalid Characters detected in Sequence.")


    #creates the functionality for the Analyze Sequence button
    @pyqtSlot()
    def bttn_analyze_clicked(self):

        #getting the sequence from the text edit boxn
        seq = self.textEdit_seq.toPlainText()

        #making seq upper case
        seq = seq.upper()

        #checking for valid valid characters
        if self._seqCheck(seq):
            #calling private analysis functionality
            self._analyzeSequence(seq)

        else:
            #Error Message
            self._errorMessage("Invalid Characters detected in Sequence.")


    #This function does the analysis on the Sequence in textEdit_seq
    def _analyzeSequence(self, sequence):

        #getting sequence length and adding it to character count
        self.label_charVal.setText(str(len(sequence)))

        #getting GC richness using biopython
        self.label_gcVal.setText(str(round(GC(sequence), 2)))

        #getting Amino Acid composition
        protein_seq = Seq(sequence)
        self.textEdit_aminoSeq.setText(str(protein_seq.translate()))

        #using seq_analyzer to mine Sequence, returns list of lists
        substrings = seq_analyzer.mineSequence(self, sequence, int(self.label_minSubSize.text()), int(self.label_maxSubSize.text()), int(self.label_minOccVal.text()))

        #filling the table
        self._populateTable(substrings)


    #populates the table_subString
    def _populateTable(self, list):

        #clearing the table
        self.table_subString.setRowCount(0)

        #setting the row count to start adding info
        row = 0

        #setting the row count to the number of items
        self.table_subString.setRowCount(len(list))

        #adding items
        for strings in list:
            self.table_subString.setItem(row , 0, QTableWidgetItem(str(strings[0])))
            self.table_subString.setItem(row , 1, QTableWidgetItem(str(strings[1])))
            self.table_subString.setItem(row , 2, QTableWidgetItem(str(strings[2])))
            row = row + 1

        #sorting items by % of sequence
        self.table_subString.sortItems(2, Qt.DescendingOrder)


    #Error Message function
    #only parameter is a string which is the Message
    def _errorMessage(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error Message Box")
        msg.setIcon(QMessageBox.Warning)
        msg.setText("<b>----- AN ERROR HAS OCCURED -----</b>")
        msg.setInformativeText(message)
        msg.exec()


    #this function check that a sequence is only composed of G's C's A's T's
    #not very efficient but does the job
    def _seqCheck(self, sequence):
        validChars = "GCAT"
        return all(chars in validChars for chars in sequence)
