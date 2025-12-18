from blessed import Terminal
from homework_1 import Person

terminal = Terminal()

fructs_colors = {
    'apple': terminal.red,
    'banana': terminal.yellow,
    'cherry': terminal.crimson,
    'grape': terminal.webpurple,
    'mango': terminal.cyan,
    'orange': terminal.magenta,
    'peach': terminal.white,

}

print(terminal.bold_underline('Fruit Color Display'))
for fruit, color in fructs_colors.items():
    print(color(fruit))




person1 = Person("Алинур", '12.05.2000', occupation = "Медик", higher_education = True)
person2 = Person("Акылай",  '03.11.1998', occupation = "Программист", higher_education = False)
person3 = Person("Артур", '25.08.2002', occupation = "Инжинер", higher_education = True)

print("\nПредс-е объектов:")
person1.introduce()
person2.introduce()
person3.introduce()
