class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f'Меня зовут {self.name}. Я родился {self.birth_date},'
        f' по профессии {self.occupation}, {education_status}.')




class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name,birth_date, occupation, higher_education)
        self.group_name = group_name


    def introduce(self):
        print(f' Здарова меня зовут {self.name}, я на группе {self.group_name}.'
              f' Я родился {self.birth_date} и я {self.occupation}.')





class Friend(Person):
    def __init__(self, name, friend_of, birth_date, hobby, higher_education, occupation):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_of = friend_of


    def introduce(self):
        print(f'Салам меня зовут {self.name}, я друг {self.friend_of},'
              f' я родился {self.birth_date}. Моё хобби {self.hobby} и я работаю {self.occupation}.')






person1 = Person("Алинур", '12.05.2000', occupation = "Медик", higher_education = True)
person2 = Person("Акылай",  '03.11.1998', occupation = "Программист", higher_education = False)
person3 = Person("Артур", '25.08.2002', occupation = "Инжинер", higher_education = True)

print("Person1:", person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print("Person2:", person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print("Person3:", person3.name, person3.birth_date, person3.occupation, person3.higher_education)


print("\nПредс-е объектов:")
person1.introduce()
person2.introduce()
person3.introduce()


print("\nДочерний класс, подкласс:")
Classmate1 = Classmate("Бектур", "05.12.2005", "Студент", False, "ИСТ 1-22")
Classmate2 = Classmate("Алыбек", "03.06.2006", "Студент", False, "ПИ 3-34")
Classmate1.introduce()
Classmate2.introduce()


print("\nДочерний класс, подкласс:")
Friend1 = Friend("Саша",   "Виктора", "01.10.2002", "программирования", True, "Программистом")
Friend2 = Friend("Андрей",  "Алинура", "21.07.1997", "валейбол", True, "Сантехником")
Friend1.introduce()
Friend2.introduce()





