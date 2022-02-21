from email.utils import decode_rfc2231


def dec(func):
    def wrapper():
        print('Я - декоратор')
        func()
        print('Я все сделал')
    return wrapper 

@dec
def hello():
    print('Привет!')    

hello()