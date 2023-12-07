class Person:
    
    def __init__(self, n, s, q = 1):
        self.name = n
        self.surname = s
        self.qualification = q
    
    def __del__(self):
        print("До свидания, мистер " + self.name + " " + self.surname)

    def MainInformation(self):
        return self.surname + " " + self.name + ". Квалификация:" + str(self.qualification)