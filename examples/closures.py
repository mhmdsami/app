def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

say_hi = outer_function('Hi')
say_hi()
