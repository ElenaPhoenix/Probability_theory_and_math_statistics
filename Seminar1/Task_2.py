# Смоделируем ситуацию, когда бросают две игральные кости одновременно 360 раз. 
# Посчитаем относительную частоту события, когда на одной кости выпадает 1, в на другой 2
import numpy as np

np.random.seed(1)
n = 360
c = np.random.randint(1, 7, n)
d = np.random.randint(1, 7, n)
print(c, d)
a = c [(c == 1) & (d == 2)]
m = len(a)
W = m/n
print(W)