import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from collections import Counter


def rng():
    total = 0
    items = 0
    z = random.randint(1, 10)
    if z == 1:  # no CPU can regen
        a = 16
    if 2 <= z <= 5:  # 1 CPU can regen
        a = 17
    else:  # 2 CPUs regen
        a = 18
    while total < a:
        x = random.randint(1, 200)
        if 1 <= x <= 80:  # red shell
            total += 1
        if 81 <= x <= 105:  # star
            y = random.randint(1, 2)
            if y == 1:
                total += 2
            else:
                total += 3
        if 106 <= x <= 125:  # triple red shell
            total += 3
        if 126 <= x <= 140:  # boo
            total += 0
        if 141 <= x <= 153:  # triple mushroom
            total += 0
        if 154 <= x <= 163:  # green shell
            y = random.randint(1, 4)
            if y == 1:
                total += 1
            else:
                total += 0
        if 164 <= x <= 173:  # bob-omb
            y = random.randint(1, 10)
            if y <= 4:
                total += 0
            elif 5 <= y <= 9:
                total += 1
            else:
                total += 2
        if 174 <= x <= 183:  # triple green shell
            y = random.randint(1, 10)
            if y <= 2:
                total += 0
            elif 3 <= y <= 9:
                total += 1
            else:
                total += 2
        if 184 <= x <= 193:  # blooper
            total += 0
        if 194 <= x <= 198:  # golden mushroom
            total += 0
        else:  # single mushroom
            total += 0
        items += 1
    return items


def main():
    my_list = []
    for i in range(5000000):
        my_list.append(rng())
    my_set = set(my_list)
    avg = sum(my_list) / len(my_list)
    std = np.std(my_list)
    print(f'Item boxes needed to win a balloon battle:\n'
          f'Number of trials: {len(my_list)}\n'
          f'Average: {avg}\n'
          f'Standard deviation: {std}\n'
          f'Median: {np.median(my_list)}\n'
          f'Minimum: {min(my_list)}\n'
          f'Maximum: {max(my_list)}')

    figure(figsize=(20, 8), dpi=100)
    plt.hist(my_list, bins=len(my_set), color='seagreen')
    plt.title('Number of Items Needed to Win Balloon Battle')
    plt.xlabel('# of Items')
    plt.ylabel('count')
    plt.savefig('balloon.png')
    plt.show()

    print(f'{Counter(my_list).keys()}')
    print(f'{Counter(my_list).values()}')


main()
