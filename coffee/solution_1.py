import matplotlib.pyplot as plt
import data

moisture = data.get("Moisture")
plt.plot(moisture)
plt.show()

plt.plot(sorted(moisture))
plt.show()
