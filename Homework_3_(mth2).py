from datetime import datetime, date


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y").date()
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        today = date.today()
        bd = self.__birth_date
        years = today.year - bd.year
        if (today.month, today.day) < (bd.month, bd.day):
            years -= 1
        return years

    def introduce(self):
        edu = "Есть высшее образование" if self.higher_education else "Нет высшего образования"
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"{edu}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        edu = "Есть высшее образование" if self.higher_education else "Нет высшего образования"
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group_name}. "
              f"{edu}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "У меня есть высшее образование" if self.higher_education else "У меня нет высшего образования"
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия — {self.occupation}. "
              f"Моё хобби — {self.hobby}. "
              f"{edu}.")


print("\nДочерний класс, подкласс (Classmate):")
classmate1 = Classmate("Бектур", "05.12.2005", "Студент", False, "ИСТ 1-22")
classmate1.introduce()
print("Возраст:", classmate1.age)


print("\nДочерний класс, подкласс (Friend):")
friend1 = Friend("Саша", "01.10.2002", "Программист", True, "программирование")
friend1.introduce()
print("Возраст:", friend1.age)

