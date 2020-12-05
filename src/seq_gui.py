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
from Bio.SeqUtils import GC
from Bio.Seq import Seq
from PyQt5.QtWidgets import QFileDialog
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
        print("open button clicked", flush=True)
        path, _ = QFileDialog.getOpenFileName(None, "Load Sequence", "", "Text Files (*.txt)")
        if path:
            file = open(path, "r")
            contents = file.read()
            self.textEdit_seq.setText(contents)


    #creates the functionality for the Save button
    @pyqtSlot()
    def bttn_save_clicked(self):
        print("save button clicked", flush=True)
        path, _ = QFileDialog.getSaveFileName(None, "Save Sequence", "", "*.txt")
        if path:
            file = open(path, "w+")
            contents = self.textEdit_seq.toPlainText()
            file.write(contents)
            file.close()


    #creates the functionality for the clear button
    @pyqtSlot()
    def bttn_clearSeq_clicked(self):
        print("clear button clicked", flush=True)
        self.textEdit_seq.clear()


    #creates the functionality for the Randomize button
    @pyqtSlot()
    def bttn_randomize_clicked(self):
        print("randomize button clicked", flush=True)

        #get Sequence from textEdit_seq
        #randomize Sequence based on Randomization percentage
        #display new sequence in texyEdit_seq
        #auto run analysis
        #compares previous sequence Amino Acid chain with new sequence amino Acid
        #chain to ensure randomization worked


    #creates the functionality for the Analyze Sequence button
    @pyqtSlot()
    def bttn_analyze_clicked(self):

        #getting the sequence from the text edit boxn
        seq = self.textEdit_seq.toPlainText()

        #calling private analysis functionality
        self._analyzeSequence(seq)


    #This function does the analysis on the Sequence in textEdit_seq
    def _analyzeSequence(self, sequence):

        #getting sequence length and adding it to character count
        self.label_charVal.setText(str(len(sequence)))

        #getting GC richness using biopython
        self.label_gcVal.setText(str(GC(sequence)))

        #getting Amino Acid composition
        protien_seq = Seq(sequence)
        self.textEdit_aminoSeq.setText(str(protien_seq.translate()))

        #using seq_analyzer to mine Sequence, returns list of lists
        seq_analyzer.mineSequence(self, sequence, int(self.label_minSubSize.text()), int(self.label_maxSubSize.text()), int(self.label_minOccVal.text()))
