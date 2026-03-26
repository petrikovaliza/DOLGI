class UpperCaseFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    
    def write(self, text):
        self.file.write(text.upper())


with UpperCaseFile("test.txt", "w") as f:
    f.write("hello world")
    f.write("python is awesome")