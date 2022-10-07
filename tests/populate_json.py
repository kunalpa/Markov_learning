from word_predictor.populate_word_data import *

# testing is less rigorous due to time restrictions
# normally I would invert control and inject all parameters.
# However, I have control over the whole project, so I won't do that

# testing populate_count_map()
# testing data is stored in text_docs/tests
curr_path = os.path.dirname(__file__)
file1 = 'C:/Users/Kunal Pathak/Desktop/cs/Extra Work/PersonalProjects/Markov_Learning/text_docs/tests/test0.txt'
file2 = 'C:/Users/Kunal Pathak/Desktop/cs/Extra Work/PersonalProjects/Markov_Learning/text_docs/tests/test3.txt'

# print(populate_count_map(file1, count_map={}))
def test_count_map1():
    expected_map = {'can': {'total_count': 1, 'is': 1}, 'no': {'total_count': 1, 'thanks': 1}, 'hello': {'total_count': 1, 'world': 1}}
    assert expected_map == populate_count_map(file1, count_map={})

def test_count_map2():
    expected_map = {'hello': {'total_count': 1, 'I': 1}, 'I': {'total_count': 2, 'like': 1, 'want': 1}, 'like': {'total_count': 1, 'cheese': 1}, 'want': {'total_count': 1, 'to': 1}, 'to': {'total_count': 1, 'eat': 1}, 'eat': {'total_count': 1, 'cheese': 1}, 'Cheese': {'total_count': 1, 'is': 1}, 'is': {'total_count': 1, 'my': 1}, 'my': {'total_count': 1, 'favorite': 1}}
    assert expected_map == populate_count_map(file2, count_map={})



# testing create_sorted_prob_map()

sample_count_map1 = {'hello': {'total_count': 2, 'world': 1, 'people': 1}}
sample_count_map2 = {'hello': {'total_count': 3, 'world': 2, 'people': 1}}
sample_count_map3 = {'hello': {'total_count': 4, 'world': 1, 'people': 3}}
# don't want to create large hashMap, so I will test count map, and use those results assuming they are correct

def test_prob_1():
    assert create_sorted_prob_map(sample_count_map1) == {'hello': [['world', 0.5], ['people', 0.5]]}

def test_prob_2():
    assert create_sorted_prob_map(sample_count_map2) == {'hello': [['world', 2/3], ['people', 1/3]]}

def test_prob_sort():
    assert create_sorted_prob_map(sample_count_map3) == {'hello': [['people', 0.75], ['world', 0.25]]}

test_prob_1()
test_prob_2()
test_prob_sort()
test_count_map1()
test_count_map2()