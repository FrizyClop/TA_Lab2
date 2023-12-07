import ClassPerson

first = ClassPerson.Person("Максим","Лютый",2)
second = ClassPerson.Person("Алсексей", "Леонов",3)
third = ClassPerson.Person("Дмитрий","Чесноков",4)

first.MainInformation()
second.MainInformation()
third.MainInformation()

del first
input()