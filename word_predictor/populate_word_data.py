"""
Create a count hashmap (word: {total_count: int, next_word1: count, nextword2: count, ...})
Create a global probability hasMap (word: [(next_word1, p), (nextword2, p), ...])
"""

import json
from operator import index
from bs4 import BeautifulSoup
import requests

def create_text_doc(site):
    soup = BeautifulSoup(requests.get(site).text, 'html.parser')
    text = soup.get_text()
    with open("text_docs/site_file.txt", "w") as file_out:
        json.dump(text, file_out)

def populate_count_map(filename, count_map):
    file = open(filename, "r")

    for line in file:
        line_list = line.split()
        # appending values to count_map
        for word_index, word in enumerate(line_list[:-1]):
            next_word = line_list[word_index+1]

            if '\\' in next_word or '\\' in word:
                continue
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

def clean_map(prob_map):
    # only append probabilities that are relevant
    prob_map_copy = {}
    threshold_prob = 0.1
    for key in prob_map:

        if len(prob_map[key]) > 1:
            prob_lst = []
            for tup in prob_map[key]:
                if tup[1] > threshold_prob: prob_lst.append(tup)

            if len(prob_lst) > 0:
                prob_map_copy[key] = prob_lst

    return prob_map_copy

def main(sites):
    count_map = {}
    for site in sites:
        create_text_doc(site)
        file = 'text_docs/site_file.txt'
        populate_count_map(file, count_map)

    prob_map = create_sorted_prob_map(count_map)
    prob_map = clean_map(prob_map)
    # write to json
    with open("word_predictor/word_data.json", "w") as file_out:
        json.dump(prob_map, file_out)
    file_out.close()

if __name__ == "__main__":
    sites = [
        'https://www.nbcnews.com/news/world/isis-syria-al-hol-camp-population-reduced-biden-administration-plan-rcna50877',
        'https://www.nbcnews.com/politics/2022-election/abortion-bombshell-rocks-georgia-senate-race-neither-candidate-wants-d-rcna51127',
        'https://www.nbcnews.com/politics/joe-biden/biden-warns-risk-nuclear-armageddon-highest-cuban-missile-crisis-rcna51146',
        'https://www.nbcnews.com/tech/internet/far-right-influencers-are-targeting-individual-doctors-rcna49701',
        'https://www.nbcnews.com/news/nbcblk/killings-rappers-are-just-hip-hop-problem-experts-say-rcna51032',
        'https://www.nbcnews.com/news/us-news/trinity-teen-solutions-wyoming-ranch-closes-abuse-allegations-rcna50762',
        'https://imsdb.com/scripts/Air-Force-One.html',
        'https://imsdb.com/scripts/Joker.html',
        'https://imsdb.com/scripts/BlacKkKlansman.html',
        'https://imsdb.com/scripts/Coco.html',
        'https://imsdb.com/scripts/Thor-Ragnarok.html',
        'https://imsdb.com/scripts/Big-Sick,-The.html',
        'https://imsdb.com/scripts/American-Beauty.html',
        'https://imsdb.com/scripts/Breakfast-Club,-The.html',
        'https://imsdb.com/scripts/Sex,-Lies-and-Videotape.html'
    ]
    main(sites)
