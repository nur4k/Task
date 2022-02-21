def dec(temperature):
    if temperature > 10:
        print('На улице тепло, давай погуляем, я не против!')
    elif temperature > 0 and temperature < 10:
        print('Прохладно. Надо одеться!')
    elif temperature > -10 and temperature < 0:
        print('Холодно. Потеплее оденься и пойдем!')
    elif temperature < -10:
        print('Мороз. Лучше давай дома посидим, фильм посмотрим!')
    def decorator(function):    
        def wrap():
            return function()
        return wrap
    return decorator
            


try:
    temperature = input()
    if temperature is not int:
        @dec(int(temperature))
        def go_for_a_walk():
            print('Давай, пойдем погуляем на улице!')
except:
    pass

go_for_a_walk()







