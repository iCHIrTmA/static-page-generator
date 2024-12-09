class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        # foreach key value pair in dict, convert into "key=value" string and push to array
        props_string = list()
        for key, value in self.props.items():
            string = f"{key}=\"{value}\""
            props_string.append(string)

        return ' '.join(props_string)
    
    def __eq__(self, other):
        return self.tag == other.tag and \
            self.value == other.value and \
            self.children == other.children and \
            self.props == other.props
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value:{self.value}, children: {self.children}, props: {self.props})"
    


