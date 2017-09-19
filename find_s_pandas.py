import pandas as pd

df = pd.read_csv('enjoysport.csv')
df = df.loc[df['enjoy_sport'] == 'yes']
df = df.values
hipotesa = []

def find_s(h, d):
    for i in range(len(d)):
        if h[i] != d[i]:
            h[i] = '?'

    return h

def main():
    print('Algoritma find s')
    hipotesa = df[0]

    print('Hipotesa awal: ', hipotesa)

    for d in df:
        hipotesa = find_s(hipotesa, d)
        print('=>', hipotesa)

    print('Hasil akhir: ', hipotesa)

if __name__ == "__main__":
    main()