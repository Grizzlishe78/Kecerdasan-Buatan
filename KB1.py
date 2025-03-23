import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 6]
y = [2, 4, 1, 3, 5]

for i in range(len(y)):
    if y[i] < 3:
        y[i] = y[i] * 2  

x_np = np.array(x)
y_np = np.array(y)

plt.plot(x_np, y_np, marker='o', linestyle='-', color='r', label='Data y setelah modifikasi')
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.title("Grafik dengan Modifikasi Data")
plt.legend()
plt.grid(True)
plt.show()