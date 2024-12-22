import time
import random
import datetime
#EX1

# a = ['Narek', 'Varazdat', 'Ruben', 'Lusine', 'Anna', 'Ashot']
# for i in a:
#     if 5 >= len(i) > 0:
#         print(i)
#         time.sleep(2)

# EX2
#
# def number(a):
#     strA = str(a)
#     if len(strA) % 2 == 0:
#         middle = int(len(strA) / 2)
#         left, right = strA[:middle], strA[middle:]
#         print(left, right)
#         rightSum = 0
#         leftSum = 0
#         for k in right:
#             rightSum += int(k)
#         for i in left:
#             leftSum += int(i)
#         return rightSum == leftSum
#     else:
#         middle = int(len(strA) / 2)
#         mid = strA[middle:][0]
#         left, right = strA[:middle], strA[middle + 1:]
#         # print(mid, left, right)
#         rightSum = 0
#         leftSum = 0
#         for k in right:
#             rightSum += int(k)
#         for i in left:
#             leftSum += int(i)
#         return rightSum == leftSum and int(mid) % 2 == 0
#
#
#
# print(number(19446))

#EX3

# girls = ['Gohar', 'Ani', 'Tatev']
# boys = ['Gor', 'Vahe', 'Vardan', 'Karen', 'Ashot']
# random.shuffle(girls)
# random.shuffle(boys)
# for g, b in zip(girls, boys):
#     print(g, '-', b)

#EX4

# print(datetime.datetime(year=2024, month=12, day=1).strftime('%A'))