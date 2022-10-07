import json

"""
Takes word data from a large dataset of english sentences.
Determines the probabilities of the next words.
When a word is entered, a next word is generated based on the most probable following word
"""

with open('word_predictor/word_data.json') as file:
    data = json.load(file)
print(data)
inp = input("Enter word: ")
if inp in data:
    print(data[inp][0])