name = input("What is your name? ")
print("Hello " + name)

def new_game():

  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print('---------------------------------------')
    print(key)

    for i in options[question_num-1]:
      print(i)

    guess = input(' Choice (A, B, C, D) ')
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key),guess)
    question_num += 1 

  display_score(correct_guesses, guesses)

#-----------------------------------------
def check_answer(answer, guess):

  if answer == guess:
    print('CORRECT')
    return 1 
  else:
    print('WRONG')
    return 0

#-----------------------------------------
def display_score(correct_guesses, guesses):
  print("----------------------------------------")
  print('RESULTS')
  print("----------------------------------------")


  print("Answers: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  print("Guesses: ", end="")
  for i in guesses:
    print(i, end=" ")
  print()

  score = int((correct_guesses/len(questions))*100)
  print("Your score is: "+str(score)+"%")


#-----------------------------------------
def play_again():

    response = input('Do you want to play again? (yes or no): ')
    response = response.upper()

    if response == 'YES':
      return True
    else:
      return False

#-----------------------------------------
questions = {
  "what is the capital of France? ": 'A', 
  'what is the capital of Germany?': 'B',
  'what is the capital of England?':'A',
  'what is the capital of Italy' :'C',
  'what is the capital of Spain?':'D',
  'what is the value of 9*8  ? ' : 'A'}

options = [['A. paris', 'B. berlin', 'C. London','D. Rome'],
           ['A. Madrid', 'B. Berlin','C. Washington DC','D. Ankara'],
           ['A. London','B. Berlin','C. Paris','D. Rome'],
           ['A. Pekin','B. Viana','C. Rome','D. Ankara'],
           ['A. Viana ','B. Berlin','C. Paris','D. Madrid'],
           ['A. 72','B. 80','C. 90','D. 100']]
new_game ()

while play_again():
  new_game()

print('good bye ! ' )


