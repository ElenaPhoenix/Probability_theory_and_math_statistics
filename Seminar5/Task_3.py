# Проверка на нормальность. Тест Шапиро-Уилка
# Применяется для небольшой выборки

import numpy as np
import pylab # для отображения 2-х и 3-х мерных массивов
import scipy.stats as stats

s = np.random.normal(0, 1, 50)

print(s)
print(stats.shapiro(s)) # ShapiroResult(statistic=0.9741081595420837, pvalue=0.33723798394203186)
# pvalue=0.33723798394203186 > alfa=0,05 (или иногда alfa=0,1) => выбор в пользу 0-й гипотезы