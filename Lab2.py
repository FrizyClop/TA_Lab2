class Person:
    
    def __init__(self, n, s, q = 1):
        self.name = n
        self.surname = s
        self.qualification = q
    
    def __del__(self):
        print("До свидания, мистер " + self.name + " " + self.surname)

    def MainInformation(self):
        print(self.surname + " " + self.name + ". Квалификация:" + str(self.qualification))

first = Person("Максим","Лютый",2)
second = Person("Алсексей", "Леонов",3)
third = Person("Дмитрий","Чесноков",4)

first.MainInformation()
second.MainInformation()
third.MainInformation()

del first
input()