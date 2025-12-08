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
    def __init__(self, name, group_name, friend_of, birth_date, occupation, higher_education):
        super().__init__(name,birth_date, occupation, higher_education)
        self.group_name = group_name
        self.friend_of = friend_of

    def introduce(self):
        print(f"Здарова меня зовут {self.name}, я из группы {self.group_name}. "
              f"Я одногруппник {self.friend_of}, я родился {self.birth_date} и я {self.occupation}")


class Friend(Person):
    def __init__(self, name, friend_of, birth_date, hobby, higher_education, occupation):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_of = friend_of


    def introduce(self):
        print(f'Салам меня зовут {self.name}, я друг {self.friend_of},'
              f' я родился {self.birth_date}. Моё хобби {self.hobby} и я работаю {self.occupation}.')



class BestFriend(Friend):
    def __init__(self, name, friend_of, birth_date, hobby, higher_education, occupation, shared_memory):
        super().__init__(name, friend_of, birth_date, hobby, higher_education, occupation)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наше лучшее воспоминание: {self.shared_memory}")


    def introduce(self):
        super().introduce()
        print(f"Наше лучшее воспоминание: {self.shared_memory}")



print("\nДочерний класс, подкласс(Classmate):")
Classmate1 = Classmate("Бектур", "ИСТ 1-22", "Путина", "05.12.2005",  "Студент", False)
Classmate2 = Classmate("Алыбек", "ПИ 3-34", "Трампа", "03.06.2006", "Студент", False)
Classmate1.introduce()
Classmate2.introduce()


print("\nДочерний класс, подкласс(Friend):")
Friend1 = Friend("Саша",   "Виктора", "01.10.2002", "программирования", True, "Программистом")
Friend2 = Friend("Андрей",  "Алинура", "21.07.1997", "валейбол", True, "Сантехником")
Friend1.introduce()
Friend2.introduce()



print("\nДоп задание 1:")
poeple = [Person("Алинур", '12.05.2000', occupation = "Медик", higher_education = True),
Classmate("Бектур", "ИСТ 1-22", "Путина", "05.12.2005",  "Студент", False),
Friend("Андрей",  "Алинура", "21.07.1997", "валейбол", True, "Сантехником")]
for person in poeple:
    person.introduce()
    print("#-----------#")


print("\nДоп задание 2:")
best = BestFriend("Эртай", "Алмаз", "10.09.2000",
"играть на гитаре", True, "Разработчиком","Познакомились на хакатоне")
best.introduce()



