# import os
# from blessed import Terminal
# from homework_1 import Person
#
# os.environ['TERM'] = 'xterm-256color'
# terminal = Terminal(force_styling=True)
#
#
# fruits_colors = {
#     'apple🍎': terminal.red,
#     'banana🍌': terminal.yellow,
#     'cherry🍒': terminal.crimson,
#     'grape🍇': terminal.webpurple,
#     'mango🥭': terminal.orange2,
#     'orange🍊': terminal.orange,
#     'peach🍑': terminal.rosybrown2,
# }
#
# print(terminal.bold_underline('Fruit Color Display'))
# for fruit, color in fruits_colors.items():
#     print(color(fruit))

from blessed import Terminal
from homework_1 import Person

# Фрукты с эмоджи
fruits = ["🍎 Apple", "🍌 Banana", "🍒 Cherry", "🍇 Grape", "🍊 Orange", "🥭 Mango", "🍍 Pineapple"]
colors = ["red", "yellow", "magenta", "blue", "darkorange", "green", "cyan"]

term = Terminal()

for fruit, color in zip(fruits, colors):
    print(getattr(term, color) + fruit + term.normal)

# Примеры Person
person1 = Person("Алинур", '12.05.2000', occupation="Медик", higher_education=True)
person2 = Person("Акылай", '03.11.1998', occupation="Программист", higher_education=False)
person3 = Person("Артур", '25.08.2002', occupation="Инжинер", higher_education=True)

print("\nПредставление объектов:")
person1.introduce()
person2.introduce()
person3.introduce()


