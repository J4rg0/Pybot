import random
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np


def addRoll(data):
    # use passed name to open file and add passed rolls
    end = '.txt'
    name = data.pop(0)
    file = name + end
    f = open(file, 'a')

    for roll in data:
        f.write(str(roll))
        f.write(' ')

    f.close()

    amount = len(data)
    sentence = f'{amount} rolls were added!'
    return sentence

def mean(data):
    # use passed name to open file and calculate mean of rolls
    end = '.txt'
    name = data.pop(1)
    file = name + end
    with open(file) as f:
        read_data = f.read()
        numbers = []
        for number in read_data.split():
            numbers.append(int(number))
        mean = statistics.mean(numbers)
        rounded = round(mean)
        amount = len(numbers)

        result = f'The mean for {name} was {rounded} over {amount} rolls!'
        return result
    f.close()
def graphIt(data):
    # use passed name to open file and graph rolls
    x = []
    y = []
    end = '.txt'
    name = data.pop(1)
    file = name + end
    with open(file) as f:
        for item in f:
            items = item.split()
            for stuff in items:
                y.append(float(stuff))
                x.append(len(y))
    f.close()
    plt.xticks(x)
    plt.scatter(x, y)
    plt.grid()
    plt.savefig("rollchart.png")
    plt.close()

# def piePlot(data):
#     end = '.txt'
#     name = data.pop(1)
#     file = name + end
#     numbers = {}
#     six = 0
#     five = 0
#     four = 0
#     three = 0
#     two = 0
#     one = 0
#
#     labels = 'Six', 'Five', 'Four', 'Three', 'Two', 'One'
#     with open(file) as f:
#         for item in f:
#             items = item.split()
#             for number in items:
#                 if number == '6':
#                     six = six + 1
#
#                 elif number == '5':
#                     five = five + 1
#                 elif number == '4':
#                     four = four + 1
#                 elif number == '3':
#                     three = three + 1
#                 elif number == '2':
#                     two = two + 1
#                 elif number == '1':
#                     one = one + 1
#     f.close()
#     numbers['six'] = six
#     numbers['five'] = five
#     numbers['four'] = four
#     numbers['three'] = three
#     numbers['two'] = two
#     numbers['one'] = one
#     values = numbers.values()
#     plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
#     plt.savefig('piechart.png')
#     plt.close
