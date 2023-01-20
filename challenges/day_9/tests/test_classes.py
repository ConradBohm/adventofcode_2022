from classes import *

up = ['U',1]
down = ['D',2]
left = ['L',3]
right = ['R',4]

def test_update_position():
    test_rope = Rope()

    test_rope.update_position(up)
    assert test_rope.head_position == [0,1]

    test_rope.update_position(down)
    assert test_rope.head_position == [0,-1]

    test_rope.update_position(left)
    assert test_rope.head_position == [-3,-1]

    test_rope.update_position(right)
    assert test_rope.head_position == [1,-1]

def test_move_tail():
    test_rope = Rope()

    test_rope.update_position(up) 
    assert test_rope.tail_position == [0,0]

    test_rope.update_position(down)
    assert test_rope.tail_position == [0,0]

    test_rope.update_position(left)
    assert test_rope.tail_position == [-2,-1]

    test_rope.update_position(right)
    assert test_rope.tail_position == [0,-1]