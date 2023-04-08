instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

class CPU:
    def __init__(self) -> None:
        self.cycle = 0
        self.register_x = 1
        self.current_instruction = []
        self.instruction_timer = 0
        self.mode = None


    def load_instruction(self, instruction) -> None:
        new_instruction = instruction.split()
        self.current_instruction = new_instruction

    def get_signal_strength(self) -> int:
        return self.cycle * self.register_x
    
    def update_register(self) -> None:
        if self.current_instruction[0][:3] == 'add':
            if self.current_instruction[0][3] == 'x':
                self.register_x += int(self.current_instruction[1])

        else:
            print(f"Error:- inappropriate instruction - {self.current_instruction[0]}")

    def increment_cycle(self) -> None:
        self.cycle += 1

    def update_mode(self):
        if self.mode == 'addx':
            self.mode = None
        else:
            self.mode = self.current_instruction[0]

    def produce_output(self):
        print(f"Signal strength from register X for cycle {self.cycle} is {self.get_signal_strength()}")
        return int(self.get_signal_strength())


cpu = CPU()

def get_latest_instruction(instruction_list):
    output = instruction_list[0]
    instruction_list.pop(0)
    return output

def main(instruction_data):
    total_signal_strength_output = 0
    
    while True:
        cpu.increment_cycle()

        if cpu.cycle in [20,60,100,140,180,220]:
            total_signal_strength_output += cpu.produce_output()
            print(f"total - {total_signal_strength_output}")

        if not cpu.mode or cpu.mode == 'noop':
            instruction = get_latest_instruction(instruction_data)
            cpu.load_instruction(instruction)
            cpu.update_mode()

        elif cpu.mode == 'addx':
            cpu.update_register()
            cpu.update_mode()

        if cpu.cycle > 220:
            print(f"Total signal strength from the above breakpoints is {total_signal_strength_output}")
            return total_signal_strength_output

if __name__ == "__main__":
    main(instruction_data)


