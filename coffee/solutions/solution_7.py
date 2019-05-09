from collections import defaultdict
import matplotlib.pyplot as plt
import data

records = list(map(float, data.get("Total.Cup.Points")))


def draw_bar_plot(records, b_size):
    buckets = defaultdict(list)

    for value in records:
        # print(value, b_size, value // b_size)
        buckets[value // b_size].append(value)

    keys = sorted(buckets.keys())
    values = [len(buckets[b]) for b in keys]
    labels = [
        "%d-%d" % (b * b_size, b * b_size + b_size)
        for b in keys
    ]

    plt.bar(keys, values)
    plt.xticks(keys, tuple(labels))
    plt.ylabel("# of people")
    plt.title("Buckets of %d" % b_size)
    plt.tight_layout()
    plt.show()


print(records)
draw_bar_plot(records, 5)
draw_bar_plot(records, 25)
draw_bar_plot(records, 50)
