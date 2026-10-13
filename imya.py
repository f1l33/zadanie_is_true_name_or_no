import pymorphy3
phrase = input()
morph = pymorphy3.MorphAnalyzer()
def name(text):
    words = text.strip().split()
    if len(words) < 1 or len(words) > 2:
        return True
    for word in words:
        first_parse = morph.parse(word)[0]
        tags = first_parse.tag
        is_name = 'Name' in tags
        is_surname = 'Surn' in tags
        if not (is_name or is_surname):
            return False
    return True
if name(phrase) == 1:
    print("Фраза является именем/именем и фамилией")
else:
    print("Фраза не является именем/именем и фамилией")