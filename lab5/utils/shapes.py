class Shape:
    def __init__(self, size):
        self.size = size
        self.color = None

    def draw(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def set_color(self, color):
        self.color = color


class Cube(Shape):
    def draw(self):
        s = self.size
        cube = [
            f"  ____{'_' * s}",
            f" /___/|{'_' * s}|",
            f"|   |{'|' * s}|",
            f"|___|{'|' * s}/",
            f"    {'|' * s}/"
        ]
        return "\n".join(cube)


class Sphere(Shape):
    def draw(self):
        s = self.size
        sphere = [
            f"  ,{'_' * s},  ",
            f" /{'   ' * s}\\ ",
            f"(  {'O' * s}  )",
            f" \\{'   ' * s}/ ",
            f"  `{'-' * s}`  "
        ]
        return "\n".join(sphere)


class AdvancedShape(Shape):
    def draw(self):
        return "Advanced representation of the shape"