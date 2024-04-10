class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(key+"="+value for key, value in self.props.items())
    
    def __repr__(self):
        return str(self.tag) + " ----- " + str(self.value) + " ----- " + str(self.children) + " ----- " + str(self.props)
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        if value is None:
            raise ValueError("Value cannot be None")
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.props_to_html() == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
