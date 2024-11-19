from lab5.input.user_input import get_shape_input
from lab5.utils.shapes import Cube, Sphere
from lab5.utils.renderer import Renderer
from lab5.utils.manipulator import Manipulator
from lab5.colors.color import Color
from lab5.output.file_handler import save_art_to_file

def main():
    shape_type, size = get_shape_input()
    
    if shape_type == "cube":
        shape = Cube(size)
    elif shape_type == "sphere":
        shape = Sphere(size)
    else:
        print("Invalid shape type!")
        return

    color = Color("white")  # Default color
    shape.set_color(color)

    ascii_art = Renderer.render(shape)
    print(ascii_art)

    Manipulator.scale(shape, 2)
    print("Scaled shape:")
    ascii_art = Renderer.render(shape)
    print(ascii_art)

    save_art_to_file(ascii_art, "lab5/output.txt")
    print("ASCII art saved to output.txt")

if __name__ == "__main__":
    main()