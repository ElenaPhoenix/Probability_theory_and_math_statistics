# Случайным образом выбирается корзина (в 1-й - 3 красных и 5 зеленых мячей, во 2-й - все красные, в 3-й - все зеленые)
# и случайным образом из нее берут мяч
# Какова вероятность, что мяч окажется зеленым?
# А - взяли зеленый мяч
# В1 - взяли 1 корзину
# В2 - взяли 2 корзину
# В3 - взяли 3 корзину
# P = P(B1)*P(A|B1) + P(B2)*P(A|B2) + P(B3)*P(A|B3)
# P = (1/3 * 5/8) + (1/3 * 0) + (1/3 * 1)
# print(P) # P = 0.54166667