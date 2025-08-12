class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        pass

    def props_to_html(self):
        if self.props:
            return "".join(map(lambda prop: ' '+prop[0]+'="'+prop[1]+'"', self.props.items()))
        return ""
        
    def __repr__(self):
        children, props = "None", "None"
        if self.children:
            children = f'[{", ".join(map(lambda child: f"{child}", self.children))}]'
        if props:
            jstr = '", '.join(self.props_to_html()[1:].split('" '))
            props = '{'+ jstr +"}"

        return f"HTMLNode({self.tag}, {self.value}, {children}, {props} )"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None, value=None):

        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a html-tag")
        if not self.children:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!YOYO!!!!!!!!!!")
            print(self.tag, self.value, self.props)
            raise ValueError("All parent nodes must have child-node(s).")
        value = ""
        if self.value:
            value = self.value
        return f'<{self.tag}{self.props_to_html()}>{value}{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>'