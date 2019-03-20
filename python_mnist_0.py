import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib

data_file = open("/Users/dowon/Desktop/Step1/mnist_train_100.csv", "r")
data_list = data_file.readlines()
data_file.close()

all_values = data_list[0].split(',')
image_array = np.asfarray(all_values[1:]).reshape((28,28))
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.show()
scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
print(scaled_input)