
import json
from collections import defaultdict
import pandas as pd

# corpus = []

# for elem in data1:
#     keyPhrases = elem.get("keyPhrases")
#     corpus.extend(keyPhrases)

# for elem in data2:
#     keyPhrases = elem.get("keyPhrases")
#     corpus.extend(keyPhrases)

# for elem in data3:
#     keyPhrases = elem.get("keyPhrases")
#     corpus.extend(keyPhrases)

# # convert to lower case
# corpus = [item.lower() for item in corpus]

# # send to dict
# uniq_counts = defaultdict(int)
# for elem in corpus:
#     uniq_counts[elem] += 1

# data = pd.DataFrame.from_dict(data=uniq_counts, orient='index')

# data.to_csv("./all_counts.csv")


def load(file):
    param =  "./" + file + ".json"
    with open(param) as data:
        return json.load(data).get("documents")

data1 = load("keywords1")
data2 = load("keywords2")
data3 = load("keywords3")

# data_list = [data1, data2, data3]

# words = ['years', 'home', 'world', 'city', 'love', 'new people', 'university of washington', 'wonderful city', 'life motto', 'interior designer']

# selected words with generic top words removed
words = [ 'love', 'new people', 'wonderful city', 'life motto', 'interior designer']

output = {}

for elem in data1:
    cur_id = elem.get("id")
    cur_keywords = elem.get("keyPhrases")
    intersection = len(list(set(words).intersection(cur_keywords)))
    output[cur_id] = intersection


for elem in data2:
    
    cur_id = elem.get("id")
    cur_keywords = elem.get("keyPhrases")
    intersection = len(list(set(words).intersection(cur_keywords)))
    output[cur_id] = intersection

for elem in data3:

    cur_id = elem.get("id")
    cur_keywords = elem.get("keyPhrases")
    intersection = len(list(set(words).intersection(cur_keywords)))
    output[cur_id] = intersection


data = pd.DataFrame.from_dict(data=output, orient='index')

data.to_csv("./output.csv")
