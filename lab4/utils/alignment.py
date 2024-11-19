def align_text(art, width, alignment='center'):
    aligned_art = []
    for line in art:
        if alignment == 'center':
            aligned_line = line.center(width)
        elif alignment == 'right':
            aligned_line = line.rjust(width)
        else:
            aligned_line = line.ljust(width)
        aligned_art.append(aligned_line)
    return aligned_art
