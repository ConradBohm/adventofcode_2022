value_total = 0
class Node:
    def __init__(self,name):
        self.parent = None
        self.children = []
        self.node_type = None
        self.value = 0
        self.name = name

    def calculate_value(self):
        global value_total
        for node in self.children:
            if node.node_type == 'file':
                print('adding file',node.name,'to dir value')
                self.value += node.value

            if node.node_type == 'directory':
                node.calculate_value()
                self.value += node.value

        print('dir',self.name,'\nvalue',self.value)
        if self.value <= 100000:
            #global value_total
            value_total += self.value
            print('value_total:',value_total)

    def assign_child(self,data_line):
        line = data_line.split()
        x = Node(line[1])
        x.parent = self
        if line[0] == 'dir':       
            x.node_type = 'directory'
        else:
            x.node_type = 'file'
            x.value = int(line[0])

        self.children.append(x)
            