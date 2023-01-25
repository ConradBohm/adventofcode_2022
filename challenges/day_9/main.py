from classes import *

instruction_data = open("input.txt", "r")
instruction_data = instruction_data.readlines()

rope = Rope()

def setup_rope(rope):
    for i in range(1,11):
        node = Node(i)
        rope.nodes.append(node)
    for node in rope.nodes:
        node.set_parent(rope.nodes)
        node.set_child(rope.nodes)

def main():
    setup_rope(rope)

    for line in instruction_data:
        single_instruction = line.split()
        rope.update_location(single_instruction)

    output_second_node = set(map(tuple,rope.nodes[1].location_tracker))
    output_tail = set(map(tuple,rope.nodes[-1].location_tracker))
    print(len(output_second_node))
    print(len(output_tail))

main()