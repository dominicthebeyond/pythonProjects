# Make a cool calculator using input and eval

# Ask user 

def calculator():
  print(" Hello! I am a handy dandy calculator. ")
  typeOfOperation = input("""What type of calc do you want to do?
                          
                          1. Addition - a
                          2. Subtraction - s
                          3. Multiplication - m
                          4. Division - d
                          5. Exponent - e
                          6. Remainder - r
                          7. floor division - f
                          8. Exit - exit
                           """)
  calc1 = int(input("Enter the first value you want to calculate: "))
  calc2 = int(input("Enter the second value you want to calculate: "))

  if typeOfOperation == "a":
    print(calc1 + calc2)
  elif typeOfOperation == "s": 
    print(calc1 - calc2)
  elif typeOfOperation == "m":
    print(calc1 * calc2)
  elif typeOfOperation == "d": 
    print(calc1 / calc2)
  elif typeOfOperation == "e":
    print(calc1 ** calc2)
  elif typeOfOperation == "r":
    print(calc1 % calc2)
  elif typeOfOperation == "f":
    print(calc1 // calc2)
  elif typeOfOperation == "exit":
    print("Thanks for calculating! Goodbye. ")
  else:
    print("I need you to enter from the options listed. Please try again ;)")

  return "Thanks for using the calculator!"

calculator()
