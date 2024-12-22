#EX1

# dict1 = {'S  001': ['Math', 'Python'], ' S    002': ['Math', 'English']}
# dict2 = {}
# for i in dict1.keys():
#     a = i.replace(' ', '')
#     dict2[a]  = dict1.get(i)
# print(dict2)

#EX2

# import collections
# dict1 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# a = collections.Counter(dict1).most_common(3)
# for i in a:
#     print(str(i[0]) + ' = ' + str(i[1]))

#EX3

# fruits = [{'fruit': 'orange', 'price': 150},
#                      {'fruit': 'apple', 'price': 100},
#                      {'fruit': 'banana'}]
# a = 0
# for i in fruits:
#     if str(i.get('price')).isdigit():
#         a += i.get('price')
# print(a)