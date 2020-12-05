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
class Seq_Randomizer:

    # constructor
    def __init__(self):
        random.seed(datetime.now())  # generate random number generator
        self.codon_table = CodonTable.CodonTable()

    def _codonParse(self, sequence):  # parse out codon sequences
        codons = []
        if len(sequence) % 3 > 0:
            sequence = sequence[: len(sequence) - (len(sequence) % 3)]
        for i in range(0, len(sequence), 3):
            codons.append(sequence[i:i + 3])
        return codons

    def randomize(self, sequence, percent):  # input raw dna sequence, randomize codons
        codons = self._codonParse(sequence)
        randomized = ""
        for codon in codons:
            if random.randint(1, 100) <= percent:
                protein = self._codonLookup(codon)
                replacements = self._proteinList(protein)
                if len(replacements) > 1:
                    replacements.remove(codon)
                    randomized += replacements[random.randint(0, len(replacements)) - 1]
                else:
                    randomized += replacements[0]
            else:
                randomized += codon
        return randomized

    def _codonLookup(self, codon):
        return self.codon_table.codon_to_protein[codon]

    def _proteinList(self, protein):
        protein_sub = self.codon_table.protein_to_codon[protein].copy()
        return protein_sub
