#EX1

# list1 = [1, 2, 45, 74, 96, 82, 79, 65, 37, 97, 97]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#      (list2.append(i))
# a = max(list2)
# print(a)

#EX2

# num_list = [13, 65, 77, 52, 10, 11, 98, 8, 6, 42, 52]
# EvenNumbers = []
# OddNumbers = []
# for i in num_list:
#     if i % 2 == 0:
#         (EvenNumbers.append(i))
#     else:
#         (OddNumbers.append(i))
# print(EvenNumbers)
# print(OddNumbers)

#EX3

# lst = [43, 900, 567, 88, 988, 0, 52, 988, 27, 29, 988]
# a = max(lst)
# for i in lst:
#     if i == a:
#         lst.remove(i)
# b = max(lst)
# print(b)

#EX4

# num = int(input('num = '))
# lst = []
# for i in range(0, num, 1):
#     if i % 3 == 0:
#         lst.append(i**3)
# print(lst)



# 5. Գրել ծրագիր, որը․
#    - իր մեջ կունենա սահմանված երկու tuple,
#      օրինակ` tuple_1 = (11, 55, 54, “abc”, 90, 102, “asdasd”, “qwerty”),
#              tuple_2 = (“bbb”, 44, 14, 11, 99, “a”),
#    - կտպի True, եթե գոյություն ունի առնվազն մեկ արժեք, որը առկա է
#      և tuple_1-ի, և tuple_2-ի մեջ, հակառակ դեպքում տպի False,
#      օրինակ՝ տվյալ դեպքում երկու tuple-ների մեջ կա 11 թիվը, այդ պատճառով պետք է տպի True:





# 6*. Գրել ծրագիր, որը․
#    - կունենա tuple, օրինակ tuple_1 = (4, 5, 5, 2, 3, 2, 3, 4, 5, 5, 3),
#    - կգտնի, թե որ թվից է ամենից շատ հանդիպում tuple_1 ի մեջ
#      և կտպի այդ թիվն ու քանակը, թե քանի անգամ է հանդիպում,
#    - հաշվի առնել որ ամենաշատ հանդիպով սիմվոլներ կարող են մի քանի հատ լինել,
#    տվյալ օրինակի դեպքում պետք է տպի
#    Number is 5, count is 4
#    Քանի որ թվերը հանդիպում են հետևյալ
#    հաճախականությամբ
#    4 - 2
#    5 - 4
#    2 - 2
#    3 - 3
