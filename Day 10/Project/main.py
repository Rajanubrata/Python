import art 
print(art.logo)

def Add(a,b):
  return a+b
def Subtract(a,b):
   return a-b
def Multiply(a,b):
  return a*b
def Divide(a,b):
  return a/b

operators = {
  "+": Add,
  "-": Subtract,
  "*": Multiply,
  "/": Divide
}

num1 = int(input("Enter 1st number: "))

for operator in operators:
  print(operator)
  
should_continue = True 
while should_continue:
  operation_symbol = input("Choose an operation : ")

  num2 = int(input("Enter next number: "))
  calculaton_function = operators[operation_symbol]
  answer = calculaton_function(num1, num2)
  print (f"{num1} {operation_symbol} {num2} = {answer}")
  
  if input(f"Do you want to continue with {answer}? (y/n) ").lower() == "y":
    num1=answer
  else:
    should_continue = False
