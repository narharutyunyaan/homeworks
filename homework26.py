# EX 1

# import math

#
#
# def circle(r, alpha):
#     S = ((math.pi * r) ** 2) * alpha / 360
#     return S
#
# print(circle(4, 180))


# EX 2
# def number(n):
#
#     if n <= 0:
#         raise ValueError("Number must be greater than 0")
#     lst = [
#         ("M", 1000),
#         ("CM", 900),
#         ("D", 500),
#         ("CD", 400),
#         ("C", 100),
#         ("XC", 90),
#         ("L", 50),
#         ("XL", 40),
#         ("X", 10),
#         ("IX", 9),
#         ("V", 5),
#         ("IV", 4),
#         ("I", 1)]
#     result = ""
#     for k, v in lst:
#         while n >= v:
#             result += k
#             n -= v
#
#     return result
#
#
# print(number(17))
# print(number(72))
# print(number(0))
# print(number(746))
# print(number(90))
# print(number(2000))



# 3․ Գրել ֆունկցիա, որը․
#    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
#      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
#    օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
#            output = ["aba", "vcd", "aba"],
#
#            input = ["aba", "aa", "z", "advc", "vcd", "aba"]
#            output = ["advc"],

# a = ["aba", "aa", "z", "ad", "vcd", "aba"]
#
# def l(lst):
#     for i in a:
#          p = len(i)
#          m = max(p)
#
#
#
#
#
#
# print(l(a))




# 4. Գնահատեք Ձեր գրած կոդերը Big O notation-ի միջոցով։