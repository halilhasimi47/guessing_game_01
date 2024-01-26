#-------------------------------------
def new_game():

    #guesses = []
    #correct_guesses = 0
    question_num = 1

    for key in questions:
      print("-------------------------")
      print(key)
      for i in options[question_num-1]:
        print(i)

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
new_game()

