import numpy as np
import pandas as pd
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


def clean(path):
    df = pd.read_csv('{path}.csv'.format(path=path))
    # we can see like read is non-less attributes, so we drop it
    print(df.head())
    df.fillna(value=df.mean(), inplace=True)
    df.drop(columns=['like_read'], inplace=True)
    df.drop(columns=['Desired age of marriage'], inplace=True)
    print(df.head())
    df.to_csv('right{path}.csv'.format(path=path), index=False, sep=',', header=0)

clean('data')
clean('realData')
myData = np.loadtxt('rightData.csv', delimiter=',')
x = myData[:, 0:3]
y = myData[:, 3]
# create model
model = Sequential()
model.add(Dense(4, input_dim=3, activation="relu"))
# model.add(Dense(2, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=100, batch_size=1000, shuffle=True)

_, accuracy = model.evaluate(x, y)
print("Accuracy: ", accuracy)

predict = model.predict(x)
classes = np.argmax(predict, axis=1)
for i in range(5):
    print(x[i].tolist(), "predicts", predict[i], "ACTUAL :", y[i])

#
dataset = loadtxt('rightrealData.csv', delimiter=",")
ds = dataset[:, 0:3]
predict = model.predict(ds)
classes = np.argmax(predict, axis=1)
for i in range(5):
    print(ds[i].tolist(), "predicts", predict[i])
