from classes import Rope

instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

rope = Rope()

for line in instruction_data:
    single_instruction = line.split()
    rope.update_position(single_instruction)

print(rope.tail_tracker)
# output = set(rope.tail_tracker)
# print(len(output))