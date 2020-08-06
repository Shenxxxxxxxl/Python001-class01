from abc import ABCMeta, abstractmethod
class Zoo(object):

    def __init__(self,name):
        self.name = name
        self.animals = []

    def add_animal(self,animal):
        if animal in self.animals:
            print("已经存在同一个动物实例")
        else:
            self.animals.append(animal)

class Animal(metaclass=ABCMeta):
    #a_type类型 figure体型
    @abstractmethod
    def __init__(self,a_type,figure,character):
        if '小' in figure:
            self.figure = 1 #体型
        elif '中' in figure:
            self.figure = 2 #体型
        else:
            self.figure = 3
        self.a_type = a_type #类型
        self.character = character #性格
    
    #是否属于凶猛动物
    @property
    def is_ferocious(self):
        if (self.figure >= 2 and self.a_type == '食肉' and self.character == '凶猛'):
            return True
        else:
            return False


class Cat(Animal):
    call = "miaomiao"
    def __init__(self,name, a_type,figure,character):
        self.name = name
        super().__init__(a_type,figure,character)

    def is_pet(self):
        if super().is_ferocious:
            return False
        return True

def getattr(zoo, animal):
    try:
        kclass = globals()[animal]
    except Exception as e:
        print("%s类在该文件中不存在" % (animal))
        return False
    if kclass is None:
        print("传入非正确类型")
        return False
    kk = kclass('','','','')
    if isinstance(kk, Animal):
        for animal in zoo.animals:
            if isinstance(animal,kclass):
                print("存在")
                return True
    return False
    


if __name__ == '__main__':
    z = Zoo('时间动物园')
    print("动物园名称: %s"%(z.name))
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('小可爱 2', '食肉', '大', '凶猛')
    print("猫猫名称: %s，是否属于凶猛动物: %s，是否适合作为宠物%s，叫声%s"%(cat1.name, cat1.is_ferocious,cat1.is_pet(),cat1.call))
    print("猫猫名称: %s，是否属于凶猛动物: %s，是否适合作为宠物%s，叫声%s"%(cat2.name, cat2.is_ferocious,cat2.is_pet(),cat2.call))
    print(dir(cat1))
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(cat2)
    print("----------------------")
    have_cat = getattr(z, 'Cat')
    have_as = getattr(z, 'As')
