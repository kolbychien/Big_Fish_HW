import unittest

from text_to_html import TextFileToHtmlConverter
from file_reader import FileReader

class TestFileToHtmlConverterTest(unittest.TestCase):
    
    def test_converts_to_html(self):
        converter = TextFileToHtmlConverter("test_doc.txt")
        self.assertEqual('test<br />', converter.convert_to_html())

if __name__ == "__main__":
    unittest.main()
