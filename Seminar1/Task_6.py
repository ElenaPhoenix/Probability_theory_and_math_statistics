# Из колоды, состоящей из 36 карт, случайным образом выбраны 5. Сколькими способами можно выбрать эти карты так, чтобы среди них оказалось 2 туза?
import math

m = math.comb(4, 2)
print('Число сочетаний по 2 туза из 4-х:', m)
n = math.comb(32, 3)
print('Число сочетаний по 3 карты из 32-х (не учитываются тузы):', n)
# Сочетания 5 карт из 36, чтобы среди них оказалось 2 туза
C = m * n
print(C)