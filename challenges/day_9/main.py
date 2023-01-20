from classes import Rope

instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

rope = Rope()

def main():
    for line in instruction_data:
        single_instruction = line.split()
        rope.update_position(single_instruction)

    output = set(map(tuple,rope.tail_tracker))
    print(len(output))

main()