from functions import mean
import random
import data
import matplotlib.pyplot as plt


records = list(map(float, data.get("Total.Cup.Points")))

iterations = [
    1, 3, 5,
    10, 30, 50,
    100, 300, 500,
    1000, 3000, 5000,
    10000, 30000, 50000
]

avg_means = []
for times in iterations:
    mean_values = []
    for i in range(times):
        sample = random.sample(records, 20)
        mean_values.append(mean(sample))
    avg_mean = mean(mean_values)
    avg_means.append(avg_mean)
    print("Mean of %d iterations: %f" % (times, avg_mean))


plt.plot(iterations, avg_means)
plt.show()
