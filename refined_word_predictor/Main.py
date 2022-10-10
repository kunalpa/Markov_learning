import markovify
import re
import markovify
import os

def getCleanText(filename):
    with open(filename, encoding='utf8') as file:
        file_text = file.read()
    return file_text

def create_markov(text):
    return markovify.Text(text)

def main():
    all_texts = ""
    for file in os.listdir('refined_word_predictor/book_texts'):
        filename = 'refined_word_predictor/book_texts/' + file
        book_text = getCleanText(filename)
        all_texts += book_text
    
    sentence_markov = create_markov(all_texts)

    for i in range(5):
        print(sentence_markov.make_short_sentence(50))
        
if __name__ == "__main__":
    main()