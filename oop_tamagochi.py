class AliveStatus():
    def __init__(self) -> None:
        self.__val = True
    
    @property
    def val(self):
        return self.__val
    
    @val.setter
    def val(self, val):
        if not self.__val:
            return
        self.__val = val


class PrivateField():
    def __init__(self, alive, start_val=0) -> None:
        self.__val = start_val
        self.overflow = False
        self.is_alive = alive

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        if not self.is_alive.val:
            return
        
        self.__val = val
        if self.__val < 0:
            self.__val = 0
        if self.__val >= 100:
            self.__val = 100
            self.overflow = True
            self.is_alive.val = False
    


class Dog():
    def __init__(self, name):
        self.name = name
        self.is_alive = AliveStatus()
        self.__hungry = PrivateField(self.is_alive)
        self.__sadness = PrivateField(self.is_alive)
        self.__tiredness = PrivateField(self.is_alive)
        self.age = 0


    # def __set_attr(self, name, val):
    #     setattr(self, name, val)
    #     x = getattr(self, name)
    #     if x < 0:
    #         setattr(self, name, 0)
    #     elif x >= 100:
    #         setattr(self, name, 100)
    #         self.is_alive = False
    def alive_check(f):
        def wrapper(self, val):
            if not self.is_alive:
                return
            self.is_alive = not f(self, val)
        return wrapper

    @property
    def hungry(self):
        return self.__hungry.val

    @hungry.setter
    @alive_check
    def hungry(self, val):
        self.__hungry.val = val

    @property
    def sadness(self):
        return self.__sadness.val

    @sadness.setter
    def sadness(self, val):
        # if not self.is_alive:
        #     return
        self.__sadness.val = val
        # self.is_alive = not self.__sadness.overflow

    @property
    def tiredness(self):
        return self.__tiredness.val

    @tiredness.setter
    def tiredness(self, val):
        self.__tiredness.val = val

    def spend_day(self):
        if not self.is_alive:
            return
        self.age += 1
        self.hungry += 40
        self.sadness += 20
        self.tiredness -= 40

    def status(self):
        print(
            f"Dog {self.name} - {self.age}\nголод: {self.hungry}\nгрусть: {self.sadness}\nусталость: {self.tiredness}")

    def eat(self):
        self.hungry -= 20
        self.sadness -= 10

    def play(self):
        self.sadness -= 30
        self.hungry += 20
        self.tiredness += 20

    def relax(self):
        self.sadness += 10
        self.tiredness -= 40


dog = Dog("Rex")
# for _ in range(10):
#     dog.spend_day()
#     dog.eat()
#     dog.eat()
#     dog.eat()
#     dog.play()
#     dog.relax()
dog.sadness = 120
dog.status()
print(dog.is_alive.val)

# Сделать метод Play, грусть -30, голод +20, усталость +20
# Метод отдых, грусть + 10, усталость -40
# Если один из параметров грусть , голод , усталость превысил 100, смерть, после этого параметры не меняются.
# Грусть голод и усталость не могут быть меньше нуля.
