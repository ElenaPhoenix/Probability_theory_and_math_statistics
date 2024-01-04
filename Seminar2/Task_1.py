# 3 раза подбрасываем монетку (n=3). Какая вероятность, что  орел выпадет 0 раз, 1 раз, 2 раза и 3 раза.
# Биномиальное распределние. Формула Бернулли
import math
p = 1/2
n = 3
q = 1 - p
for k in range (0, 4):
    P = math.comb(n, k)*pow(p, k)*pow(q, n - k)
    print(f"P(k={k}) = {P}")
print(f'P0 = {math.comb(3, 0)/8}')
print(f'P1 = {math.comb(3, 1)/8}')
print(f'P2 = {math.comb(3, 2)/8}')
print(f'P3 = {math.comb(3, 3)/8}')