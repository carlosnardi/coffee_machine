from data import MENU
from data import resources
from data import money

def payment():
  quarters = 0.25 
  dimes = 0.10
  nickles = 0.05
  pennies = 0.01
  quarters = float(input("How many quarters: ")) * quarters 
  dimes = float(input("How many dimes: ")) * dimes
  nickles = float(input("How many nickles: ")) * nickles
  pennies = float(input("How many pennies: ")) * pennies
  total_payed = quarters + dimes + nickles + pennies
  return total_payed

def check_product(product):
  if product == 'espresso':
    return resources['water'] >= MENU[product]['ingredients']['water'] and resources['coffee'] >= MENU[product]['ingredients']['coffee']
  else:
    return resources['water'] >= MENU[product]['ingredients']['water'] and resources['coffee'] >= MENU[product]['ingredients']['coffee'] and resources['milk'] >= MENU[product]['ingredients']['milk'] 

def make_product(product):
  # poderia mudar pra um for cada item do MENU
  resources['water'] -= MENU[product]['ingredients']['water'] 
  resources['coffee'] -= MENU[product]['ingredients']['coffee']
  if product != 'espresso':
    resources['milk'] -= MENU[product]['ingredients']['milk']
  money['value'] += MENU[product]['cost']
  print(f'Enjoy your {product.title()}!')

while True:
  menu = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if menu == 'off':
    break
  if menu == 'report':
    for i in resources:
      print(f"{i.title()}: {resources[i]}")
    print(f"Money: {money['value']}")
  else:
    if check_product(menu) == True:
      pay = payment()
      if pay >= MENU[menu]['cost']:
        money_change = pay - MENU[menu]['cost']
        if money_change > 0:
          print(f'Here is your change: {money_change}')
        make_product(menu)
      else:
        print('Not enough money')
    else:
      print('Sorry. Not enough ingredients.')