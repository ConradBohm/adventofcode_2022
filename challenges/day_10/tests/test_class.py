import main

test_cpu = main.CPU()

def test_load_instruction():
    instruction_1 = 'noop'
    instruction_2 = 'addx 5'

    test_cpu.load_instruction(instruction_1)
    assert test_cpu.current_instruction == ['noop']

    test_cpu.load_instruction(instruction_2)
    assert test_cpu.current_instruction == ['addx', '5']

def test_increment_cycle():
    test_cpu.increment_cycle() 
    test_cpu.increment_cycle()

    assert test_cpu.cycle == 2

def test_update_register():
    instruction_1 = 'addx 2'
    instruction_2 = 'addx -21'
    test_cpu.register_x = 0

    test_cpu.load_instruction(instruction_1)
    test_cpu.update_register()
    assert test_cpu.register_x == 2

    test_cpu.load_instruction(instruction_2)
    test_cpu.update_register()
    assert test_cpu.register_x == -19

def test_get_signal_strength():
    test_cpu.register_x = 10
    test_cpu.cycle = 5

    assert test_cpu.get_signal_strength() == 50

def test_update_mode():
    test_cpu.mode = 'addx'
    test_cpu.update_mode()
    assert test_cpu.mode == None

    test_cpu.load_instruction('noop')
    test_cpu.update_mode()
    assert test_cpu.mode == 'noop'