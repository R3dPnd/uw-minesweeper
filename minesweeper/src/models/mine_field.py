class MineField:

    def __init__(self):
        self._width = 0
        self._height = 0
        self._field = [[]]

    def __init__(self, width, height, field):
        self._width = width
        self._height = height
        self._field = field

    def __init__(self, title, field):
        self._title = title
        self._field = field

    def __str__(self):
        field_text = ""
        for i in range(len(self._field)):
            for j in range(len(self._field[i])):
                field_text += self._field[i][j]
            field_text += "\n"
        label = self._title if self._title else f"Height: {self._height} Width: {self._height}"
        return f"{label}\n {field_text}"