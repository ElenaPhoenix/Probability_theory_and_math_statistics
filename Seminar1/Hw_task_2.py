# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
import math

P = 1 / math.comb(10, 3)
print(round(P, 4)) # P = 0.0083