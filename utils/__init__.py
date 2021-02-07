def euclidean_dist(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return (x * x + y * y) ** (0.5)