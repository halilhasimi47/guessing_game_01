name = input("What is your name? ")
print("Hello " + name + " :) wellcome to guessing game ")
question = input("are you ready to play game (yes/no) ")
if question.upper() == 'YES':
  print("ok lets start " + name)
elif question == "no" or question == "No" or question == "NO" or question == "nO":
  print(name + " why you are not ready to play game :(" ) 
question1 = input("what is the capital of France? ")
if question1 == "Paris" or question1 == "paris" :
  print("correct you got one point")
else:
  print("incorrect")
question2 = input("what is the capital of Germany?")
if question2 == "Berlin"or question2 == "berlin":
  print("correct you got one point")
else:
  print("incorect")
question3 = input("what is the capital of England?")
if question3 == "London" or question3 == "london":
  print("correct you got one point")
else:
  print("incorrect")
