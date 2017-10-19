import pandas as pd
import numpy as np

attributes = [['sunny', 'overcast', 'rainy'],
              ['hot','mild', 'cool'],
              ['high','normal'],
              ['strong','weak']]

df = pd.read_csv('tennis.csv')

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

def pred(tes, training, play):
    arr = []
    for i in range(len(tes)):
        idx = [x for x in range(len(attributes[i])) if attributes[i][x] == tes[i]]
        idx = idx[0]
        yes = training[i][idx][0]
        no = training[i][idx][1]
        arr.append([yes, no])

    # print(arr)
    # print(play)


    temp_yes = []
    temp_no = []
    for dt in arr:
        temp_yes.append(dt[0])
        temp_no.append(dt[1])

    yes = np.prod(temp_yes, dtype=np.float) * play[0]
    no = np.prod(temp_no, dtype=np.float) * play[1]

    if yes > no:
        print("Play Tennis YES, pobability: ", yes)
    else:
        print("Play Tennis NO, probability: ", no)

def main():
    play_length = count_attr_length('Play')

    d_play_yes = count_attr('Play', 'yes')
    d_play_no = count_attr('Play', 'no')
    play = [d_play_yes, d_play_no]

    outlook = count_attr_spec('Outlook', play_length)
    temp = count_attr_spec('Temp', play_length)
    humidity = count_attr_spec('Humidity', play_length)
    windy = count_attr_spec('Windy', play_length)
    training = [outlook, temp, humidity, windy]

    # ASK User

    print("Input the data test, example: sunny cool high strong")
    print("Input: ")
    test = input().split()

    pred(test, training, play)


if __name__ == "__main__":
    main()
