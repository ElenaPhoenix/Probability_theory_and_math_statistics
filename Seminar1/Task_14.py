# В ящике находится 10 красных, 5 черных, 5 зеленых шаров. Наудачу вынимают 6 шаров.
# Какова вероятность, что вынуты 3 красных, 2 черных, 1 зеленый?
import math
P = math.comb(10,3)*math.comb(5,2)*math.comb(5,1) / math.comb(20,6)
print(P)