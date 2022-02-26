import math
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


class MyApp():
    def __init__(self):
        self.count = 0
        self.parcelList = []
        self.main()

    def main(self):
        name = str(input('Enter parcel {count} >> '.format(count=self.count)))
        weight = float(input('Enter parcel {count} weight >> '.format(count=self.count)))
        distance = float(input('Enter parcel {count} shipping distance in km >> '.format(count=self.count)))
        item = {'name': name, 'weight': weight, 'distance': distance}
        self.parcelList.append(item)
        self.calculat(item)
        self.conttinue()

    def calculat(self, item):
        if not (item is None):
            weight = math.ceil(item['weight'])
            distance = math.ceil(item['distance'] / 100)
            item['price'] = weight + distance * 2
        else:
            print('please Enter something')

    def true_check(self, response):
        if response == "Y":
            return True
        elif response == "N":
            return False
        else:
            self.conttinue()
            print('please Enter Y/N')

    def conttinue(self):
        _continue = bool(
            self.true_check(input('Continue (Y/N) ?')))
        if _continue:
            self.count += 1
            self.main()
        else:
            self.display()

    def display(self):
        for i in range(len(self.parcelList)):
            item = self.parcelList[i]
            print('====== Parcel {count} ======'.format(count=i))
            print('PARCEL NO   : {k}'.format(k=item['name']))
            print('WEIGHT   : {weight}kg'.format(weight=item['weight']))
            print('DISTANCE   : {distance}km'.format(distance=item['distance']))
            print('SHIPPIING COST : ${price}'.format(price=item['price']))
        self.bars()

    def bars(self):
        parcelNames = []
        parcelWeight = []
        parcelDistance = []
        parcelPrice = []
        for i in range(len(self.parcelList)):
            parcelNames.append(self.parcelList[i]['name'])
            parcelWeight.append(self.parcelList[i]['weight'])
            parcelDistance.append(self.parcelList[i]['distance'])
            parcelPrice.append(self.parcelList[i]['price'])

        x = np.arange(len(parcelNames))
        width = 0.25
        plt.bar(x, parcelWeight, width, color='red', label='parcelWeight')
        plt.bar(x, parcelDistance, width, color='yellow', bottom=parcelWeight, label='parcelDistance')
        plt.bar(x, parcelPrice, width, bottom=parcelDistance, color='gray', label='parcelPrice')
        plt.xticks(x, labels=parcelNames)
        plt.legend()
        plt.show()
        counts = np.bincount(parcelPrice)
        print(np.mean(parcelPrice), 'Average shipping cost')
        print(np.min(parcelDistance), 'Minimum distance')
        print(np.max(parcelWeight), 'Maximum weight')
        print(np.std(parcelPrice), 'Shipping cost standard deviation')
        print(np.argmax(counts), 'Mode shipping cost')


if __name__ == "__main__":
    root = MyApp()
