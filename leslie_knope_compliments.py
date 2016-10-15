'''
A geneartor for Leslie Knope-ish compliments.
'''

import random

name = input("Who are you? ")

adj = ["gorgeous,", "voluptuous,", "elusive,", "spirited,", "clever,", "brilliantly radiant,", "fertile,",\
"subtle,", "seductive,", "simple,", "wise,", "persistent,", "trembling,", "insatiable,", "purebred,"]

noun = ["land mammal", "baby", "baby owl", "starburst", "fox", "platypus", "rainbow", "lollipop", "horse's mane", \
"sundial"]

print(name + ",", "you", random.choice(adj), random.choice(adj), random.choice(adj), random.choice(noun) + "!")