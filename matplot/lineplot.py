import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [1,6,4,16,9]

plt.plot(x,y, marker = 'o', label = "Data Points")
plt.xlabel("X-Axis") 
plt.ylabel("Y-Axis") 
plt.legend()  #Display all labels on graph
plt.savefig("lineplot.png")
plt.show()

