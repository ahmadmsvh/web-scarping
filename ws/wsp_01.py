import pandas as pd
from xlsxwriter import Workbook
import itertools

data = [12.99, 20.90, 13.21, 12.77, 10.03, 8.89, 13.42,
        12.18, 9.31,8.66, 14.55, 0.0, 14.74, 10.81, 15.94,
        16.72,18.09, 6.45]

band = []
counter = 0
for i in data:
    for j in data[(data.index(i) + 1):]:
        for k in data[data.index(j) + 1:]:
            for l in data[data.index(k) + 1:]:
                for m in data[data.index(l) + 1:]:
                    for n in data[data.index(m) + 1:]:
                        group_1 = [i, j, k, l, m, n]

                        dat = data.copy()
                        for g in group_1:
                            dat.remove(g)

                        for ii in dat:
                            for jj in dat[dat.index(ii) + 1:]:
                                for kk in dat[dat.index(jj) + 1:]:
                                    for ll in dat[dat.index(kk) + 1:]:
                                        for mm in dat[dat.index(ll) + 1:]:
                                            for nn in dat[dat.index(mm) + 1:]:
                                                group_2 = [ii, jj, kk, ll, mm, nn]

                                                da = dat.copy()
                                                for g in group_2:
                                                    da.remove(g)

                                                group_3 = da

                                                if abs(sum(group_1) - sum(group_2)) < 1.5:
                                                    if abs(sum(group_1) - sum(group_3)) < 1.5:
                                                        if abs(sum(group_2) - sum(group_3)) < 1.5:

                                                            band.append([group_1,
                                                                         group_2,
                                                                         group_3,
                                                                         ])
for record in band:
   permutationObj = itertools.permutations(record)
   permutationList = list(permutationObj)
   counter = 0

   for perm_record in permutationList:
      if list(perm_record) in band:
         counter += 1
         if counter > 1:
            band.remove(list(perm_record))

for rec in band:
   max_diff = abs(max(sum(rec[0])-sum(rec[1]),sum(rec[0])-sum(rec[2]),sum(rec[1])-sum(rec[2])))
   rec.append(sum(rec[0]))
   rec.append(sum(rec[1]))
   rec.append(sum(rec[2]))
   rec.append(max_diff)

band_dataFrame = pd.DataFrame(band,
                              columns = ['group_1','group_2','group_3','sum_1','sum_2','sum_3','max_diff'],
                              index = range(1,len(band)+1)
                              )
band_dataFrame.to_csv('csv_out.csv')
band_dataFrame.to_excel('xlsx_out.xlsx', engine='xlsxwriter')