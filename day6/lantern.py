import numpy as np

inputs = open('input', 'r')

fish = [int(x.strip()) for x in inputs.read().split(',')]
fish_dict = {}

fish_dict[-1] = 0
for i in range(9):
    fish_dict[i] = sum([1 if x==i else 0 for x in fish])

for iteration in range(256):
    new_fishes = fish_dict[0]
    for i in range(0,9):
        fish_dict[i-1] = fish_dict[i]
    fish_dict[8] = new_fishes
    fish_dict[6] += fish_dict[-1]
    fish_dict[-1] = 0

total = 0
for i in range(-1,9):
    total+=fish_dict[i]
print(total)