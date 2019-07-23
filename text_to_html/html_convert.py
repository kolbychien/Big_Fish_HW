import html

# (O) Creating a Converter base class with method "convert" and then
# extending for other output formats (e.x. JSON)
class HTMLConvert:
    def convert(self, data):
        html_out = ""
        for line in data:
            line = line.rstrip()
            html_out += html.escape(line, quote=True)
            html_out += "<br />"

        return html_out