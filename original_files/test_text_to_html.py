import unittest

from text_to_html import TextFileToHtmlConverter


class TestFileToHtmlConverterTest(unittest.TestCase):
    x = TextFileToHtmlConverter("text_to_html.py")
    print(x.convert_to_html())


if __name__ == "__main__":
    unittest.main()
