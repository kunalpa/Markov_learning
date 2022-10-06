import imp
import numpy as np
from matplotlib import pyplot as plt
from word_predictor.populate_probabilities import prob_map

"""
Takes word data from a large dataset of english sentences.
Determines the probabilities of the next words.
When a word is entered, a next word is generated based on the most probable following word
"""

inp = input("Enter word: ")
if inp in prob_map:
    print(prob_map[inp][0])