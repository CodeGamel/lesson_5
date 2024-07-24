from addition import addition
from addition import subtraction
from addition import division
from addition import multiplication

def main():
   flag = True
   while flag :
        action = input('''
Welcome to the calculator, select an option
                   
+ - addition
- = Subtraction
/ - Division
* - multiplication
quit - Quit
''')
        if action == '+':
            addition()

        elif action == '-':
            subtraction()

        elif action == '/':
            division()   
        ValueError("Unsupported operation")

        if action == '*':
            multiplication()   

        if action == 'quit':
            exit
        break
   else:
      print('invalid choice')

main()




   



