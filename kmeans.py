from copy import deepcopy
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import operator
import math

# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Fungsi untuk menghitung jarak euclidean
def errorCentroid(a, b, length):
    distance = 0
    for x in range(length):
        for y in range(2):
            # total terlebih dahulu baru di akar (test - training)^2 + ...
            distance += pow((a[x][y] - b[x][y]), 2)
    return math.sqrt(distance)

# Fungsi untuk menghitung jarak euclidean
def euclideanDistance(a, b, length):
    distances = []
    for x in range(length):
        distance = 0
        for y in range(2):
            # total terlebih dahulu baru di akar (test - training)^2 + ...
            distance += pow((a[y] - b[x][y]), 2)
            # print(pow((a[y] - b[x][y]), 2))
        distances.append(math.sqrt(distance))
    return np.array(distances)

def main():
    df = pd.read_csv('ruspini.csv', names=['x', 'y', 'z'])
    # df = pd.read_csv('xclara.csv')

    print(len(df))

    f1 = df['x'].values
    f2 = df['y'].values
    # f1 = df['V1'].values
    # f2 = df['V2'].values
    X = np.array(list(zip(f1, f2)))

    plt.scatter(f1, f2, c='red', s=10)

    # print("Input k: ")
    # k = int(input())
    k = 4
    C_x = np.random.randint(0, np.max(X), size=k)
    C_y = np.random.randint(0, np.max(X), size=k)
    C = np.array(list(zip(C_x, C_y)), dtype=np.float32)

    print("Intial Centroids: ")
    print(C)
    print("=========================\n")

    plt.scatter(C_x, C_y, marker="*", c="black", s=10)

    C_old = np.zeros(C.shape)

    clusters = np.zeros(len(X))
    # print(cluster)

    error = errorCentroid(C, C_old, k)
    print(error)

    while error != 0:
        # Hitung jarak data dengan centroit
        for i in range(len(X)):
            distances = euclideanDistance(X[i], C, k)
            cluster = np.argmin(distances)
            clusters[i] = cluster

        # simpan centroid lama
        C_old = deepcopy(C)
        for i in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        # Hitung error
        print("\nCentroid baru: ")
        print(C)
        print("-------------------------")
        error = errorCentroid(C, C_old, k)

    for i in range(len(X)):
        print("Data: ", X[i], " cluster: ", clusters[i])

    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    fig, ax = plt.subplots()
    for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], c=colors[i], s=10)
    ax.scatter(C[:, 0], C[:, 1], c='black', s=10)
    plt.show()


if __name__ == "__main__":
    main()
