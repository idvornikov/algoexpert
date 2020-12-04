class Boundaries:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self._width and 0 <= y < self._height


class Grid:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._limits = Boundaries(width, height)

    def __contains__(self, coord):
        return coord in self._limits
