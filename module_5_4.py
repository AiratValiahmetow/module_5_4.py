class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        k = super().__new__(cls)
        cls.houses_history.append(args[0])
        return k
    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
            print(f'{self.name} снесён, но он останется в истории')


    def go_to(self, new_floor):
        for k in (range(new_floor)):
            k += 1
            if new_floor > self.number_of_floors or new_floor < 1:
                 print("Такого этажа не существует")
                 break
            else:
                 print(k)

    def __len__(self):
            return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors} '

    def __eq__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
            if isinstance(value, int):
                self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
            return self.__add__(value)

    def __iadd__(self, value):
            if isinstance(value, int):
                self.number_of_floors += value
            return self
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)




