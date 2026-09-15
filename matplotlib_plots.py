import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt
import numpy as np

'''x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label='Sine Wave', color='blue', linewidth=2, linestyle='-')
ax.plot(x, np.cos(x), label='Cosine Wave', color='orange', linewidth=2, linestyle='--')
ax.set_title("Line Plot of Sine and Cosine Functions")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(alpha=0.3)
plt.savefig('line_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved line_plot.png")

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [215, 130, 245, 210]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.1, 0, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Pie Chart of Programming Language Popularity")
plt.savefig('pie_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved pie_chart.png")

np.random.seed(42)
data = [np.random.normal(0, std, 200) for std in range(1, 6)]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
fig, ax = plt.subplots()
parts = ax.violinplot(data, showmeans=False, showmedians=True)
for pc in parts['bodies']:
    pc.set_facecolor(colors[parts['bodies'].index(pc)])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)
ax.set_title("Violin Plot of Random Data")
ax.set_xticks(range(1, 6))
ax.set_xticklabels(["Grp1", "Grp2", "Grp3", "Grp4", "Grp5"])
plt.savefig('violin_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved violin_plot.png")

np.random.seed(42)
x= np.random.rand(150) * 10
y= 2*x + np.random.normal(150)*2
sizes = np.random.rand(150) * 300

fig, ax = plt.subplots()
sc= ax.scatter(x, y, s=sizes, alpha=0.5, c=y, cmap='viridis', edgecolors='w', linewidth=0.5)

ax.set_title("Scatter Plot with Random Data")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()
plt.colorbar(sc, ax=ax, label='Color Scale')
plt.savefig('scatter_plot.png', dpi=150, bbox_inches='tight')
x=np.linspace(-3, 3, 200)
y=np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2) * np.exp(-0.1 * (X**2 + Y**2))
fig, ax = plt.subplots()
contour = ax.contourf(X, Y, Z, levels=20, cmap='plasma')
ax.set_title("Contour Plot of a Gaussian Function")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.colorbar(contour, ax=ax, label='Function Value')
plt.savefig('contour_plot.png', dpi=150, bbox_inches='tight')
plt.close()
np.random.seed(42)
data = np.random.normal(65, 12, 1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color='#66b3ff', edgecolor='black', alpha=0.7)
ax.set_title("Histogram of Normally Distributed Data")
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.axvline(data.mean(), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {data.mean():.2f}')
ax.axvline(data.mean() + data.std(), color='green', linestyle='dashed', linewidth=1, label=f'Std Dev: {data.std():.2f}')
ax.legend()
plt.savefig('histogram_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved histogram_plot.png")
branches = ["CSE", "ECE", "MECH", "CIVIL"]
students = [120, 80, 60, 40]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
fig, ax = plt.subplots()
ax.bar(branches, students, color=colors, edgecolor='black', alpha=0.7)
ax.set_title("Bar Chart of Students in Different Branches")
ax.set_xlabel('Branches')
ax.set_ylabel('Number of Students')
for i, v in enumerate(students):
    ax.text(i, v + 2, str(v), ha='center', va='bottom')
plt.savefig('bar_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved bar_chart.png")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

plt.fill_between(x, y1, color='skyblue', alpha=0.5, label='sin(x)')
plt.fill_between(x, y1, y2, color='lightgreen', alpha=0.5, label='sin(x) to cos(x)')
plt.fill_between(x, y2, y3, color='salmon', alpha=0.5, label='cos(x) to sin(x) * cos(x)')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Complex Area Plot Example')

plt.legend()

plt.savefig('area_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved area_plot.png")'''
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
plt.axes[0,1].plot(x, np.sin(x), label='Sine Wave', color='blue', linewidth=2, linestyle='-')
plt.axes[0,1].plot(x, np.cos(x), label='Cosine Wave', color='orange', linewidth=2, linestyle='--')
plt.axes[1,0].bar(["Python", "Java", "C++", "JavaScript"], [215, 130, 245, 210], color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.axes[1,1].scatter(np.random.rand(150) * 10, 2*np.random.rand(150) * 10 + np.random.normal(150)*2, s=np.random.rand(150) * 300, alpha=0.5, c=np.random.rand(150) * 10, cmap='viridis', edgecolors='w', linewidth=0.5)
plt.suptitle("Multiple Plots in a Single Figure")
plt.show()
