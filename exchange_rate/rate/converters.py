class StringUrlСurrency:
    regex = r'get-current-+[a-zA-Z]{3}'
    
    def to_python(self, value):
        return str(value).split("-")[2].upper()
    
    def to_url(self, value):
        return value