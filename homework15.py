import random

#EX1

# def temp(c: int | float, /, c_type = 'c' , result = 'f') -> int | float:
#     if c_type == 'c' and result == 'f':
#         f = c * (9 / 5) + 32
#         return f
#     elif c_type == result:
#         return c
#     elif c_type == 'f' and result == 'c':
#         celsius = (c - 32) / (9 /  5)
#         return celsius
#
#
# print(temp(27, 'c', 'f'))

#EX2

# def start_game():
#     myScore = 0
#     robotScore = 0
#
#     while myScore != 5 and robotScore != 5:
#         myNumber = int(input('My Number = '))
#         robotNumber = random.randrange(1, 7)
#         print(robotNumber)
#         if myNumber < 1 or myNumber > 6:
#             print('wrong number')
#             continue
#         elif myNumber > robotNumber:
#             myScore += 1
#         elif myNumber > robotNumber:
#             robotScore += 1
#         print('my Score: ', myScore )
#         print('robot Score: ', robotScore)
#
#     return {myScore, robotScore}
#
#
#
# print(start_game())






# 3․ Գրել հետևյալ ծրագիրը․
#    - տրված բառարանը բաղկացած է տրանսպորտային միջոցներից և դրանց քաշից՝ կիլոգրամներով,
#    օրինակ՝ dict_1 = {"Sedan": 1500, "SUV": 2000,
#                    "Pickup": 2500, "Minivan": 1600,
#                    "Van": 2400, "Semi": 13600,
#                    "Bicycle": 12, "Motorcycle": 110},
#    - մեկ տողով կառուցեք 2 տոննայից ցածր և հավասար քաշ ունեցող մեքենաների անունների
#      ցուցակը որպես list՝ բոլորի անունները մեծատառ դարձնելով,
#    - տվյալ օրինակի դեպքում կտպի`
#      ['SEDAN', 'SUV', 'MINIVAN', 'BICYCLE', 'MOTORCYCLE']։

# dict_1 = {"Sedan": 1500, "SUV": 2000,
#                    "Pickup": 2500, "Minivan": 1600,
#                    "Van": 2400, "Semi": 13600,
#                    "Bicycle": 12, "Motorcycle": 110}
# lst1 = []
