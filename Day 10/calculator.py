from art import logo

def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

# dictionary of operation functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


# input 1
def calculator():
  print(logo)
  
  continue_game = 'y'
  num1 = float(input("What is the first number?: "))

  for operator in operations:
    print(operator)

  while continue_game == 'y':
    operation_symbol = input("Pick an operation: ")
    calculation_function = operations[operation_symbol]
    num2 = float(input("What is the next number?: "))
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_game = input(f"Type 'y' to continue calculating with {answer}, or type 'r' to   start fresh, or type 'n' to exit.\n")
    if(continue_game == 'r'):
      calculator()

calculator()
print("Program Ended.")
