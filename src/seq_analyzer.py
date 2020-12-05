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


#the seq_analyzer class
class seq_analyzer:


    #the analyser function
    #find all substring of a min and max length and of a minimum occurance in Sequence
    #returns a list of lists
    def mineSequence(self, sequence, minLength, maxLength, minOccurance):

        #list of substrings to return
        substrings = []

        #the length of the sequence
        length = len(sequence)

        #this chuck of code parses iterates through the sequence for substrings
        #and adds them to substrings list
        while minLength <= maxLength:
            index = 0
            temp = minLength
            while temp <= length:
                substring = []
                string = sequence[index: temp]
                substrings.append(string)
                index = index + 1
                temp = temp + 1
            minLength = minLength + 1

        #converting substrings list to set to remove duplicates
        substringSet = set(substrings)

        newSubstrings = []

        #iterates through substringSet
        #calculates count, and percentage of string
        for strings in substringSet:
            tempList = []

            #calculating substring count
            stringCount = sequence.count(strings)

            #calculating how the percentage of the sequence the string takes
            stringPercent = round(((len(strings)*stringCount)/length)*100,2)

            #creating the subtring list with info
            #(substring, count, percentage)
            tempList.append(strings)
            tempList.append(stringCount)
            tempList.append(stringPercent)

            #only adds templist to substring list if minOccurance is met
            if stringPercent >= minOccurance:
                newSubstrings.append(tempList)


        #creating a set to remove duplicates
        #substringSet = set(substrings)
        return newSubstrings
