class Rope:
    def __init__(self):
        self.head_position = [0,0]
        self.tail_position = [0,0]
        self.tail_tracker = [[0,0]]

    # def __str__(self):
    #     return f"tail has been in {len(self.tail_tracker)} positions"

    def update_position(self,instruction):
        """ 
        input should be a 2 element list: 
        - first element a letter in U,D,L,R
        - second element a, integer
        """
        # print(f"---------------\nstarting locations:\nhead - {self.head_position}\ntail - {self.tail_position}\n")
        # print(f'instruction: {instruction}')
        direction = instruction[0]
        number = instruction[1]
        for i in range(int(number)):
            if direction == 'U':
                self.head_position[1] += 1
                self.move_tail(direction)
            elif direction == 'D':
                self.head_position[1] -= 1
                self.move_tail(direction)
            elif direction == 'L':
                self.head_position[0] -= 1
                self.move_tail(direction)
            elif direction == 'R':
                self.head_position[0] += 1
                self.move_tail(direction)
        
    def move_tail(self, direction):
        current_x = self.tail_position[0]
        current_y = self.tail_position[1]

        # print(self.tail_position, self.head_position)
        # print('current posotiton: x',current_x,'y',current_y)

        for j in range(current_y - 1,current_y + 2, 1): 
            for i in range(current_x - 1,current_x + 2, 1):
                if [i,j] == self.head_position:
                    # print('head close to tail')
                    return

        if direction == 'U':
            self.tail_position[0] = self.head_position[0]
            self.tail_position[1] = self.head_position[1] - 1
        elif direction == 'D':
            self.tail_position[0] = self.head_position[0]
            self.tail_position[1] = self.head_position[1] + 1
        elif direction == 'L':
            self.tail_position[0] = self.head_position[0] + 1
            self.tail_position[1] = self.head_position[1] 
        elif direction == 'R':
            self.tail_position[0] = self.head_position[0] - 1
            self.tail_position[1] = self.head_position[1]  

        self.tail_tracker.append(self.tail_position[:])
        # print(f'tail tracker - {self.tail_tracker}')
