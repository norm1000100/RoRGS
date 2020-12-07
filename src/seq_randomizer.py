"""
--Sequence Randomizer File--

This file contains one class, seq_randomizer. Takes in a sequence, and randomizes it
while maintaining same amino acid chain. randomize() is the only public function

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
        # generate random number generator
        random.seed(datetime.now())
        # make the codon tables
        self.codon_table = CodonTable.CodonTable()


    # parse out codon sequences
    def _codonParse(self, sequence):
        codons = []
        if len(sequence) % 3 > 0:
            sequence = sequence[: len(sequence) - (len(sequence) % 3)]
        for i in range(0, len(sequence), 3):
            codons.append(sequence[i:i + 3])
        return codons


    # input raw dna sequence, randomize codons
    def randomize(self, sequence, percent):

        # Parse the codons into list
        codons = self._codonParse(sequence)

        # empty string to create return string
        randomized = ""

        # for all codons in the codon list
        for codon in codons:

            # if random number less than percent of randomness
            if random.randint(1, 100) <= percent:

                # lookup protein value from table
                protein = self._codonLookup(codon)

                # Get a list of compatible codons
                replacements = self._proteinList(protein)

                # if the list of codons is greater than one
                if len(replacements) > 1:

                    # remove the original codon from the list
                    replacements.remove(codon)

                    # pick a random codon to replace it with
                    randomized += replacements[random.randint(0, len(replacements)) - 1]

                else:

                    # if there is only one codon in the replacements, just use that one
                    randomized += replacements[0]
            else:

                # if the random number is greater than %, just use the original codon
                randomized += codon
                
        # return the completed randomized codon sequence.
        return randomized


    # lookup the specific codon's protein
    def _codonLookup(self, codon):
        return self.codon_table.codon_to_protein[codon]


    # return a list containing codons for a specific protein
    def _proteinList(self, protein):
        protein_sub = self.codon_table.protein_to_codon[protein].copy()
        return protein_sub
