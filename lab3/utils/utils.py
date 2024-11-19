def save_ascii_art(ascii_art):
    """Save ASCII art to a file."""
    save_option = input("Do you want to save the result to a file? (y/n): ").lower()
    if save_option == "y":
        with open("lab3/tests/ascii_art.txt", "w") as f:
            f.write(ascii_art)
        print("ASCII art saved to 'ascii_art.txt'.")

def preview_ascii_art(ascii_art):
    """Preview the ASCII art."""
    preview_option = input("Do you want to see a preview of the ASCII art? (y/n): ").lower()
    if preview_option == "y":
        print(ascii_art)
