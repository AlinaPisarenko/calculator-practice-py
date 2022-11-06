from colorama import Fore, Back, Style

print(Back.GREEN)
print(Fore.BLACK)

what = input('Choose: +/- ')

print(Back.YELLOW)

a = float(input('First num: '))
b = float(input('Second num: '))

print(Back.CYAN)

if what == '+':
    c = a + b
    print('result: ' + str(c))

elif what == '-':
    c = a - b
    print('result: ' + str(c))

else:
    print('Error')

input()
