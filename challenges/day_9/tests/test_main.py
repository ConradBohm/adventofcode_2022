from main import *

test_data = open("tests/test_data/test_data.txt", "r")
test_data = test_data.readlines()

def test_second_position():
    test_rope = Rope()

    for line in test_data:
        single_instruction = line.split()
        test_rope.update_position(single_instruction)

    location_list = test_rope.nodes[1].locaction_tracker
    output = set(map(tuple,location_list))
    assert len(output) == 13

    