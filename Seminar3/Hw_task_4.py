# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, 
# сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?
# А - сессия сдана
# B1 - студент с факультета А P(B1) = 0,25
# B2 - студент с факультета B P(B2) = 0,25 
# B3 - студент с факультета C P(B3) = 0,5 
# P(A) = P(B1)*P(A|B1) + P(B2)*P(A|B2) + P(B3)*P(A|B3)
# P(B1|A) = P(A|B1) * P(B1) / P(A)
# P(B2|A) = P(A|B2) * P(B2) / P(A)
# P(B3|A) = P(A|B3) * P(B3) / P(A)
P_A = (0.25 * 0.8) + (0.25 * 0.7) + (0.5 * 0.9)
P_B1 = 0.8 * 0.25 / P_A
P_B2 = 0.7 * 0.25 / P_A
P_B3 = 0.9 * 0.5 / P_A
# print(P_A) # P(A) = 0,825
print(f'Вероятность, что сдавший сессию студент учится на факультете A: ', P_B1) # 0,242
print(f'Вероятность, что сдавший сессию студент учится на факультете B: ', P_B2) # 0,212
print(f'Вероятность, что сдавший сессию студент учится на факультете C: ', P_B3) # 0,545