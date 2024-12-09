from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:dict=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError('parent node needs html tag')
        if not self.children:
            raise ValueError('parent node needs at least one child node')
        string_props = ''
        if self.props:
            string_props = ' ' + super().props_to_html()
        children_nodes = []
        for child in self.children:
            children_nodes.append(child.to_html())
        return f"<{self.tag}{string_props}>{''.join(children_nodes)}</{self.tag}>"