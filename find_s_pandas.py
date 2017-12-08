import pandas as pd

attributes = [['Sunny','Rainy'],
              ['Warm','Cold'],
              ['Normal','High'],
              ['Strong','Weak'],
              ['Warm','Cool'],
              ['Same','Change']]

df = pd.read_csv('enjoysport.csv')
df = df.loc[df['enjoy_sport'] == 'yes']
df = df.values
hipotesa = []

def find_s(h, d):
    for i in range(len(d)):
        if h[i] != d[i]:
            h[i] = '?'

    return h

def check_data(h, d):
    for i in range(len(d)):
        if h[i] != '?':
            if h[i] != d[i]:
                return 'NO'

    return 'YES'

def main():
    print('Algoritma find s')
    hipotesa = df[0]

    print('Hipotesa awal: ', hipotesa)

    for d in df:
        hipotesa = find_s(hipotesa, d)
        print('=>', hipotesa)

    print('Hasil akhir: ', hipotesa)

    print("\nTEST");
    print("==============================")

    argsList = []
    maxLengthList = 6
    while len(argsList) < maxLengthList:
        item = input("Enter your data: ")
        argsList.append(item)
    print("\nData test: ")
    print(argsList)

    print('\nApakah olahraga? ')
    print(check_data(hipotesa, argsList))

if __name__ == "__main__":
    main()