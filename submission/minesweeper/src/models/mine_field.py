class MineField:

    '''
    Description: This class represents a mine field. It has a title, width, height and a 2D array of cells.
    '''
    def __init__(self):
        self._width = 0
        self._height = 0
        self._field = [[]]

    '''
    Description: This class represents a mine field. It has a title, width, height and a 2D array of cells.
    Parameters:
        _width: An integer representing the width of the mine field.
        _height: An integer representing the height of the mine field.
        _field: A 2D array of strings representing the cells of the mine field.
    '''
    def __init__(self, width, height, field):
        self._width = width
        self._height = height
        self._field = field

    '''
    Description: This class represents a mine field. It has a title, width, height and a 2D array of cells.
    Parameters:
        _title: A string representing the title of the mine field.
        _field: A 2D array of strings representing the cells of the mine field.
    '''
    def __init__(self, title, field):
        self._title = title
        self._field = field

    '''
    Description: Simple to string method.
    '''
    def __str__(self):
        field_text = ""
        for i in range(len(self._field)):
            for j in range(len(self._field[i])):
                field_text += self._field[i][j]
            field_text += "\n"
        label = self._title if self._title else f"Height: {self._height} Width: {self._height}"
        return f"{label}\n {field_text}"