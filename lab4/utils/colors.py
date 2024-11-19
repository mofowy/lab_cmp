def apply_grayscale(art):
    shades = ['@', '#', '*', '+', '-', '.', ' ']
    colored_art = []
    for line in art:
        colored_line = ''.join(f"\033[38;5;{232 + shades.index(ch)}m{ch}" for ch in line)
        colored_art.append(colored_line)
    return colored_art
