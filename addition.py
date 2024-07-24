def addition():
    while True:
        try:
            num1= int(input("Please enter the first number : "))
            num2 = int(input("Please enter the second number : "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of adding {num1} + {num2} = {num1 + num2}")
            break

def subtraction() :
    while True:
        try:
            num1= int(input("Please enter the first number : "))
            num2 = int(input("Please enter the second number : "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of subtracting {num1} - {num2} = {num1 - num2}")
            break

def division() :
   while True:
        try:
            num1= int(input("Please enter the first number : "))
            num2 = int(input("Please enter the second number : "))
            ans = (num1 / num2)
        except ValueError:
            print("Please enter valid numbers!")
        except ZeroDivisionError:
            print("Can't do that")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of dividing {num1} / {num2} = {ans}")
            break

def multiplication():
    while True:
        try:
            num1= int(input("Please enter the first number : "))
            num2 = int(input("Please enter the second number : "))
            ans = num1 * num2
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of multiplying {num1} * {num2} = {ans}")
            break
