# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
import math

p = 0.0004
n = 5000
m0 = 0
m2 = 2
lamb = p * n
# Формула Пуассона
P0 = pow(lamb, m0) * math.exp(-lamb) / math.factorial(m0)
P2 = pow(lamb, m2) * math.exp(-lamb) / math.factorial(m2)
# Сравнение с формулой Бернулли
P0 = math.comb(n, m0) * pow(p, m0) * pow(1-p, (n-m0))
P2 = math.comb(n, m2) * pow(p, m2) * pow(1-p, (n-m2))
print(f'Вероятность, что ни одна лампочка не перегорит в первый день: {round(P0*100, 1)}%') # 0,135 ≈ 13,5%
print(f'Вероятность, что перегорят ровно две лампочки: {round(P2*100, 1)}%') # 0,271 ≈ 27,1%