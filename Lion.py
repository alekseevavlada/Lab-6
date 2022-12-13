class buildings:
    def __init__(self, square, price, residents):
        self.square = square
        self.price = price
        self.residents = residents

    def get_price(self):
        all_price = self.square * self.price
        return all_price

    def all(self):
        all_all = self.price / self.residents
        return all_all

class village(buildings):
    def __init__(self, square=50, price=100000, residents=4):
        self.__square = square
        self.__price = price
        self.__residents = residents
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        self.all_all = super().all()

    def reload(self, square):
        self.__square += square
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        print("Новая общая стоимость: ", self.all_price)

    def print(self):
        print("Деревенский дом")
        print("Соотношение стоимости к числу проживающих: ", self.all_all)

class anthill(buildings):
    def __init__(self, square=1500, price=25000, residents=120):
        self.__square = square
        self.__price = price
        self.__residents = residents
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        self.all_all = super().all()

    def reload(self, square):
        self.__square += square
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        print("Новая общая стоимость: ", self.all_price)

    def print(self):
        print("Многоэтажный дом")
        print("Соотношение стоимости к числу проживающих: ", self.all_all)

class hostel(buildings):
    def __init__(self, square=1500, price=5000, residents=120):
        self.__square = square
        self.__price = price
        self.__residents = residents
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        self.all_all = super().all()

    def reload(self, square):
        self.__square += square
        super().__init__(self.__square, self.__price, self.__residents)
        self.all_price = super().get_price()
        print("Новая общая стоимость: ", self.all_price)

    def print(self):
        print("Общежитие")
        print("Соотношение стоимости к числу проживающих: ", self.all_all)

v = village()
v.print()
v.reload(70)
a = anthill()
a.print()
a.reload(1700)
h = hostel()
h.print()
h.reload(1700)