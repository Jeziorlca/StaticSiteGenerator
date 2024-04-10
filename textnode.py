
class TextNode():

    def __init__(self, text: str = None, text_type : str = None, url : str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self) -> str:
        return "TextNode(" + str(self.text) + ", " + str(self.text_type)  + ", " + str(self.url) + ")"

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
