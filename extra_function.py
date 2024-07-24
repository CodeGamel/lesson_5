cart = []
def buy():
    user_input = input('What do you want to buy?')
    cart.append(user_input)
    print(cart)

def remove():
    user_input = input ('What do you want to remove?')
    if user_input in cart:
        cart.remove(user_input)
        print(cart)
