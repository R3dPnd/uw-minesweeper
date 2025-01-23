import unittest

from src.services.file_service import read_file
from src.services.mine_sweeper_service import count_mines, generate_minesweeper, create_mine_fields


class TestMineSweeper(unittest.TestCase):
    def test_count_mines_corner(self):
        """Test mine counting in corner position"""
        field = ['*...', '....', '....']
        count = count_mines(3, 4, 0, 1, field)
        self.assertEqual(count, 1)

    def test_count_mines_surrounded(self):
        """Test mine counting with all surrounding mines"""
        field = ['***', '*.*', '***']
        count = count_mines(3, 3, 1, 1, field)
        self.assertEqual(count, 8)

    def test_count_mines_border(self):
        """Test mine counting on field border"""
        field = ['**.', '*..', '...']
        count = count_mines(3, 3, 0, 2, field)
        self.assertEqual(count, 1)  # Only adjacent to one mine

    def test_generate_minesweeper_empty(self):
        """Test minesweeper generation with no mines"""
        field = ['.....', '.....']
        result = generate_minesweeper(2, 5, field)
        self.assertEqual(result.strip(), '00000\n00000')

    def test_generate_minesweeper_all_mines(self):
        """Test minesweeper generation with all mines"""
        field = ['***', '***']
        result = generate_minesweeper(2, 3, field)
        self.assertEqual(result.strip(), '***\n***')

    def test_max_field_size(self):
        """Test maximum field size (100x100)"""
        field = []
        for _ in range(100):
            row = ['.' for _ in range(100)]
            field.append(''.join(row))
        result = generate_minesweeper(100, 100, field)
        rows = result.strip().split('\n')
        self.assertEqual(len(rows), 100)  # Check number of rows
        self.assertEqual(len(rows[0]), 100)  # Check row length

    def test_min_field_size(self):
        """Test minimum field size (1x1)"""
        test_input = "1 1\n*\n0 0"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)
        fields = create_mine_fields('test_input.txt')
        self.assertEqual(len(fields[0]._field[0]), 1)

    def test_multiple_fields(self):
        """Test processing multiple fields"""
        test_input = "2 2\n.*\n*.\n3 3\n...\n.*.\n...\n0 0"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)
        fields = create_mine_fields('test_input.txt')
        self.assertEqual(len(fields), 2)

    def test_field_formatting(self):
        """Test output string formatting"""
        test_input = "3 3\n.*.\n...\n.*.\n0 0"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)
        fields = create_mine_fields('test_input.txt')
        output = fields[0].__str__()
        self.assertTrue('Field #1:' in output)

    def test_rectangular_field(self):
        """Test non-square field"""
        field = ['.*.',
                 '...']
        result = generate_minesweeper(2, 3, field)
        rows = result.strip().split('\n')
        self.assertEqual(len(rows), 2)  # Check number of rows
        self.assertEqual(len(rows[0]), 3)  # Check row length
