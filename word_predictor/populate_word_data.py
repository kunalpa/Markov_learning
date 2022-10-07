"""
Create a count hashmap (word: {total_count: int, next_word1: count, nextword2: count, ...})
Create a global probability hasMap (word: [(next_word1, p), (nextword2, p), ...])
"""

import os
import json


def populate_count_map(filename, count_map):
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
    return count_map

def create_sorted_prob_map(count_map):
    # Finds prob of each next word and sorts in descending order
    prob_map = {}
    for word in count_map:
        prob_map[word] = []
        total_count = count_map[word]["total_count"]
        for next_word in count_map[word]:
            if next_word != "total_count":
                p = count_map[word][next_word]/total_count
                prob_map[word].append([next_word, p])

        prob_map[word].sort(key=lambda x: x[1], reverse=True)
    return prob_map

def main():
    count_map = {}
    for file in os.listdir("text_docs/tests"):
        f = "text_docs/tests/" + file
        populate_count_map(f, count_map)
    prob_map = create_sorted_prob_map(count_map)
    print(count_map)
    # write to json
    with open("word_predictor/word_data.json", "w") as file_out:
        json.dump(prob_map, file_out)
    file_out.close()

if __name__ == "__main__":
    main()