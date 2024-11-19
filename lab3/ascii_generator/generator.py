import pyfiglet

def generate_ascii_art(text, font='standard', width=80, symbol=None):
    """Функція для генерації ASCII-арту з вирівнюванням і кастомними символами."""
    ascii_art = pyfiglet.figlet_format(text, font=font)
    ascii_art_centered = '\n'.join([line.center(width) for line in ascii_art.split('\n')])
    
    if symbol:
        ascii_art_centered = ascii_art_centered.replace('#', symbol).replace('@', symbol)
    
    return ascii_art_centered
