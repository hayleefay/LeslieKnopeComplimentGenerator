from collections import defaultdict
from leslie_data import get_leslie_quotes
import random
import json

try:
    table = json.load(open('table.json'))
except:
    # get data
    leslie_quotes = get_leslie_quotes()

    # create table
    table = defaultdict(list)

    word1 = None
    word2 = None

    for quote in leslie_quotes:
        for word in quote.split():
            word1 = word2
            word2 = word

            if word1 is None:
                continue
            else:
                table[word1].append(word2)

    with open('table.json', 'w') as fp:
        json.dump(table, fp)

# create output
first_word = None
second_word = None
sentence = ''
num_sentences = 0
ending_punct = ['.', '!', '?']

while num_sentences < 3:
    if second_word in table:
        second_word = random.choice(table[second_word])
        sentence += second_word + ' '
        for letter in second_word:
            if letter in ending_punct:
                num_sentences += 1
                break
    else:
        while first_word is None or first_word[0].islower():
            first_word = random.choice(list(table))
        second_word = random.choice(table[first_word])
        sentence += first_word + ' ' + second_word + ' '
        for letter in first_word + second_word:
            if letter in ending_punct:
                num_sentences += 1
                break

print(sentence)
