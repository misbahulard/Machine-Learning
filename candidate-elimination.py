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

def hipotesa(g, s):
    gTemp = []
    flags = []
    for ds in s:
        if ds != '?':
            flags.append(ds)

    flagIdx = 0
    i = 0
    for f in flags:
        pieces = []
        count = 0
        idx = 0
        for ds in s:
            if idx < flagIdx:
                continue
            if count < 2:
                if f == ds:
                    pieces.append(f)
                    flagIdx = idx
                    count += 1
                elif f != ds and ds != '?':
                    pieces.append(ds)
                    count += 1
                else:
                    pieces.append('?')
            else:
                break
            idx += 1
        gTemp.append(pieces)
        i += 1

    print(pieces)
        # if dg[idx] != '?':
        #     flag = dg[idx]
        #     print('flag: ', flag)
        #     for ds in s:
        #         if flag != ds:
        #             if count < 2:
        #                 pieces.append(ds)
        #             else:
        #                 pieces.append('?')
        #                 if ds != '?':
        #                     flag
        #         else:
        #             pieces.append(flag)
        #         count += 1
        #     idx += 1
        #     print('pieces: ', pieces)
        #     gTemp.append(pieces)
        # print(gTemp)
        # if s[idx] != '?':
        #     print(dg[idx])
        #     print(s[idx])
        #     print('======')
        #     if dg[idx] == s[idx]:
        #         print(s[idx])
        #         gTemp.append(s[idx])
        # idx += 1
        # print(gTemp)

    # print(gTemp)
    # g = gTemp

def main():
    print('Candidate elimination\n')
    tipeIdx = len(df[0]) - 1
    trueCol = len(attributes)
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
                            # jika data general tidak sama dengan specific maka g baru di isi nilai spesifik
                            if dg[i] != s[idx]:
                                temp[idx] = s[idx]
                                g[i] = temp
                        idx += 1
            else:

                # update spesifik
                s = find_s(s, data)

                idx = 0
                for dg in g:
                    for i in range(len(dg)):
                        temp = ['?'] * trueCol
                        if i == idx:
                            # jika data general sama dengan specific maka g baru di isi nilai spesifik
                            if dg[i] == s[idx]:
                                temp[idx] = s[idx]
                                g[i] = temp
                        idx += 1
        else:
            idx = 0
            for dg in g:
                for i in range(len(dg)):

                    temp = ['?'] * trueCol
                    if i == idx:
                        # Jika data tidak sama maka g di isi nilai s
                        if dg[i] != data[idx]:
                            g[i] = temp
                            temp[idx] = s[idx]
                        else:
                            temp[idx] = '?'
                            g[i] = temp
                idx += 1
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
    print('Hipotesa: ')
    hipotesa(g, s)
    print('==============================================================\n')

if __name__ == '__main__':
    main()