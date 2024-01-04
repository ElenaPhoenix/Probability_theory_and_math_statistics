# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
import numpy as np
import scipy.stats as stats

x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
print(stats.wilcoxon(x1, x2)) # WilcoxonResult(statistic=0.0, pvalue=0.0625)
print('Вывод: pvalue=0.063 > 𝛼=0.05 => нет статистически значимых различий между выборками. Препарат не влияет на уровень давления пациентов')