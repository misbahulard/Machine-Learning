import pandas as pd
from matplotlib import pyplot as plt
import operator
import math


# Fungsi untuk menghitung jarak euclidean
def euclideanDistance(inst1, inst2, length):
    distance = 0
    for x in range(length):
        # total terlebih dahulu baru di akar (test - training)^2 + ...
        distance += pow((inst1[x] - inst2[x]), 2)
    return math.sqrt(distance)


# Fungsi untuk mencari tetangga sebanyak k
def getNeighbors(training, test, k):
    # untuk setiap data training hitung jaraknya
    # dan simpan jarak ke list dan urutkan asc
    distances = []
    length = len(test)
    for x in range(len(training)):
        dist = euclideanDistance(training[x], test, length)
        distances.append((training[x], dist))
    distances.sort(key=operator.itemgetter(1))

    # cari tetangga sebanyak k dan simpan ke list
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        # print(distances[x][1])
    return neighbors


# fungsi untuk memprediksi data test masuk ke label mana
def predict(neighbors):
    # Hitung dan masukkan ke var classVote
    classVote = {}
    for x in range(len(neighbors)):
        res = neighbors[x][-1]
        if res in classVote:
            classVote[res] += 1
        else:
            classVote[res] = 1

    # urutkan yang paling banyak mana
    sortedVotes = sorted(classVote.items(), key=operator.itemgetter(1), reverse=True)
    print("\nPredict: ", sortedVotes[0][0])


def main():
    df = pd.read_csv('irisdata.csv')
    training = df.values

    # Example input (5 2 4 2) / (6 6 4 3)
    # testInput = [5, 2, 4, 2]
    print("Input data test")
    testInput = list(map(float, input().split()))

    print("\nInput K: ")
    k = int(input())

    for x in range(len(testInput)):
        neighbors = getNeighbors(training, testInput, k)

    print("\nNeighbors: ")
    for ng in neighbors:
        print("=> ", ng[-1])

    predict(neighbors)
    # Menampilkan plot sepal
    iris_setosaX = [x[0] for x in training if x[4] == 'Iris-setosa']
    iris_setosaY = [x[1] for x in training if x[4] == 'Iris-setosa']
    iris_versicolorX = [x[0] for x in training if x[4] == 'Iris-versicolor']
    iris_versicolorY = [x[1] for x in training if x[4] == 'Iris-versicolor']
    iris_virginicaX = [x[0] for x in training if x[4] == 'Iris-virginica']
    iris_virginicaY = [x[1] for x in training if x[4] == 'Iris-virginica']

    plt.figure(1)
    plt.scatter(iris_setosaX, iris_setosaY, alpha=0.2, c='r', marker='x')
    plt.scatter(iris_versicolorX, iris_versicolorY, alpha=0.2, c='g', marker='^')
    plt.scatter(iris_virginicaX, iris_virginicaY, alpha=0.2, c='b', marker='+')
    plt.scatter(testInput[0], testInput[1], c=[1, 1, 0])
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')

    # Menampilkan plot petal
    iris_setosaX = [x[2] for x in training if x[4] == 'Iris-setosa']
    iris_setosaY = [x[3] for x in training if x[4] == 'Iris-setosa']
    iris_versicolorX = [x[2] for x in training if x[4] == 'Iris-versicolor']
    iris_versicolorY = [x[3] for x in training if x[4] == 'Iris-versicolor']
    iris_virginicaX = [x[2] for x in training if x[4] == 'Iris-virginica']
    iris_virginicaY = [x[3] for x in training if x[4] == 'Iris-virginica']

    plt.figure(2)
    plt.scatter(iris_setosaX, iris_setosaY, alpha=0.2, c='r', marker='x')
    plt.scatter(iris_versicolorX, iris_versicolorY, alpha=0.2, c='g', marker='^')
    plt.scatter(iris_virginicaX, iris_virginicaY, alpha=0.2, c='b', marker='+')
    plt.scatter(testInput[2], testInput[3], c=[1, 1, 0])
    plt.xlabel('Petal length')
    plt.ylabel('Petal width')
    plt.show()

if __name__ == "__main__":
    main()
