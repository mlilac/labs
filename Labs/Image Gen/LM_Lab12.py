#playing with pgm image gen
class Pattern:
    def __init__(self, data):
        self.data = data

    def make_image(self, filename):
        try:
            width = len(self.data[0])
            height = len(self.data)
            lines = []
            for row in self.data:
                line = " ".join(map(str, row)) + '\n'
                lines.append(line)
            with open(filename, 'w') as f:
                f.write(f"P2 {width} {height} 255\n")
                for line in lines:
                    f.write(line)


        except AssertionError as e:
            print(e)

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

class HourGlass(Pattern):
    def __init__(self):
        pattern = []
        for i in range(51):
            row = []
            for j in range(101):
                if i % 2 == 0 and j % 2 == 0:
                    if i <= j <= 101 - i:
                        row.append(0 + i*2)
                        continue
                row.append(255)
            pattern.append(row)
        pattern.extend(pattern[-2::-1])
        super().__init__(pattern)

class SquareSpiral(Pattern):
    def __init__(self):
        pattern = []
        is_even = lambda x: x % 2 == 0
        for i in range(1, 52):
            row = []
            for j in range(1,52):
                if j < i:
                    if is_even(j):
                        row.append(0)
                    else:
                        row.append(180)
                else:
                    if is_even(i):
                        row.append(0)
                    else:
                        row.append(180)
            row.extend(row[-2::-1])
            pattern.append(row)
        pattern.extend(pattern[-2::-1])
        super().__init__(pattern)

class Number(Pattern):
    def __init__(self, number):
        nums = {
            0: [0,1,2,3,5,6,8,9,11,12,13,14],
            1: [1,4,7,10,13],
            2: [0,1,2,5,6,7,8,9,12,13,14],
            3: [0,1,2,5,6,7,8,11,12,13,14],
            4: [0,3,6,7,8,2,5,11,14],
            5: [0,1,2,3,6,7,8,11,12,13,14],
            6: [0,3,6,9,11,12,13,14,1,2,7,8],
            7: [0,1,2,5,8,11,14],
            8: [0,1,2,3,5,6,7,8,9,11,12,13,14],
            9: [0,1,2,3,5,6,7,8,11,12,13,14]
        }
        self.blocks = nums[number]
        pattern = []

        def valid_coord(x, y):
            coords = {
                0: ((0.0, 40.0), (0.0, 40.0)),
                1: ((40.0, 80.0), (0.0, 40.0)),
                2: ((80.0, 120.0), (0.0, 40.0)),
                3: ((0.0, 40.0), (40.0, 80.0)),
                4: ((40.0, 80.0), (40.0, 80.0)),
                5: ((80.0, 120.0), (40.0, 80.0)),
                6: ((0.0, 40.0), (80.0, 120.0)),
                7: ((40.0, 80.0), (80.0, 120.0)),
                8: ((80.0, 120.0), (80.0, 120.0)),
                9: ((0.0, 40.0), (120.0, 160.0)),
                10: ((40.0, 80.0), (120.0, 160.0)),
                11: ((80.0, 120.0), (120.0, 160.0)),
                12: ((0.0, 40.0), (160.0, 200.0)),
                13: ((40.0, 80.0), (160.0, 200.0)),
                14: ((80.0, 120.0), (160.0, 200.0))
            }
            for b in self.blocks:
                low_x, high_x = coords[b][0]
                low_y, high_y = coords[b][1]
                if low_x <= x <= high_x and low_y <= y <= high_y:
                    return True
            return False

        for y in range(201):
            row = []
            for x in range(121):
                if valid_coord(x,y):
                    row.append(0)
                else:
                    row.append(255)
            pattern.append(row)
        super().__init__(pattern)
