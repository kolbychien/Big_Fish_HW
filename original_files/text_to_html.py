import html

class TextFileToHtmlConverter:

    def __init__(self, file):
        self.file = file

    def convert_to_html(self):
        f = open(self.file, "r")
        html_out = ""
        for line in f:
            line = line.rstrip()
            html_out += html.escape(line, quote=True)
            html_out += "<br />"

        return html_out
