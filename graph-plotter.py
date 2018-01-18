import matplotlib.pyplot as plt

plot_data = []


for i in range(0,10):
	plot_data.append(i**2)

plt.plot(plot_data)
plt.show()