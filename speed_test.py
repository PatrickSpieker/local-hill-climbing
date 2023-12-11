import matplotlib.pyplot as plt
from helpers import create_array
from algos import aaron_algo, patrick_algo

from collections import defaultdict
arrays = [create_array() for _ in range(10000)]

def map_results(results):
    xs = []
    ys = []

    counts_dict = defaultdict(int)
    for num_steps in results:
        counts_dict[num_steps] += 1

    xs = [pair[0] for pair in counts_dict.items()]
    ys = [pair[1] for pair in counts_dict.items()]

    return xs, ys


aaron_results = [aaron_algo(i)[1] for i in arrays]
patrick_results = [patrick_algo(i)[1] for i in arrays]

# Head to head
def head_to_head_counts(a_results, b_results):
    a_wins = 0
    b_wins = 0

    for i in range(len(a_results)):
        if a_results[i] < b_results[i]:
            a_wins += 1
        elif b_results[i] < a_results[i]:
            b_wins += 1
    return a_wins, b_wins

# Raw counts
def counts_plot(a_results, b_results):
    a_xs, a_ys = map_results(a_results)
    b_xs, b_ys = map_results(b_results)

    a_wins, b_wins = head_to_head_counts(a_results, b_results)
    plt.scatter(b_xs, b_ys)
    plt.scatter(a_xs, a_ys, c="red")
    plt.text(0, 5000, f"A Wins: ({a_wins}) B Wins: ({b_wins})")
    plt.show()

print(head_to_head_counts(aaron_results, patrick_results))
counts_plot(aaron_results, patrick_results)



