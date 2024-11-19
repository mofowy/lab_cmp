from lab3.ascii_generator.generator import generate_ascii_art
from lab3.fonts.fonts import choose_font
from lab3.colors.colors import get_color_choice
from lab3.utils.utils import save_ascii_art, preview_ascii_art

def main():
    # User input
    user_input = input("Enter a word or phrase to convert into ASCII art: ")

    # Choose font
    font = choose_font()

    # Choose size (width)
    width = input("Enter desired width (default is 80): ")
    width = int(width) if width.isdigit() else 80

    # Choose character for ASCII art
    symbol_choice = input("Enter a symbol you want to use for ASCII art (default is '#'): ")
    symbol = symbol_choice if symbol_choice else '#'

    # Generate ASCII art
    ascii_art = generate_ascii_art(user_input, font, width, symbol)

    # Choose color
    color = get_color_choice()

    # Preview ASCII art
    preview_ascii_art(color + ascii_art)

    # Save to file
    save_ascii_art(ascii_art)

if __name__ == "__main__":
    main()
