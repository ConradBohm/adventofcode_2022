instructions = open("input.txt", "r")
instruction_list = instructions.read().split("\n")
instructions.close()

stack_arrangement = reversed(instruction_list[:9]) # from bottom to top of stacks
instruction_list = instruction_list[10:] # take off the stack arrangement

class Stack:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

    def move_items(self, recipient_stack, amount):
        for i in range(1, amount + 1):
            box = self.stack.pop()
            recipient_stack.add_on(box)      

    def add_on(self, box):
        self.stack.append(box)

    def add_on_grouped(self, box):
        self.stack.extend(box)

    def top_item(self):
        return str(self.stack[-1])

    def move_items_grouped(self, recipient_stack, amount):
        boxes = []
        for i in range(1, amount + 1):
            boxes.append(self.stack.pop())

        boxes = reversed(boxes)
        recipient_stack.add_on_grouped(boxes)

def parse_instructions(instruction_list):
    final_instructions_list = []

    for row in instruction_list:
        final_instructions_row = {}
        split_row = row.split(' ')
        final_instructions_row["amount"] = int(split_row[1])
        final_instructions_row["source"] = split_row[3]
        final_instructions_row["destination"] = split_row[5]

        final_instructions_list.append(final_instructions_row)

    return final_instructions_list

def create_stack_from_input(): 
    stack_collection = []
    stack_list_1 = []
    stack_list_2 = []
    stack_list_3 = []
    stack_list_4 = []
    stack_list_5 = []
    stack_list_6 = []
    stack_list_7 = []
    stack_list_8 = []
    stack_list_9 = []

    for row in stack_arrangement:
        stack_list_1.append(row[1])
        stack_list_2.append(row[5])
        stack_list_3.append(row[9])
        stack_list_4.append(row[13])
        stack_list_5.append(row[17])
        stack_list_6.append(row[21])
        stack_list_7.append(row[25])
        stack_list_8.append(row[29])
        stack_list_9.append(row[33])

    stack_list = [
        [i for i in stack_list_1 if i != ' '],
        [i for i in stack_list_2 if i != ' '],
        [i for i in stack_list_3 if i != ' '],
        [i for i in stack_list_4 if i != ' '],
        [i for i in stack_list_5 if i != ' '],
        [i for i in stack_list_6 if i != ' '],
        [i for i in stack_list_7 if i != ' '],
        [i for i in stack_list_8 if i != ' '],
        [i for i in stack_list_9 if i != ' ']
    ]

    for list in stack_list:
        name = list[0]
        list.pop(0)

        stack = Stack(f"{name}", list)
        stack_collection.append(stack)    

    return stack_collection

def perform_action_part_1(stack_list, instruction):
    for item in stack_list:
        if item.name == instruction["destination"]:
            destination = item
    for item in stack_list:
        if item.name == instruction['source']:
            item.move_items(destination,instruction["amount"])

def perform_action_part_2(stack_list, instruction):
    for item in stack_list:
        if item.name == instruction["destination"]:
            destination = item
    for item in stack_list:
        if item.name == instruction['source']:
            item.move_items_grouped(destination,instruction["amount"])

def main():
    output = ''
    list_of_stacks = []
    instructions_data = parse_instructions(instruction_list)

    list_of_stacks = create_stack_from_input()

    # part 1
    # for instruct in instructions_data:
    #     perform_action_part_1(list_of_stacks, instruct) 

    # part 2
    for instruct in instructions_data:
        perform_action_part_2(list_of_stacks, instruct)

    for stack in list_of_stacks:
        output += stack.top_item()

    print(output)
    for stack in list_of_stacks:
        print(stack.stack)

if __name__=="__main__":
    main()