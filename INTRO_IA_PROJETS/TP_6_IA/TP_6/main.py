from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns




def main():
    Partie2()
    Partie1()
    Partie3()
    ex_scatter()
    return 0


def ex_scatter():
    df = pd.read_csv('World_hapiness_dataset_2019.csv', sep=',', header=0)

    plt.scatter(df['GDP per capita'], df['Score'], s=50)
    plt.show()

    sns.scatterplot(x='GDP per capita', y='Score', data=df)
    plt.show()

    sns.catplot(x='GDP per capita', y='Score', data=df)
    plt.show()


def Partie3():
    df = pd.read_csv('wine.csv', sep=',', header=0)

    # Converti vers numpy
    X = df.to_numpy()

    pca: PCA = PCA(n_components=2)
    reduced_data = pca.fit_transform(X)

    # 3 clusters
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(reduced_data)
    classe = kmeans.predict(reduced_data)

    labels_unique = np.unique(classe)
    print(labels_unique)
    classe = df["Class"]
    for label in labels_unique:
        to_plot = reduced_data[np.where(classe == label)[0]]
        plt.scatter(to_plot[:, 0], to_plot[:, 1], s=20)

    plt.show()

def Partie2():
    # Ouvre le fichier wine.csv
    df = pd.read_csv('wine.csv', sep=',', header=0)
    # Print les 10 premières rows
    print(df.head(10))
    # Print les 10 dernières lignes
    print(df.tail(10))

    # Informations du DataSet
    print(df.info())
    # Vérifie les valeurs nulles
    print(df.isnull().sum())

    # Affiche les labels du dataset en utilisant np.unique()
    print(np.unique(df['Class']))


def Partie1():
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], s=50)

    # Print les coordonnées des points
    for i in range(len(X)):
        print(X[i])

    plt.show()

    kmeans = KMeans(n_clusters=4)  # 4 clusters
    kmeans.fit(X)  # Fit the model to the data

    y_kmeans = kmeans.predict(X)  # Predict the clusters of the data

    # Afiche les clusters
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_  # Get the coordinates of the centers
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()

    #OPTIONNEL DEUX SOUS-GRAPHIQUES, pour differencier les classes avec l'algorithme
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Graphique des classes réelles
    axes[0].scatter(X[:, 0], X[:, 1], c=y_true, s=50, cmap='viridis')
    axes[0].set_title("Classes Réelles")
    axes[0].set_xlabel("Dimension 1")
    axes[0].set_ylabel("Dimension 2")

    # Graphique des classes prédites
    axes[1].scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    axes[1].scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    axes[1].set_title("Classes Prédites par K-means")
    axes[1].set_xlabel("Dimension 1")
    axes[1].set_ylabel("Dimension 2")

    # Affichage du graphique
    plt.tight_layout()
    plt.show()

    # Affiche classes X et classes y_kmeans
    print("X classes: ", y_true)
    print("y_kmeans classes: ", y_kmeans)


if __name__ == '__main__':
    main()