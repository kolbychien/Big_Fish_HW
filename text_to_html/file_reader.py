
class FileReader:
    def read_file(self, file):
        try:
            data = open(file, "r")
            return data
        except FileNotFoundError:
            print('{} File Not Found'.format(file))
            return ''