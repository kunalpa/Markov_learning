"""
Create a count hashmap (word: {total_count: int, next_word1: count, nextword2: count, ...})
Create a global probability hasMap (word: [(next_word1, p), (nextword2, p), ...])
"""

import os

prob_map = {}

def populate_count_map(filename):
    file = open(filename, "r")

    for line in file:
        line_list = line.split()

        for word_index, word in enumerate(line_list[:-1]):
            next_word = line_list[word_index+1]
            if word in count_map:
                if next_word in count_map[word]:
                    count_map[word][next_word] += 1
                else:
                    count_map[word][next_word] = 1
                count_map[word]["total_count"] += 1
            else:
                count_map[word] = {"total_count": 1, next_word: 1}

    file.close()

def populate_sorted_prob_map():
    # Finds prob of each next word and sorts in descending order
    for word in count_map:
        prob_map[word] = []
        total_count = count_map[word]["total_count"]
        for next_word in count_map[word]:
            if next_word != "total_count":
                p = count_map[word][next_word]/total_count
                prob_map[word].append((next_word, p))

        prob_map[word].sort(key=lambda x: x[1], reverse=True)

def main():
    global count_map
    global prob_map
    count_map = {}
    prob_map = {}

    for file in os.listdir("text_docs"):
        f = "text_docs/" + file
        populate_count_map(f)
    
    populate_sorted_prob_map()

if __name__ == "__main__":
    main()