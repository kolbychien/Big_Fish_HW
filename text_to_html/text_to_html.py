from file_reader import FileReader
from html_convert import HTMLConvert

class TextFileToHtmlConverter:

    def __init__(self, file):
        self.file = file

    def convert_to_html(self):
        # (S) Moved open to file reader class so this class only
        # handles conversion, created HTMLConvert class to handle
        # the conversion
        f = FileReader().read_file(self.file)
        return HTMLConvert().convert(f)

# (Me) Having a Converter base class that this extends with a method
# called convert.  The API has the file to convert being set 
# on the constructor, but it seems nicer in the future 
# to just have it be passed into convert 

