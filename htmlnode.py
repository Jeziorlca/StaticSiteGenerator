class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        raise NotImplementedError
    
    def __repr__(self):
        return str(self.tag) + " ----- " + str(self.value) + " ----- " + str(self.children) + " ----- " + str(self.props)