class Rope:
    def __init__(self):
        self.nodes = []

    def update_location(self,instruction):
        """ 
        input should be a 2 element list: 
        - first element a letter in U,D,L,R
        - second element a, integer
        """
        
        direction = instruction[0]
        number = instruction[1]

        head = self.nodes[0]
        
        print(f'---------------\nstarting locations:\nhead - {head.location}')
        print(f'instruction: {instruction}')

        for i in range(int(number)):
            print('-------------------')
            head.previous_location = head.location[:]       # without the [:] then the lists are linked and one affects the other
                                                            # this is because the lists are mutable
            if direction == 'U':
                head.location[1] += 1
                print('head -',head.location)
                self.update_nodes()

            elif direction == 'D':
                head.location[1] -= 1
                print('head -',head.location)
                self.update_nodes()

            elif direction == 'L':
                head.location[0] -= 1
                print('head -',head.location)
                self.update_nodes()

            elif direction == 'R':
                head.location[0] += 1
                print('head -',head.location)
                self.update_nodes()

    def update_nodes(self):
        for node in self.nodes:
            if node.position_in_rope == 1:
                pass
            else:
                # print(f"-------\n{node.position_in_rope} - {node.location}")
                node.update_location()
                if True: #node.position_in_rope == 10:
                    print(f"{node.position_in_rope} - {node.location}")

class Node:
    def __init__(self, position_in_rope):
        self.position_in_rope = position_in_rope
        self.location = [0,0]
        self.previous_location = []
        self.location_tracker = [[0,0]]
        self.parent = None
        self.child = None

    def set_parent(self,node_list):
        if self.position_in_rope == 1:
            return
        for node in node_list:
            if node.position_in_rope == self.position_in_rope - 1:
                self.parent = node

    def set_child(self,node_list):
        if self.position_in_rope == len(node_list):
            pass
        for node in node_list:
            if node.position_in_rope == self.position_in_rope + 1:
                self.child = node

    def update_location(self):
        self.previous_location = self.location

        # print('location',self.location)

        current_x = self.location[0]
        current_y = self.location[1]

        for j in range(current_y - 1,current_y + 2): 
            for i in range(current_x - 1,current_x + 2):
                if [i,j] == self.parent.location:
                    # print('head close to tail')
                    return

        if self.parent.location[0] != self.location[0] and self.parent.location[1] != self.location[1]:
            if self.parent.location[0] > self.location[0]:
                self.location[0] += 1
            else:
                self.location[0] -= 1

            if self.parent.location[1] > self.location[1]:
                self.location[1] += 1
            else:
                self.location[1] -= 1

        elif self.parent.location[0] == self.location[0] or self.parent.location[1] == self.location[1]:
            self.location = self.parent.previous_location

        self.location_tracker.append(self.location[:])
            


