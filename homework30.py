# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։



class MyShow:
    def __init__(self, showName, showPlatform, showYear, showSeria = 1, rating = None, actors = []):

        self.__showName = showName
        self.__showPlatform = showPlatform
        self.__showYear = showYear
        self.__showSeria = showSeria
        self.__rating = rating
        self.__actors = actors
    def get_showName(self):
        return self.__showName
    def get_showPlatform(self):
        return self.__showPlatform
    def get_showYear(self):
        return self.__showYear
    def get_showSeria(self):
        return self.__showSeria
    def get_rating(self):
        return self.__rating
    def get_actors(self):
        return self.__actors

    def set_showSeria(self, value):
        self.__showSeria = value
    def set_rating(self, value):
        self.__rating = value

    def delete_rating(self):
        self.__rating = None
    def add_actor(self, actor):
        self.__actors.append(actor)
    def remove_actor(self, actor):
        self.__actors.remove(actor)
    def info(self):
        i = {'showName': self.__showName, 'showPlartform': self.__showPlatform, 'showYear': self.__showYear, 'showSeria': self.__showSeria, 'rating': self.__rating, 'actors': self.__actors}
        return i
myshow = MyShow('squid game', 'Netlix', 2024, 4, 60, ['abc', 'ksk', 'jncnjk', 'kna'])
print(myshow.get_showName(), myshow.get_showYear(), myshow.get_showPlatform(), myshow.get_showSeria(), myshow.get_rating(), myshow.get_actors())
myshow.set_showSeria(7)
print(myshow.get_showSeria())
myshow.add_actor('Michael Jackson')
print(myshow.get_actors())
myshow.remove_actor('jncnjk')
print(myshow.get_actors())



