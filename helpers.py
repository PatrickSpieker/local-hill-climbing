import random
import sys

def create_array():
    items = [random.randint(-sys.maxsize, sys.maxsize)]
    for i in range(1, 1000):
        candidate = random.randint(-sys.maxsize, sys.maxsize)
        while candidate == items[i-1]:
            candidate = random.randint(-sys.maxsize, sys.maxsize)
        items.append(candidate)
    return items