import math

# HOMEWORK 3


#EX1

# age = int(input('age = '))
# if age < 0:
#     print('wrong')
# elif age < 18:
#     print('you are under 18')
#
# else:
#     print('you are over 18')


#EX2

# a = int(input('a = '))
# b = int(input('b = '))
# c = a * b
# if c % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

#EX3

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     print(x)
# elif x == y:
#     print(x)
# else:
#     print(y)

# HOMEWORK 4

#EX1

# text = input('text = ')
# print(text[0], text[-1])
# print(len(text))

#EX1

# text = input('text = ')
# length = len(text)
# if len(text) % 2 == 0:
#     print(text[:length//2])
# else:
#     print(text[length // 2])

#EX2

# #1
# text = input('text = ')
# #2
# print(text.isupper())
# #3
# print(text.islower())
# #4
# if len(text) % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
# #5
# print(text.count('a'))
# #6
# print(text.isalpha())
# #7
# print(text.lower())
# #8
# print(text.title())
# #9
# print(text.find("a"))
# #10
# print(text.replace('a', 'b', 1))
# #11
# print('00000' + text + '00000')

#EX4

# name=input("name=")
# lastname = input("lastname=")
# age = input("age=")
# print(f"Hello {name.title()} {lastname.title()}. You are {age} years old.")


#HOMEWORK16

#EX1

# lst1 = ['square', 'rectangle', 'circle', 'triangle']
# def squareS(a: int | float) -> int | float:
#     return a ** 2
# def recrangleS(a: int | float, b: int | float) -> int | float:
#     return a * b
# def circleS(r: int | float) -> int | float:
#     return (math.pi * r) ** 2
# def triangleS(a: int | float, h: int | float) -> int | float:
#     return (a * h) / 2
#
#
# def geoFigS(figure: str):
#     if geoFigure == 'square':
#         a = float(input('a = '))
#         return squareS(a)
#     elif geoFigure == 'rectangle':
#         a = float(input('a = '))
#         b = float(input('b = '))
#         return recrangleS(a, b)
#     elif geoFigure == 'circle':
#         r = float(input('r = '))
#         return circleS(r)
#     elif geoFigure == 'triangle':
#         a = float(input('a = '))
#         h = float(input('h = '))
#         return triangleS(a, h)
#     else:
#         raise Exception("wrong figure")
#
#
# while True:
#     geoFigure = input('geoFigure = ')
#     try:
#         if lst1.index(geoFigure) >= 0:
#             print(geoFigS(geoFigure))
#     except Exception:
#         print('wrong GeoFigure: Please try again')
#     finally:
#         continue