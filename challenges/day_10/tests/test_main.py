import main

test_data = open("tests/test_data/test_data.txt", "r")
test_data = test_data.readlines()

total_signal_strength_output = 0

def test_get_latest_instruction():
    test_list = [
        'noop',
        'addx 3',
        'addx -5'
    ]

    init_length = len(test_list)

    output = main.get_latest_instruction(test_list)

    assert output == 'noop'
    assert len(test_list) == (init_length - 1)

def test_main():
    test_output = main.main(test_data)
    assert test_output == 13140