from classes import *
from main import setup_rope

up = ['U',1]
down = ['D',2]
left = ['L',3]
right = ['R',4]

def test_update_position_rope_class():
    test_rope = Rope()
    setup_rope(test_rope)

    test_rope.update_position(up)
    assert test_rope.nodes[0].position == [0,1]

    test_rope.update_position(down)
    assert test_rope.nodes[0].position == [0,-1]

    test_rope.update_position(left)
    assert test_rope.nodes[0].position == [-3,-1]

    test_rope.update_position(right)
    assert test_rope.nodes[0].position == [1,-1]


def test_update_position_node_class():
    test_rope = Rope()
    setup_rope(test_rope)

    test_rope.update_position(up) 
    assert test_rope.nodes[1].position == [0,0]

    test_rope.update_position(down)
    assert test_rope.nodes[1].position == [0,0]

    test_rope.update_position(left)
    assert test_rope.nodes[1].position == [-2,-1]

    test_rope.update_position(right)
    assert test_rope.nodes[1].position == [0,-1]

def test_set_parent():
    pass

def test_set_child():
    pass