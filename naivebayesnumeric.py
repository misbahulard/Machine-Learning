import pandas as pd
import numpy as np
import math

attributes = [['sunny', 'overcast', 'rainy'],
              ['hot', 'mild', 'cool'],
              ['high', 'normal'],
              ['strong', 'weak']]

df = pd.read_csv('tennis_numeric.csv')

data_total = len(df.values)


# df = df.values

def count_attr_length(attr):
    df_frame = df[attr].values
    yes = len([x for x in df_frame if x == 'yes'])
    no = len([x for x in df_frame if x == 'no'])
    return [yes, no]


def count_attr(attr, val):
    df_frame = df[attr].values
    res = len([x for x in df_frame if x == val]) / data_total
    return res


def count_attr_spec(attr, div):
    temp = []

    if attr == 'Outlook':
        arr = attributes[0]
    elif attr == 'Temp':
        arr = attributes[1]
    elif attr == 'Humidity':
        arr = attributes[2]
    else:
        arr = attributes[3]

    for val in arr:
        data_yes = np.array((df[attr] == val) & (df['Play'] == 'yes'))
        data_no = np.array((df[attr] == val) & (df['Play'] == 'no'))
        yes = len([x for x in data_yes if x == True])
        no = len([x for x in data_no if x == True])
        temp.append([yes / div[0], no / div[1]])

    return temp


def count_attr_spec_numeric(attr, div):
    temp = []

    if attr == 'Outlook':
        arr = attributes[0]
    elif attr == 'Temp':
        arr = attributes[1]
    elif attr == 'Humidity':
        arr = attributes[2]
    else:
        arr = attributes[3]

    for val in arr:
        data_yes = np.array((df[attr] == val) & (df['Play'] == 'yes'))
        data_no = np.array((df[attr] == val) & (df['Play'] == 'no'))
        yes = len([x for x in data_yes if x == True])
        no = len([x for x in data_no if x == True])
        temp.append([yes / div[0], no / div[1]])

    return temp


def mean_attr(attr):
    yes, no = [], []

    for x in range(len(df)):
        if df['Play'][x] == 'yes':
            yes.append(df[attr][x])
        else:
            no.append(df[attr][x])

    mean = [np.mean(yes), np.mean(no)]
    # print("mean: ", mean)
    return mean


def std_dev_attr(attr):
    yes, no = [], []

    for x in range(len(df)):
        if df['Play'][x] == 'yes':
            yes.append(df[attr][x])
        else:
            no.append(df[attr][x])

    std_dev = [np.std(yes, ddof=1), np.std(no, ddof=1)]
    return std_dev


def pred(tes, training, play):
    idxOutlook = [x for x in range(len(attributes[0])) if attributes[0][x] == tes[0]]
    idxOutlook = idxOutlook[0]
    outlook = training[0][idxOutlook]

    idxWindy = [x for x in range(len(attributes[3])) if attributes[3][x] == tes[3]]
    idxWindy = idxWindy[0]
    windy = training[3][idxWindy]

    tempYes = 1 / (math.sqrt(2 * math.pi) * (training[1][1][0])) * math.pow(math.e, -(
        ((tes[1] - training[1][0][0]) ** 2) / (2 * (training[1][1][0]) ** 2)))
    tempNo = 1 / (math.sqrt(2 * math.pi) * (training[1][1][1])) * math.pow(math.e, -(
        ((tes[1] - training[1][0][1]) ** 2) / (2 * (training[1][1][1]) ** 2)))

    temp = [tempYes, tempNo]

    # print("Hitungan temp:\n", temp)

    humidityYes = 1 / (math.sqrt(2 * math.pi) * (training[2][1][0])) * math.pow(math.e, -(
        ((tes[1] - training[2][0][0]) ** 2) / (2 * (training[2][1][0]) ** 2)))
    humidityNo = 1 / (math.sqrt(2 * math.pi) * (training[1][1][1])) * math.pow(math.e, -(
        ((tes[1] - training[2][0][1]) ** 2) / (2 * (training[2][1][1]) ** 2)))

    humidity = [humidityYes, humidityNo]

    arr = [outlook, temp, humidity, windy]

    yesRes, noRes = 1, 1

    for dt in arr:
        yesRes = yesRes * dt[0]
        print(yesRes)
        noRes = noRes * dt[1]

    print(play[0])

    yesRes = yesRes * play[0]
    noRes = noRes * play[1]


    print("=> Yes Value: ", yesRes)
    print("=> No Value: ", noRes)

    if yesRes > noRes:
        print("Play Tennis YES, pobability: ", yesRes)
    else:
        print("Play Tennis NO, probability: ", noRes)


def main():
    play_length = count_attr_length('Play')

    d_play_yes = count_attr('Play', 'yes')
    d_play_no = count_attr('Play', 'no')
    play = [d_play_yes, d_play_no]

    outlook = count_attr_spec('Outlook', play_length)
    windy = count_attr_spec('Windy', play_length)
    temp_mean = mean_attr('Temp')
    temp_std_dev = std_dev_attr('Temp')
    temp = [temp_mean, temp_std_dev]
    print("std_dev temp:\n", temp_std_dev)
    humidity_mean = mean_attr('Humidity')
    humidity_std_dev = std_dev_attr('Humidity')
    print("std hum: \n", humidity_std_dev)
    humidity = [humidity_mean, humidity_std_dev]
    training = [outlook, temp, humidity, windy]

    # xx = 1 / (math.sqrt(2 * math.pi) * (6.2)) * math.pow(math.e, -(((66 - 73) ** 2) / (2 * (6.2) ** 2)))

    # test = ['sunny', 85, 85, 'weak']

    # ASK User

    print("Input the data test, example: sunny cool high strong")
    print("Input: ")
    test = input().split()
    test[1] = int(test[1])
    test[2] = int(test[2])

    pred(test, training, play)


if __name__ == "__main__":
    main()
