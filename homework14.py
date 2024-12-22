#EX1

# def f(a, b):
#     lst = [a +b, a - b, a * b, a / b]
#     return lst
#
#
# print(f(1, 2))

#EX2

# def a(*args):
#     lst = [sum(args) / len(args)]
#     l = []
#     l = len(args)
#     args = sorted(args)
#     if l % 2 == 0:
#         lst.append(args[l // 2] + args[l // 2 - 1] / 2)
#     else:
#          lst.append(args[l // 2])
#     lst.append(sum(args))
#     p = 1
#     for i in args:
#         p *= i
#     lst.append(p)
#     return lst
#
# print(a(1, 2, 3, 4, 5, 6))

#EX3

# def power(x, y = None):
#     if y is None:
#         return x ** 2
#     elif x == 0 and y <= 0:
#         return "exception"
#     else:
#         return x ** y
#
#
# print(power(0, 0))

#EX4

# fruits = input('fruits = ')
# prices = input('prices = ')
# fruitsL = fruits.split(' ')
# pricesL = prices.split(' ')
#
# def f(*, fruit, price):
#     d = {}
#     for i in fruit:
#         a = fruit.index(i)
#         if a >= len(price):
#             d[i] = None
#         else:
#             d[i] = price[a]
#     return d
#
#
#
# print(f(fruit = fruitsL, price = pricesL))