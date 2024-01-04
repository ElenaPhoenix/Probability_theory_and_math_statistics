# Даны значения проницаемости сосудов сетчатки gr1 (здоровые пациенты), gr 2 ( поражение в области центральной ямки), gr3 (в области центральной ямки и на периферии).
# Сравнить данные, относящиеся к разным видам поражения.
# gr1 =([0.5, 0.7, 1, 1.2, 1.4])
# gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])
# gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])
import numpy as np
import scipy.stats as stats

gr1 = np.array([0.5, 0.7, 1, 1.2, 1.4])
gr2 = np.array([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = np.array([6.2, 12.6, 13.2, 14.1, 14.2])
print(stats.kruskal(gr1, gr2, gr3)) # KruskalResult(statistic=12.02000000000001, pvalue=0.002454088180413905)
# pvalue=0.002 < alfa=0,05 => отвергаем 0-ю гипотезу, есть статистически значимые различия