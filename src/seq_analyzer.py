"""
--Seqence Analyzer File--

Analyses a sequence for substrings
only has one function that will be called statically from the seq_gui.py file.

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde"
__credits__         = "Scott Howes, Braeden Van Der Velde"
__email__           = "showes@unbc.ca, "
__python_version__  = "3.9.0"


#imports go here


#the seq_analyzer class
class seq_analyzer:


    #the analyser function
    #find all substring of a min and max length and of a minimum occurance in Sequence
    #returns a list of lists
    def mineSequence(self, sequence, minLength, maxLength, minOccurance):

        #list of substrings to return
        substrings = []

        print(f"sequence: {sequence}\nminimum substring length: {minLength}\nmaximum substring length: {maxLength}\nminOcc: {minOccurance}", flush=True)
