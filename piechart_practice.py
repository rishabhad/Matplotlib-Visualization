import matplotlib.pyplot as plt

#Data to plot

lables=['apple','orange','grape','guava']

sizes=[100,150,400,220]

color=['pink','orange','green','lightgreen']

plt.pie(sizes,labels=lables, colors=color,
        autopct='%1.1f%%', shadow=True, startangle=45)
plt.axis('equal')
plt.show()
