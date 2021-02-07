def rectanglearea(xmin, ymin, xmax, ymax):
    length = ymax - ymin
    breadth = xmax - xmin
    if (length < 0 or breadth < 0):
        print("length/breadth of rectangle cannot be negative, please check passed arguments")
        return -1
    return length * breadth