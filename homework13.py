#EX1

# import math
# from random import random
#
# a = float(input('a = '))
# b = math.radians(a)
# print(b)
# x = math.sin(b)
# y = math.cos(b)
# print(x)
# print(y)

#EX2

# import random
#
# x = []
# for i in range(10):
#     a = random.randrange(10, 100)
#     x.append(a)
# print(x)
# p = []
# for i in x:
#     if i % 2 == 0:
#         p.append(i)
# print(random.choices(p, k = 3))
# f = (sum(p) / len(p)) ** 0.5
# print(f)

#EX3

# import random
# yourScore = 0
# robotScore = 0
# while yourScore != 5 and robotScore != 5:
#     a = input('type your choice: rock or paper or scissors:  ')
#     b = ['rock', 'paper', 'scissors']
#     c = random.choice(b)
#     print('robot choice: ', c)
#     if a == 'rock' and c == 'scissors':
#         yourScore += 1
#     elif a == 'rock' and c == 'paper':
#         robotScore += 1
#     elif a == 'paper' and c == 'rock':
#         yourScore += 1
#     elif a == 'paper' and c == 'scissors':
#         robotScore += 1
#     elif a == 'scissors' and c == 'rock':
#         robotScore += 1
#     elif a == 'scissors' and c == 'paper':
#         yourScore += 1
#     elif a == c:
#         yourScore += 0
#         robotScore += 0
#     else:
#         print('wrong input')
#     print('your score: ', yourScore)
#     print('robot score: ', robotScore)
# if yourScore == 5:
#     print('YOU WOOON!', chr(128513))
# elif robotScore == 5:
#     print('YOU LOSE', chr(128532))