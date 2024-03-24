# The List 'menu' contains elements from a cafe menu.
menu = ["Coffee", "Tea", "Cake", "Biscuit", "Coke", "Sprite"]

# The dictionary 'stock' defines the number of units of each element in 'menu'.
stock = {'Coffee': 20,
         'Tea': 15,
         'Cake': 20,
         'Biscuit': 100,
         'Coke': 200,
         'Sprite': 150
        }

# The dictionary 'price' defines the price of elements in 'menu'.
price = {'Coffee': 3.50,
         'Tea': 1.50,
         'Cake': 4.50,
         'Biscuit': 1.50,
         'Coke': 1.20,
         'Sprite':1.15
        }

# Create a variable to store the total value of all elements in 'menu'
total_stock = 0

# Create a variable to iterate through elements in 'menu' using indexing.
index = 0

print("Stock list for imaginary cafe: \n")

""" 
Create a 'for' loop to print the type, units and value of each element in 
'menu', recalling data from the dictionaries 'price' and 'stock' to calculate 
values and store the total value of the stock in a variable ('total_stock').
"""
for i in menu:
    item_value = (stock[menu[index]]) * price[menu[index]] 
    print(f'There is {stock[menu[index]]} units of {menu[index]} worth {item_value} pounds.') 
    total_stock += item_value
    index += 1

# Print the total stock value.
print(f'\nThe total worth of the stock is {total_stock} pounds.')       

