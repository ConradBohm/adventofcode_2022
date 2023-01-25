from main import *

test_data = open("tests/test_data/test_data.txt", "r")
test_data = test_data.readlines()

larger_test_data = open("tests/test_data/larger_test_data.txt", "r")
larger_test_data = larger_test_data.readlines()

def test_second_position_in_rope():
    test_rope = Rope()
    setup_rope(test_rope)

    for line in test_data:
        single_instruction = line.split()
        test_rope.update_location(single_instruction)

    location_list = test_rope.nodes[1].location_tracker
    output = set(map(tuple,location_list))
    assert len(output) == 13

def test_rope_tail_with_larger_data():
    test_rope = Rope()
    setup_rope(test_rope)

    for line in larger_test_data:
        single_instruction = line.split()
        test_rope.update_location(single_instruction)

    location_list = test_rope.nodes[-1].location_tracker
    print('============\n',location_list,f'\nlength - {len(location_list)}')
    output = set(map(tuple,location_list))
    assert len(output) == 36

    