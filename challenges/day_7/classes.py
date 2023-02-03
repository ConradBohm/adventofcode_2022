value_total = 0

class Node:
    def __init__(self,name):
        self.parent = None
        self.children = []
        self.node_type = None
        self.value = 0
        self.name = name

    def calculate_value(self):
        for node in self.children:
            if node.node_type == 'file':
                self.value += node.value

            if node.node_type == 'directory':
                node.calculate_value()
                self.value += node.value

        if self.value <= 10000:
            value_total += self.value

    def assign_child(self,data_line):
        line = data_line.split()
        x = Node()
        x.parent = self
        if line[0] == 'dir':       
            x.node_type = 'directory'
            x.name = line[1]
        else:
            x.node_type = 'file'
            x.value = int(line[0])
            x.name = line[1]

        self.children.append(x)
            