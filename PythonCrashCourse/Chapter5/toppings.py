# Revised 'if' statement conditions.
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'pepperoni', 'extra cheese', 'french fries']

# if  'mushrooms' in requested_toppings:
#     print('Adding mushrooms.')

# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni.')

# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese.')

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print('Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?') 
