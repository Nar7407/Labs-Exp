import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
plt.axes[0,1].plot(x, np.sin(x), label='Sine Wave', color='blue', linewidth=2, linestyle='-')
plt.axes[0,1].plot(x, np.cos(x), label='Cosine Wave', color='orange', linewidth=2, linestyle='--')
plt.axes[1,0].bar(["Python", "Java", "C++", "JavaScript"], [215, 130, 245, 210], color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.axes[1,1].scatter(np.random.rand(150) * 10, 2*np.random.rand(150) * 10 + np.random.normal(150)*2, s=np.random.rand(150) * 300, alpha=0.5, c=np.random.rand(150) * 10, cmap='viridis', edgecolors='w', linewidth=0.5)
plt.suptitle("Multiple Plots in a Single Figure")
plt.show()
