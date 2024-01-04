# Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты? 
import math

def combinations (n, k):
    return(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))
print(combinations(36, 4))
print(math.comb(36, 4))