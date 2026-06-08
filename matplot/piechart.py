import matplotlib.pyplot as plt
#import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TATA', 'MAHINDRA',]
data = [23, 10, 35, 65, 72]

plt.pie(data, labels=cars)
plt.title(" Pie Chart")
plt.show(block = False)
plt.waitforbuttonpress()
plt.close()

