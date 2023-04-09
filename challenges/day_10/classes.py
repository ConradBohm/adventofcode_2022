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
    
class CRT:
    def __init__(self):
        self.screen = ['','','','','','']
        self.cycle = 0
        self.position = 0
        self.row = 0

    def increment_cycle(self) -> None:
        self.cycle += 1

    def update_position(self):
        self.position += 1

        if self.position > 40:
            self.position = 1
            self.row += 1

    def draw_pixel(self, cpu):
        if (cpu.register_x + 1) >= self.position >= (cpu.register_x - 1):
            self.screen[self.row] += '#'
        else:
            self.screen[self.row] += '.'

    def render_screen(self):
        for row in self.screen:
            print(f"{row}")