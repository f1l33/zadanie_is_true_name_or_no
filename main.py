import pymorphy3
from random import randint,random
phrase = input()

morph = pymorphy3.MorphAnalyzer()
def name(text):
    words = text.strip().split()
    if len(words) < 1 or len(words) > 2:
        return False
    for word in words:
        first_parse = morph.parse(word)[0]
        tags = first_parse.tag
        is_name = 'Name' in tags
        is_surname = 'Surn' in tags
        if not (is_name or is_surname):
            return False
    return True
import random

def generate_phrase():
    phrases = [ "Сегодня отличный день!", "Ты справишься со всем!", "Всё обязательно получится!", "Впереди много хорошего!", "У тебя всё под контролем!" ]
    return random.choice(phrases)

def voskl(a):
    
    c = randint(1,10)
    s=a + "!"*c
    return s

if name(phrase) == 1:
    print(generate_phrase(),voskl(phrase))
else:
    print("не имя")
