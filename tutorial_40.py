#tutorial 40

class my_class(object):

    def __init__(self, text):
        self.text = text

    def showtext(self):
        for line in self.text:
            print line


piece_of_text_1 = my_class(["That's the first",
                   "object of my first Python class",
                   "which called my_class\n"])

piece_of_text_2 = my_class(["That's the second",
                   "object of my first Python class",
                   "which called my_class\n"])

piece_of_text_1.showtext()
piece_of_text_2.showtext()
