import pyfiglet

def get_available_fonts():
    """Get a list of available fonts."""
    return pyfiglet.FigletFont.getFonts()

def choose_font():
    """Function to choose a font."""
    fonts = get_available_fonts()
    print("Available fonts: ", fonts)
    font_choice = input("Choose a font: ")
    
    if font_choice not in fonts:
        print("Invalid font choice. Using default 'standard'.")
        font_choice = 'standard'
    
    return font_choice
