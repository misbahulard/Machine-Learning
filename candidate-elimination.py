import pandas as pd

attributes = [['Sunny','Rainy'],
              ['Warm','Cold'],
              ['Normal','High'],
              ['Strong','Weak'],
              ['Warm','Cool'],
              ['Same','Change']]

df = pd.read_csv('enjoysport.csv')
# df = df.drop('enjoy_sport', 1)
df = df.values

def find_s(h, d):
    for i in range(len(d)):
        if h[i] != d[i]:
            h[i] = '?'

    return h

def main():
    print('Candidate elimination\n')
    tipeIdx = len(df[0]) - 1
    trueCol = len(attributes)
    s = []
    g = []
    s = df[0]
    g = [['?'] * trueCol] * trueCol

    count = 0
    for data in df:
        if data[tipeIdx] == 'yes':
            # eliminate g
            if count == 0:
                idx = 0
                for dg in g:
                    for i in range(len(dg)):
                        temp = ['?'] * trueCol
                        if i == idx:
                            if dg[i] != s[idx]:
                                temp[idx] = s[idx]
                                g[i] = temp
                                # print('i: ', i, 'idx: ', idx)
                                # print(i, 'temp => ', temp)
                                # print(i, 'dg => ', g)
                                # print()
                        idx += 1
            else:

                # update spesifik
                s = find_s(s, data)

                idx = 0
                for dg in g:
                    for i in range(len(dg)):
                        temp = ['?'] * trueCol
                        if i == idx:
                            if dg[i] == s[idx]:
                                temp[idx] = s[idx]
                                g[i] = temp
                                # print('i: ', i, 'idx: ', idx)
                                # print(i, 'temp => ', temp)
                                # print(i, 'dg => ', g)
                                # print()
                        idx += 1
        else:
            idx = 0
            for dg in g:
                for i in range(len(dg)):

                    temp = ['?'] * trueCol
                    if i == idx:
                        if dg[i] != data[idx]:
                            g[i] = temp
                            # print('dg => ', i, ' ', dg[i])
                            # print('data =>', data[idx])
                            # print('temp => ', temp)
                            temp[idx] = s[idx]
                        else:
                            temp[idx] = '?'
                            g[i] = temp
                            # print('i: ', i, 'idx: ', idx)
                            # print(i, 'temp => ', temp)
                            # print(i, 'dg => ', g)
                            # print()
                idx += 1
                # for i in range(len(g)):
                #     if i == idx:
                #         print('==> ', i, ' ',idx)
                #         if g[i][idx] != s[idx]:
                #             print('row: ', i)
                #             print('g =>', g[i])
                #             print('s =>', s[idx])
                #             print('\n')
                #             g[i][idx] = s[idx]
                #         idx += 1
                # print(g)
        count += 1


        print('=> specific: ', s)
        print('=> general: ', g)
        print()

    #  delete baris jika isinya ? semua
    gTemp = []
    cIdx = 0
    for dg in g:
        if any(x != '?' for x in dg):
            # print('all ?', cIdx)
            gTemp.append(dg)
        cIdx += 1

    g = gTemp

    # delete kolom yes
    s = [x for x in s if x != 'yes']

    print('==============================================================\n')
    print('Hasil: ')
    print('specific: {}'.format(s))
    print('general: {}'.format(g))

if __name__ == '__main__':
    main()