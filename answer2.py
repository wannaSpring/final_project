import math
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


class MyApp():
    def __init__(self):
        self.count = 0
        self.locked = False
        self.parcelObj = {}
        self.main()

    def main(self):
        name = str(input('Enter parcel {count} >> '.format(count=self.count)))
        weight = float(input('Enter parcel {count} weight >> '.format(count=self.count)))
        distance = float(input('Enter parcel {count} shipping distance in km >> '.format(count=self.count)))
        self.parcelObj[name] = {'weight': weight, 'distance': distance}
        self.calculat(self.parcelObj[name])
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
        for k, v in self.parcelObj.items():
            print('====== Parcel {count} ======'.format(count=self.count))
            print('PARCEL NO   :{k}'.format(k=k))
            print('WEIGHT   :{weight}'.format(weight=v['weight']))
            print('DISTANCE   :{distance}'.format(distance=v['distance']))
            print('SHIPPIING COST :{price}'.format(price=v['price']))
        self.bars()

    def bars(self):
        parcelNames = list(self.parcelObj.keys())
        parcelWeight = list(map(lambda item: item['weight'], self.parcelObj.values()))
        parcelDistance = list(map(lambda item: item['distance'], self.parcelObj.values()))
        parcelPrice = list(map(lambda item: item['price'], self.parcelObj.values()))
        parcelItem = list(self.parcelObj.values())
        print(parcelItem)
        x = np.arange(len(parcelNames))
        width = 0.25
        plt.bar(x, parcelWeight, width, color='red', label='parcelWeight')
        plt.bar(x, parcelDistance, width, color='yellow', bottom=parcelWeight, label='parcelDistance')
        plt.bar(x, parcelPrice, width, bottom=parcelDistance, color='gray', label='parcelPrice')
        plt.xticks(x, labels=parcelNames)
        plt.legend()
        plt.show()
        df = pd.DataFrame.from_dict(parcelItem)
        print(df.max(), '1')
        print(df.min(), '2')
        print(df.std(), '3')
        print(df.mode(), '4')
        print(df.mean(), '5')


if __name__ == "__main__":
    root = MyApp()
