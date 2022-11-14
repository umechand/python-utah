

#Exercise5

class Text:
    def __init__(self,string_text):
        self.string_text = string_text

    def reverse_text(self):
        return self.string_text[::-1]


word = "Hello indla umesh"
text = Text(word)
print(text.reverse_text())
