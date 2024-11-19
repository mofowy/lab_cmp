def save_art_to_file(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)

def load_art_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()