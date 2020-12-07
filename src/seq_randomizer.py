"""
--Seqence Randomizer File--

Just a place holder at the moment

"""

# Metadata
__author__ = "Braeden Van Der Velde, Scott Howes"
__credits__ = "Braeden Van Der Velde, Scott Howes"
__email__ = "velde@unbc.ca, showes@unbc.ca"
__python_version__ = "3.9.0"

# imports go here
import CodonTable
import random
from datetime import datetime


# the seq_randomizer class
class seq_randomizer:

    # constructor
    def __init__(self):
        random.seed(datetime.now())  # generate random number generator
        self.codon_table = CodonTable.CodonTable()  # make the codon tables

    def _codonParse(self, sequence):  # parse out codon sequences
        codons = []
        if len(sequence) % 3 > 0:
            sequence = sequence[: len(sequence) - (len(sequence) % 3)]
        for i in range(0, len(sequence), 3):
            codons.append(sequence[i:i + 3])
        return codons

    def randomize(self, sequence, percent):  # input raw dna sequence, randomize codons
        codons = self._codonParse(sequence)  # Parse the codons into list
        randomized = ""  # empty string to create return string
        for codon in codons:  # for all codons in the codon list
            if random.randint(1, 100) <= percent:  # if random number less than percent of randomness
                protein = self._codonLookup(codon)  # lookup protein value from table
                replacements = self._proteinList(protein)  # Get a list of compatible codons
                if len(replacements) > 1:  # if the list of codons is greater than one
                    replacements.remove(codon)  # remove the original codon from the list
                    randomized += replacements[random.randint(0, len(replacements)) - 1]  # pick a random codon to replace it with
                else:
                    randomized += replacements[0]  # if there is only one codon in the replacements, just use that one
            else:
                randomized += codon  # if the random number is greater than %, just use the original codon
        return randomized  # return the completed randomized codon sequence.

    def _codonLookup(self, codon):  # lookup the specific codon's protein
        return self.codon_table.codon_to_protein[codon]

    def _proteinList(self, protein):  # return a list containing codons for a specific protein
        protein_sub = self.codon_table.protein_to_codon[protein].copy()
        return protein_sub
