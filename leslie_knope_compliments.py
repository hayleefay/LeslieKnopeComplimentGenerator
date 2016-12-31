'''
A geneartor for Leslie Knope-ish compliments.
'''

import random
import requests
import time
random.seed(time.time())

name = input("Who are you? ")

nouns = ["baby", "pony", "starburst", "fox", "platypus", "rainbow", "lollipop", \
"banana", "bear", "cub", "librarian", "lightbulb", "cloud", "shrub", \
"flower", "giraffe", "gemstone", "blanket", "sapling", "cucumber", "puppy", \
"potato", "trash"]

noun = random.choice(nouns)

url = 'http://api.datamuse.com/words?rel_jjb={noun}&max=5&topics=lovely'.format(noun = noun)
response = requests.get(url)
adj = response.json()

list_of_adj = []

for word in adj:
    list_of_adj.append(word['word'])

print(name + ",", "you", ", ".join(list_of_adj), noun + "!")
