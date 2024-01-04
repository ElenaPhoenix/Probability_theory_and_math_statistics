# В магазине 20 покупателей. Сколькими способами они могут образовать очередь из 5 человек?
import math

def arrangements (n, k):
    return(math.factorial(n) // math.factorial(n - k))
print(arrangements(20, 5))
print(math.perm(20, 5))