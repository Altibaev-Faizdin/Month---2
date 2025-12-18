def printer(func):
    def wrapper(*args, **kwargs):
        print("до вызова")
        func(*args, **kwargs)
        print("после вызова")
    return wrapper


@printer
def hello_world():
    print("hello world")


# hello_world = printer(hello_world)

hello_world()

@printer
def add_numbers(a, b):
    print(a + b)

add_numbers(3, 4)