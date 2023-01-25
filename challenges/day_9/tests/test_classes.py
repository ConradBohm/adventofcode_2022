from classes import *
from main import setup_rope

up = ['U',1]
down = ['D',2]
left = ['L',3]
right = ['R',4]

def test_update_location_rope_class():
    test_rope = Rope()
    setup_rope(test_rope)

    test_rope.update_location(up)
    assert test_rope.nodes[0].location == [0,1]

    test_rope.update_location(down)
    assert test_rope.nodes[0].location == [0,-1]

    test_rope.update_location(left)
    assert test_rope.nodes[0].location == [-3,-1]

    test_rope.update_location(right)
    assert test_rope.nodes[0].location == [1,-1]


def test_update_location_node_class():
    test_rope = Rope()
    setup_rope(test_rope)

    test_rope.update_location(up) 
    assert test_rope.nodes[1].location == [0,0]

    test_rope.update_location(down)
    assert test_rope.nodes[1].location == [0,0]

    test_rope.update_location(left)
    assert test_rope.nodes[1].location == [-2,-1]

    test_rope.update_location(right)
    assert test_rope.nodes[1].location == [0,-1]

def test_set_parent():
    pass

def test_set_child():
    pass