class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return  "TAG:  " + str(self.tag) + " ----- " + "VALUE:   " + str(self.value) + " ----- " + str(self.children) + " ----- " + str(self.props)
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        if value is None:
            raise ValueError("Value cannot be None")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.props_to_html() == "":
            if self.tag == None:
                return f"{self.value}"
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

#ParrentNode is a node that has children. Ie children list is passed to the parrent node
class ParrentNode(HTMLNode):
    # doesn't take a value argument, and the children argument is not optional
    def __init__(self, tag, children: list = None, props: dict = None):
        if children is None:
            raise ValueError("Children cannot be None")
        if tag is None:
            raise ValueError("Tag cannot be None")
        super().__init__(tag, None, children, props)

    def to_html(self):
        #I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}>" + html + f"</{self.tag}>"