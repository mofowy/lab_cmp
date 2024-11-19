from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def get_color_choice():
    """Function to choose a color."""
    color_choice = input("Choose a color (red, green, blue): ").lower()
    
    if color_choice == "red":
        return Fore.RED
    elif color_choice == "green":
        return Fore.GREEN
    elif color_choice == "blue":
        return Fore.BLUE
    else:
        print("Unknown color, using default white.")
        return Fore.WHITE
