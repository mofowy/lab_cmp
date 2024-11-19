class Renderer:
    @staticmethod
    def render(shape):
        ascii_art = shape.draw()
        if shape.color:
            pass
        return ascii_art