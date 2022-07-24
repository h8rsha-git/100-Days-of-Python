from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# user input
menu = Menu()
coffee_machine = CoffeeMaker()
money_manager = MoneyMachine()

state = 'on'

while state == 'on':
  choice = input(f"What would you like? ({menu.get_items()}): ")
  if choice == 'report':
    coffee_machine.report()
    money_manager.report()
  elif choice == 'off':
    print("Thank You...")
    print("Good bye!!")
    state = 'off'
  else:
    item = menu.find_drink(choice)
    cost = menu.find_drink(choice).cost
    if coffee_machine.is_resource_sufficient(item):
      # Transaction
      if money_manager.make_payment(cost):
          coffee_machine.make_coffee(item)
    
  