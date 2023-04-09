import classes

test_crt = classes.CRT()
test_cpu = classes.CPU()

def test_increment_cycle():
    test_crt.increment_cycle() 
    test_crt.increment_cycle()

    assert test_crt.cycle == 2

def test_update_position():
    for x in range(0,45):
        test_crt.update_position()

    assert test_crt.row == 1
    assert test_crt.position == 5
