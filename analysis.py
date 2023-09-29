import csv
import matplotlib.pyplot as plt
import numpy as np


def plot():
    x = np.array([])
    number = 0

    y_s = []
    y_i = []
    y_r = []

    with open('record.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            y_s.append(float(row[0]))
            y_i.append(float(row[1]))
            y_r.append(float(row[2]))
            number += 1
        x = np.linspace(0, 100, number)

        plt.plot(x, y_s, color='yellow', label='suspicious')
        plt.plot(x, y_i, color='red', label='infected')
        plt.plot(x, y_r, color='gray', label='recovered')

        plt.legend()
        plt.show()

        max1 = 0
        for value in y_i:
            if max1 < value:
                max1 = value
        return max1


print(plot())
