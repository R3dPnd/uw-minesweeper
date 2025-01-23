from src.models.mine_field import MineField
from src.services.file_service import read_file

'''
    Description: This function creates mine fields from a given file path.
    Parameters:
        file_path: A string representing the file path.
    Returns:
        A list of mine fields.
'''
def create_mine_fields(file_path):
    fields = read_file(file_path).strip().split('\n')
    index = 0
    field_number = 1
    output_fields = []
    while index < len(fields):
        n, m = map(int, fields[index].split())
        if n == 0 and m == 0:
            break
        index += 1
        field = []
        for _ in range(n):
            field.append(fields[index])
            index += 1
        field = generate_minesweeper(n, m, field)
        mine_field = create_mine_field(f"Field #{field_number}:", field)
        output_fields.append(mine_field)
        field_number += 1

    return output_fields

'''
    Description: This function creates a mine field from a given title and field.
    Parameters:
        title: A string representing the title of the mine field.
        field: A string representing the field of the mine field.
    Returns:
        A mine field.
'''
def create_mine_field(title, field):
    mine_field = []
    rows = field.split('\n')
    for row in rows:
        elements = row.split(',')
        mine_field.append(elements)
    return MineField(title,mine_field)

'''
    Description: This function generates a minesweeper field from a given field.
    Parameters:
        n: An integer representing the number of rows.
        m: An integer representing the number of columns.
        field: A 2D array of strings representing the field.
    Returns:
        A string representing the minesweeper field.
'''
def generate_minesweeper(n, m, field):
    result = ""
    for i in range(n):
        row = ''
        for j in range(m):
            if field[i][j] == '*':
                row += '*'
            else:
                row += str(count_mines(n, m, i, j, field))
        result += row + '\n'
    return result

'''
    Description: This function counts the number of mines around a given cell.
    Parameters:
        n: An integer representing the number of rows.
        m: An integer representing the number of columns.
        x: An integer representing the row index.
        y: An integer representing the column index.
        field: A 2D array of strings representing the field.
    Returns:
        An integer representing the number of mines around the cell.
'''
def count_mines(n, m, x, y, field):
    count = 0
    for i in range(max(0, x - 1), min(n, x + 2)):
        for j in range(max(0, y - 1), min(m, y + 2)):
            if field[i][j] == '*':
                count += 1
    return count