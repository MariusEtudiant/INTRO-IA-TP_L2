import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from scipy import interp
from sklearn.metrics import roc_auc_score
import pandas as pd

# PARTIE DONNEES 
wine = datasets.load_wine()
X = pd.DataFrame(wine.data)
y = pd.DataFrame(wine.target)

#PARTIE EXPLOITATION DONNEES 
# représentation matricielle binaire
y = label_binarize(y, classes=[0, 1, 2])

n_classes = y.shape[1] # on récupère le nombre de classe car y.shape = (178,3) donc n_classes = 3

n_samples, n_features = X.shape


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30,
random_state = 0)

#utilisation du modèle gini vu dans le dernier TP
model_decisiontree = DecisionTreeClassifier(criterion = "gini",
random_state = 100, max_depth = 3, min_samples_leaf = 5)
model_decisiontree.fit(X_train, y_train)



y_score = model_decisiontree.predict(X_test)
print("données prédites: ",y_score)

# PARTIE ROC
tfp = dict() # dico avec les faux positifs
tvp = dict() # dico avec les vrai positifs
roc_auc = dict() # dico pour le calcul de l'air sous la courbe 

for i in range(n_classes):
    tfp[i], tvp[i], seuils = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(tfp[i], tvp[i]) # calcule l’aire de la courbe


plt.figure()
plt.plot(tfp[1], tvp[1], color='green', lw=2,
label='courbe ROC (surface = %0.3f)' % roc_auc[1])

plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='dashdot')
plt.xlim([0.0, 1.0])
plt.ylim([0.0,1.0])

plt.xlabel('Taux Faux Positifs')
plt.ylabel('Taux Vrai Positifs')
           
plt.title('Exemple de courbe ROC')
plt.legend(loc = "lower right")

plt.show()