from blessed import Terminal
from homework_1 import Person

term = Terminal()

fruit_colors = {
    "🍎 Apple": "red",
    "🍌 Banana": "yellow",
    "🍒 Cherry": "crimson",
    "🍇 Grape": "webpurple",
    "🍊 Orange": "orange2",
    "🥭 Mango": "orange",
    "🍍 Pineapple": "rosybrown2"
}

for fruit, color in fruit_colors.items():
    print(getattr(term, color) + fruit + term.normal)



person1 = Person("Алинур", '12.05.2000', occupation="Медик", higher_education=True)
person2 = Person("Акылай", '03.11.1998', occupation="Программист", higher_education=False)
person3 = Person("Артур", '25.08.2002', occupation="Инжинер", higher_education=True)

print("\nПредставление объектов:")
person1.introduce()
person2.introduce()
person3.introduce()


#ЧТОБЫ ПОЛУЧИТ ОТВЕТ НАДО ПОСТАВИТ ВОТ ЭТОТ КОММАНДУ НА ТЕРМИНАЛ ИЛИ GIT BUSH!!!
#cd C:\Users\admin\PycharmProjects\Month2
#python Month2_homework/colorful_print.py


