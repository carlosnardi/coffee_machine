from data import MENU
from data import resources
from data import money

def payment():
  quarters = 0.25 
  dimes = 0.10
  nickles = 0.05
  pennies = 0.01
  print('Please insert coins.')
  quarters = float(input("How many quarters: ")) * quarters 
  dimes = float(input("How many dimes: ")) * dimes
  nickles = float(input("How many nickles: ")) * nickles
  pennies = float(input("How many pennies: ")) * pennies
  total_payed = quarters + dimes + nickles + pennies
  return total_payed

def check_product(product):
  for item in MENU[product]['ingredients']:
      if MENU[product]['ingredients'][item] > resources[item]:
          print(f'Not enough {item}')
          return False
  return True

def make_product2(product):
  '''A brief make coffee function'''
  for item in MENU[product]['ingredients']:
    resources[item] -= MENU[product]['ingredients'][item]
  money['value'] += MENU[product]['cost']
  print(f'Enjoy your {product.title()}!')

def make_product(product):
  '''Not using anymore'''
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
  elif menu == 'report':
    for i in resources:
      print(f"{i.title()}: {resources[i]}")
    print(f"Money: {money['value']}")
  elif menu == 'espresso' or menu == 'latte' or menu == 'cappuccino':
    if check_product(menu) == True:
      pay = payment()
      if pay >= MENU[menu]['cost']:
        money_change = pay - MENU[menu]['cost']
        if money_change > 0:
          print(f'Here is your change: {round(money_change,2)}')
        make_product2(menu)
      else:
        print('Not enough money')
    else:
      print('Sorry. Not enough ingredients.')
  else: 
    print('Please choose again')