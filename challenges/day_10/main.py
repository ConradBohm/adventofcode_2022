instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

def load_instruction(inst_list):
    instruction = inst_list[0]
    inst_list.pop(0)

    return instruction

class CPU:
    def __init__(self) -> None:
        self.cycle = 0
        self.register_x = 1
        self.current_instruction = []
        self.instruction_timer = 0


    def load_instruction(self, instruction) -> None:
        new_instruction = instruction.split()
        self.current_instruction = new_instruction

    def signal_strength(self) -> int:
        return self.cycle * self.register_x
    
    def update_register(self) -> None:
        if self.current_instruction[0][:3] == 'add':
            if self.current_instruction[0][3] == 'x':
                self.register_x += int(self.current_instruction[1])
        else:
            print(f"Error:- inappropriate instruction - {self.current_instruction[0]}")

    def increment_cycle(self) -> None:
        self.cycle += 1

    

skip = False
cycle = 0
register_value = 1
instruction_timer = 0

while True:
    cycle += 1

    if skip == True:
        skip = False
        continue




