import random
from math import sqrt

N = int(input("Dwse akeraio arithmo N: "))
L = [random.randint(1,20) for num in range(1, N)]


def stats(list):
    list_items = len(list)
    M = sum(list) / list_items
    variance = sum([(x-M)**2 for x in L]) / len(list)
    sd = sqrt(variance)
    print("The list is: ", L)
    print("The average is: M=", M)
    print('The standard deviation is {}.'.format("%.2f" % round(sd,2)))


stats(list=L)