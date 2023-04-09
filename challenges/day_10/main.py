import classes

instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

cpu = classes.CPU()
crt = classes.CRT()

def update_cycle():
    cpu.increment_cycle()
    crt.increment_cycle()
    crt.update_position()

def get_latest_instruction(instruction_list):
    output = instruction_list[0]
    instruction_list.pop(0)
    return output

def main(instruction_data):
    total_signal_strength_output = 0
    
    while True:
        update_cycle()
        crt.draw_pixel(cpu)

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

        if len(instruction_data) == 0:
            print(f"Total signal strength from the above breakpoints is {total_signal_strength_output}")
            crt.render_screen()
            return total_signal_strength_output

if __name__ == "__main__":
    main(instruction_data)


