# 1․ Գրել BankUser class, որը․
#    - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#      -- անունը և ազգանունը - տառերից բաղկացած,
#      -- տարիքը - բնական թիվ,
#      -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
#      -- գումարը - դրական թիվ,
#      -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
#    - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#    - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու անունը, ազգանունը և տարիքը,
#    - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
#    - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
#    - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
#    - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված,
#    - կունենա մեթոդ, որի միջոցով կվերականգնվի հասանելիությունը անունը, ազգանունը և հաշվեհամարի վերջին 4 թվանշանները մուտքագրելուց հետո։
from idlelib.run import Executive


class BankUser:
    def __init__(self, name, surname, age, account, money, password):
        if not name.isalpha() or not surname.isalpha():
            raise ValueError('wrong name or surname:')
        elif not age.isdigit() or age <= 0:
            raise ValueError('wrong age:')
        elif len(account) != 16:
            raise ValueError('wrong account number')
        elif money < 0:
            raise ValueError('wrong money')
        elif len(password) < 8 or not password.isalpha():
            raise ValueError('wrong password')
        self._name = name
        self._surname = surname
        self._age = age
        self.__account = account
        self.__money = money
        self.__password = password
    def get_user_info(self):
        return {'Name': self._name, 'Surname': self._surname, 'Age': self._age}
    def get_account_info(self, password):
        if password != self.__password:
            raise Exception('wrong password')
        return {'Account': self.__account, 'Money': self.__money}
    def add_money(self, money):
        self.__money += money
    def withdraw_money(self, money):
        if self.__money - money < 0:
            raise Exception('not enough money')
        self.__money -= money

bankuser = BankUser('Narek', 'Harutyunyan', 'abc', '12345679', 50000, '1234')
print(bankuser.get_user_info())

