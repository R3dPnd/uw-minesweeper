import unittest
import os

from src.services.file_service import read_file, write_file


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.txt'
        self.test_content = 'test content'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read_file(self):
        """Test writing to and reading from file"""
        from src.services.file_service import write_file
        write_file(self.test_file, self.test_content)
        content = read_file(self.test_file)
        self.assertEqual(content, self.test_content)

    def test_write_empty_file(self):
        """Test writing empty content"""
        write_file(self.test_file, '')
        content = read_file(self.test_file)
        self.assertEqual(content, '')

    def test_write_large_content(self):
        """Test writing large content"""
        large_content = 'x' * 1000000  # 1MB of data
        write_file(self.test_file, large_content)
        content = read_file(self.test_file)
        self.assertEqual(content, large_content)

    def test_write_multiple_lines(self):
        """Test writing content with multiple lines"""
        multi_line = 'line1\nline2\nline3'
        write_file(self.test_file, multi_line)
        content = read_file(self.test_file)
        self.assertEqual(content, multi_line)
