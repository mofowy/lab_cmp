def get_shape_input():
    shape_type = input("Enter the shape (cube/sphere): ").strip().lower()
    size = int(input("Enter the size of the shape: "))
    return shape_type, size