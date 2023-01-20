from main import *

test_data = open("tests/test_data/test_data.txt", "r")
test_data = test_data.readlines()

def test_main():
    test_rope = Rope()

    for line in test_data:
        single_instruction = line.split()
        test_rope.update_position(single_instruction)

    print(test_rope.tail_tracker)
    output = set(map(tuple,test_rope.tail_tracker))
    assert len(output) == 13

    