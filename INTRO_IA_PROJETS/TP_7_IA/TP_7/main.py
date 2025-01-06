import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

donnees = pd.DataFrame(iris.data)
donnees.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

target = pd.DataFrame(iris.target)

x_train, x_test, y_train, y_test = train_test_split(donnees, target, test_size=0.30, random_state=1)


# Modèle avec critère Gini et paramètres ajustés
model_decisiontree_gini = DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=5, min_samples_leaf=2)
model_decisiontree_gini.fit(x_train, y_train)
y_pred_gini = model_decisiontree_gini.predict(x_test)

# Modèle avec critère d'entropie et paramètres ajustés
model_decisiontree_entropy = DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=5, min_samples_leaf=2)
model_decisiontree_entropy.fit(x_train, y_train)
y_pred_entropy = model_decisiontree_entropy.predict(x_test)

# Comparaison des résultats
print("Accuracy (Gini):", accuracy_score(y_test, y_pred_gini))
print("Confusion Matrix (Gini):\n", confusion_matrix(y_test, y_pred_gini))
print("Classification Report (Gini):\n", classification_report(y_test, y_pred_gini))

print("\nAccuracy (Entropy):", accuracy_score(y_test, y_pred_entropy))
print("Confusion Matrix (Entropy):\n", confusion_matrix(y_test, y_pred_entropy))
print("Classification Report (Entropy):\n", classification_report(y_test, y_pred_entropy))

# Visualisation de l'arbre avec critère Gini
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plot_tree(model_decisiontree_gini, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
          class_names=['setosa', 'versicolor', 'virginica'], filled=True)
plt.title("Decision Tree - Gini")

# Visualisation de l'arbre avec critère d'entropie
plt.subplot(1, 2, 2)
plot_tree(model_decisiontree_entropy, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
          class_names=['setosa', 'versicolor', 'virginica'], filled=True)
plt.title("Decision Tree - Entropy")

plt.show()




