def decorator1(function):
    def wrapper():
        print('привет')
        function()
        print ('Конец функции')
    return wrapper
def decorator2():
    print(3)
decorator2 = decorator1(decorator2)
decorator2()