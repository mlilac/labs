class Gradient(Pattern):
    def __init__(self, size):
        pattern = []
        for y in range(size):
            row = []
            for x in range(size):
                value = (x + y) // 2
                row.append(int(value / size * 255))
            pattern.append(row)
        super().__init__(pattern)


class Banner(Pattern):
    def __init__(self):
        data = [[255, 255], [191, 191], [127, 127], [63, 63], [0, 0]]
        super().__init__(data)


class CircleCorner(Pattern):
    def __init__(self, radius):
        data = []
        for y in range(radius):
            row = []
            for x in range(radius):
                if (x**2 + y**2) ** 0.5 <= radius:
                    row.append(255)
                else:
                    row.append(0)
            data.append(row)
        super().__init__(data)