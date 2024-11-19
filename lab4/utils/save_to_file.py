def save_art_to_file(art, filename="lab4/logs/ascii_art.txt"):
    with open(filename, 'w') as f:
        for line in art:
            f.write(line + "\n")
    print(f"ASCII-арт збережено у файл {filename}")
