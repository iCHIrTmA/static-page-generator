from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value:str, props:dict=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError
        if not self.tag:
            return self.value
        string_props = ''
        if self.props:
            string_props = ' ' + super().props_to_html()
        return f"<{self.tag}{string_props}>{self.value}</{self.tag}>"