import random
'Функция заменя строчных на заглавные буквы'

word = input('input text: ')

def word_glav():
    s_up = word.upper()
    return s_up
print(word_glav())

word2 = input('Text: ')
def word2_glav():
  'Функция на заглавную букву'
  capitalized_word2 = word2.capitalize()
  return capitalized_word2
print(word2_glav())

print('Good bye')
