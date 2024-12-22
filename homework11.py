#EX1

# dict = {"name": "Kelly",
#                "age": 25,
#                "salary": 8000,
#                "city": "New york"}
# keys = ["name", "salary", 'hair_color']
# d = {}
# for i in keys:
#     d[i] = dict.get(i)
# print(d)

#EX2

# sampleDict = {
#
#     "class A": {
#         "student_1": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         },
#          "student_2": {
#              "name": "Jack",
#                    "marks": {
#                    "physics": 80,
#                     "history": 75
#                    }
#          }
#     }
# }
# s = sampleDict.values()
# a = []
#
# for i in s:
#     a = i.values()
#
# for k in a:
#     # print(k)
#     # print(k.get('name'))
#     if k.get('name') == 'Mike':
#         print(k.get('marks').get('history'))

#EX3

#
# dict1 = {'d': 50, 'a': 10, 'b': 20, 'c': 30, 'e' : 40}
# dict2 = {'b': 30, 'a': 5, 'd': 25, 'c': 20}
# dict3 = {}
# l1 = dict1.keys()
# l2 = dict2.keys()
# # print(l1)
# # print(l2)
# u = l1 | l2
# for i in u:
#     if dict1.get(i) != None and dict2.get(i) != None:
#         m = max(dict1.get(i), dict2.get(i))
#         dict3[i] = m
#     elif dict1.get(i) != None and dict2.get(i) == None:
#         dict3[i] = dict1.get(i)
#     else:
#         dict3[i] = dict2.get(i)
# print(dict3)