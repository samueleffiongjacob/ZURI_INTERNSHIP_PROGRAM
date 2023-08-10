# function

print('------------------------------------------------')
print('function starts here')

print('------------------------------------------------')


def new_function():
    print('hallon')


new_function()

print('-------------------------------------')


def new_now(x):
    return x*2


new_now(2)
print(new_now(2))

print('--------------------------------------')


def get_input(user_input):
    user_input = str(input('what is your name: \n'))
    # print(user_input)


get_input('hello')

print('------------------------------------------------')
print('printing name 3 twice')
print('------------------------------------------------')


def your_name():
    name = input('what is your name: \n')
    # print(name)


for i in range(3):
    your_name()

print('------------------------------------------------')


def user_me(age, name, country):
    user = age = int(input('input your age:\n'))
    print('------------------------------------------------')
    user = name = str(input('Enter your name:\n'))
    print('------------------------------------------------')
    user = country = str(input('enter your country: \n '))


user_me(90, 'samuel', 'kenya')
print('------------------------------------------------')


def user_be(country='Nigeria'):
    print(country)


user_be()
print('----------------------------------------------------------------------------')

# Abitary argument are define by  *args


def user_f(*args):
    for i in args:
        print(i)
    print(args)


user_f('hello', 0)

print('-------------------------------------------------------------------------')


# Keywords aguerments **Kwargs
def user_inf(**kwargs):
    for i in kwargs:
        print(i)
    print(kwargs)


user_inf(h='hello', m='me')

# number testing


def greater(first_num, sec_num):
    if first_num > sec_num:
        return True
    else:
        return False


print(greater(6, 8))


# # class object

# class vechicle():
#     def __init__(self, name, size):
#         self.name = 'name'
#         self.size = 'size'

#     def speaker(self):
#         pass
#     print('my name is name ''and l am by size')


# vechicle('truck')
