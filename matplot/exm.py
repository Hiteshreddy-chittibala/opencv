# Import libraries
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [15, 20, 35, 40, 50, 60, 70, 80, 88, 95]

# Plot graph
plt.plot(x, y, marker = '*', color='red')
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Student Score Predictor")
plt.savefig("output.jpg")

plt.show(block = False)
plt.waitforbuttonpress()
plt.close()
