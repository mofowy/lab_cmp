import random

def generate_ascii_art(text, characters, width, height):
    art = []
    for _ in range(height):
        line = ''.join(random.choice(characters) for _ in range(width))
        art.append(line)
    return art
