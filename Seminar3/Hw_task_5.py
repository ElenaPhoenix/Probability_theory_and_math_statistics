# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, 
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
# A - в первый месяц выйдут из строя все детали
# B - в первый месяц выйдут из строя только две детали
# C - в первый месяц выйдет из строя хотя бы одна деталь
# D - в первый месяц выйдут из строя от одной до двух деталей
P_A = 0.1 * 0.2 * 0.25
P_B = (0.9 * 0.2 * 0.25) + (0.1 * 0.8 * 0.25) + (0.1 * 0.2 * 0.75)
P_C = P_A + P_B + (0.9 * 0.8 * 0.25) + (0.1 * 0.8 * 0.75) + (0.9 * 0.2 * 0.75)
P_D = P_B + (0.9 * 0.8 * 0.25) + (0.1 * 0.8 * 0.75) + (0.9 * 0.2 * 0.75)
print(f'В первый месяц выйдут из строя все детали: ', P_A) # 0,005
print(f'В первый месяц выйдут из строя только две детали: ', P_B) # 0,08
print(f'В первый месяц выйдет из строя хотя бы одна деталь: ', P_C) # 0,46
print(f'В первый месяц выйдут из строя от одной до двух деталей: ', P_D) # 0,455