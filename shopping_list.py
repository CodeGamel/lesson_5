from extra_function import buy
from extra_function import remove
cart = []

def main():
   flag = True
   while flag :
        action = input('''
Welcome to Amazon, select an option
                   
1. Buy
2. Remove
3. Quit
''')
        if action == '1':
            buy()
        elif action == '2':
            remove()
        elif action == '3':
            exit
            break
        else:
            print('invalid option')


main()