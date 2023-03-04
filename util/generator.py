from itertools import permutations
import json
from random import choice

restult = {}
all_colors = ['red', 'blue', 'green', 'yellow', 'white']

for correct_color in all_colors:

    text_color = correct_color
    remaining_colors = list(filter(lambda x: x != correct_color, all_colors))
    all_permutations = list(permutations(remaining_colors, 2))

    for permutation in all_permutations:

        text = permutation[0]
        background_color = permutation[1]

        if text_color not in restult.keys():
            restult[text_color] = []

        restult[text_color].append([text.upper(), text_color, background_color])

with open('all_combinations.json', 'w') as f:
    f.write(json.dumps(restult))
