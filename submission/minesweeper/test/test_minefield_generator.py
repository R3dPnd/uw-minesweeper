import unittest

from src.services.minefield_generation import generate_minefield, generate_test_file


class TestMineFieldGenerator(unittest.TestCase):
    def test_minefield_dimensions_minimum(self):
        """Test minefield generation with minimum dimensions (1x1)"""
        field = generate_minefield(1, 1).split('\n')
        self.assertEqual(field[0], "1 1")
        self.assertEqual(len(field), 2)
        self.assertEqual(len(field[1]), 1)

    def test_minefield_dimensions_maximum(self):
        """Test minefield generation with maximum dimensions (100x100)"""
        field = generate_minefield(100, 100).split('\n')
        self.assertEqual(field[0], "100 100")
        self.assertEqual(len(field), 101)
        self.assertEqual(len(field[1]), 100)

    def test_valid_characters(self):
        """Test that generated field contains only valid characters ('.' and '*')"""
        field = generate_minefield(10, 10).split('\n')[1:]
        valid_chars = {'.', '*'}
        for row in field:
            self.assertTrue(all(char in valid_chars for char in row))

    def test_file_terminator(self):
        """Test that generated file ends with '0 0'"""
        content = generate_test_file(3)
        self.assertTrue(content.endswith('0 0'))

    def test_mine_density(self):
        """Test that mine density is approximately correct"""
        field = generate_minefield(20, 20, mine_density=0.25).split('\n')[1:]
        mines = sum(row.count('*') for row in field)
        total_cells = 20 * 20
        density = mines / total_cells
        self.assertGreater(density, 0.15)  # Allow for random variation
        self.assertLess(density, 0.35)