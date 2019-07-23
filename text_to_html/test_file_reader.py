import unittest

from file_reader import FileReader

class TestFileReader(unittest.TestCase):
    
    def test_file_does_not_exist(self):
        reader = FileReader()
        self.assertEqual('', reader.read_file("fake_file.txt"))

if __name__ == "__main__":
    unittest.main()
