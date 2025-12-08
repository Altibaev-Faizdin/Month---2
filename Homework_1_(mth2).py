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






