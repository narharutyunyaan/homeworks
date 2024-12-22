# import time
# import datetime
#EX1

# def speed(mile: int | float) -> int | float:
#     kmH = mile * 1.6
#     mH = kmH * 1000 / 3600
#     return kmH, mH
# print(speed(40))

#EX2

# c = time.time()
# l = []
# for i in range(1, int(10e7) + 1):
#     if i % 3 == 0:
#         l.append(i)
# a = len(l)
# print(a)
# print(int(10e7) // 3)
# b = time.time()
# print(b - c)

#EX3

# a = []
# b = []
# list = [2, 4, 7, 7, 9, 10]
# for i in range(len(list)):
#     if i % 2 == 0:
#         a.append(list[i])
#     else:
#         b.append(list[i])
# medA = sum(a) / len(a)
# medB = sum(b) / len(b)
# print(medA)
# print(medB)
