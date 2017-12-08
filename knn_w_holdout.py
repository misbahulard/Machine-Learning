import random
import pandas as pd
import numpy as np
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
    length = len(test)-1
    for x in range(len(training)):
        dist = euclideanDistance(training[x], test, length)
        distances.append((training[x], dist))
    distances.sort(key=operator.itemgetter(1))

    # cari tetangga sebanyak k dan simpan ke list
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    # Tambahkan jaraknya
    for x in range(k):
        if (len(neighbors[x]) == 5):
            neighbors[x].insert(5, distances[x][1])
        else:
            neighbors[x][5] = distances[x][1]

    return neighbors


# fungsi untuk memprediksi data test masuk ke label mana
def predict(neighbors):
    # Hitung dan masukkan ke var classVote
    classVote = {}
    for x in range(len(neighbors)):
        res = neighbors[x][-2]
        if res in classVote:
            classVote[res] += 1
        else:
            classVote[res] = 1

    # urutkan yang paling banyak mana
    sortedVotes = sorted(classVote.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def calculateError(testSet, prediction):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][4] == prediction[x]:
            correct += 1

    numError = len(testSet) - correct
    return (numError/float(len(testSet))) * 100.0

# fungsi untuk mendapatkan random sample test sebanyak k
def holdoutDataset(training, k):
    temp = []
    length = len(training) - 1
    for i in range(k):
        idx = length - i
        temp.append(training[idx])
        training.pop(idx)

    print(temp)

    return temp

def main():
    df = pd.read_csv('irisdata.csv')
    training = df.values
    training = training.tolist()

    print("\nInput K: ")
    k = int(input())

    print("\nNumber of sample: ")
    numOfRand = int(input())
    data_test = holdoutDataset(training, numOfRand)

    # print("Total training data set: ", len(training))
    # print(training)

    prediction = []
    for x in range(len(data_test)):
        neighbors = getNeighbors(training, data_test[x], k)
        print("\nNeighbors data test ke-: ", (x+1))
        for ng in neighbors:
            print("=> ", ng[4], " | distance: ", ng[5])

        prediction.append(predict(neighbors))
        print(predict(neighbors))

    error = calculateError(data_test, prediction)
    print("Error ratio: ", error, "%")



if __name__ == "__main__":
    main()
