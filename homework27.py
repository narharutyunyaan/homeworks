# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
#    - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
#      (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։




# import math
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
#             raise ValueError('Wrong Triangle')
#
#     def sides(self):
#         return [self.a, self.b, self.c]
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         w = (self.a + self.b + self.c) / 2
#         S = (w * (w - self.a) * (w - self.b) * (w - self.c)) ** 0.5
#         return S
#
#     def type(self):
#         if self.a == self.b or self.a == self.c or self.b == self.c:
#             return 'equal'
#         elif self.a == self.b == self.c:
#             return 'equilateral'
#         else:
#             return 'irregular'
#
#     def angle(self):
#         angle_A = math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))
#         angle_B = math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
#         angle_C = math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
#
#         angle_A_deg = math.degrees(angle_A)
#         angle_B_deg = math.degrees(angle_B)
#         angle_C_deg = math.degrees(angle_C)
#         return [angle_A_deg, angle_B_deg, angle_C_deg]
#     def rightTriangle(self):
#         for i in self.angle():
#             if i == 90:
#                 return True
#         return False
#
#
# t = Triangle(1, 5, 5)
# print(t.area())
# print(t.sides())
# print(t.perimeter())
# print(t.type())
# print(t.angle())
# print(t.rightTriangle())