# В среднем при изготовлении напольного покрытия на 1  кв.м   встречается 2 вкрапления. Какова вероятность, что на 1 кв.м будет не более 1 вкрапления?
import math

lamb = 1 * 2
P0 = math.pow(lamb, 0) * math.pow(2.72, -lamb)/ math.factorial(0)
P1 = math.pow(lamb, 1) * math.pow(2.72, -lamb)/ math.factorial(1)
P = P0 + P1
print(P)