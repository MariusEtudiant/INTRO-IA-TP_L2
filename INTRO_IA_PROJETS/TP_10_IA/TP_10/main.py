import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from random import random
from sklearn_som.som import SOM

#PARTIE DONNEES

wine = datasets.load_wine()

print("Keys in wine dataset:", wine.keys())

X = wine.data
label = wine.target

#PARTIE ANALYSE

m, n = 16, 16  # Define grid dimensions

som = SOM(m=m, n=n, dim=13, random_state=1234) 

print(som.fit(X))
predictions = som.predict(X)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(5, 7))
colors = ['red', 'green', 'blue']
x = predictions // m + [random() for _ in range(len(predictions))]
y = predictions % m + [random() for _ in range(len(predictions))]

ax[0].scatter(x, y, c=label, cmap=ListedColormap(colors))
ax[0].set_title('After one epoch')

som.fit(X, epochs=100)
predictions = som.predict(X)
x = predictions // m + [random() for _ in range(len(predictions))]
y = predictions % m + [random() for _ in range(len(predictions))]
ax[1].scatter(x, y, c=label, cmap=ListedColormap(colors))
ax[1].set_title('After 100 epochs')

plt.figure()
plt.imshow(som.transform(X))
plt.show()



