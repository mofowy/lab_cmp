def get_user_text():
    text = input("Введіть слово або фразу для ASCII-арту: ")
    return text

def get_dimensions():
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    return width, height
