import matplotlib.pyplot as plt

x = ['MON', 'Tues', 'Wed', 'Thru']
y = [900,600, 650, 300]

plt.bar(x,y)
plt.title("bar chart")
plt.xlabel("Days")
plt.ylabel("Total bills")
plt.savefig("barchart.jpg")

plt.show(block=False)
print("Press any key on graph window to close...")
plt.waitforbuttonpress()
plt.close()
