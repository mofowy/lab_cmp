from lab4.input.user_input import get_user_text, get_dimensions
from lab4.art_generation.characters import get_ascii_characters
from lab4.art_generation.generate_art import generate_ascii_art
from lab4.utils.alignment import align_text
from lab4.display.display import display_art
from lab4.display.preview import preview_art
from lab4.utils.save_to_file import save_art_to_file

def main():
    text = get_user_text()
    width, height = get_dimensions()
    characters = get_ascii_characters()
    
    art = generate_ascii_art(text, characters, width, height)
    alignment = input("Виберіть вирівнювання (ліво, центр, право): ")
    aligned_art = align_text(art, width, alignment)

    preview_art(aligned_art)
    save_choice = input("Зберегти у файл? (так/ні): ")
    if save_choice.lower() == 'так':
        save_art_to_file(aligned_art)

if __name__ == "__main__":
    main()
