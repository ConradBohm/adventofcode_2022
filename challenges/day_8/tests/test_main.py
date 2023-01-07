from tree_check import *

small_test_data = open("tests/test_data/small_test_data.txt", "r")
small_test_data = small_test_data.readlines()

large_test_data = open("tests/test_data/large_test_data.txt", "r")
large_test_data = large_test_data.readlines()

small_visible_check = [[2],[8],[4],[6]]
large_visible_check_1 = [[5,3],[5,3],[3,2],[5,6]]
large_visible_check_2 = [[0],[5,3,5],[2],[5,1,2]]
large_visible_check_3 = [[6,2,3],[3],[],[3,5,4,9]]

def test_parse_tree_data():
    small_parsed_data = parse_tree_data(small_test_data)
    large_parsed_data = parse_tree_data(large_test_data)

    expeted_result_small = [[1,2,3],[4,5,6],[7,8,9]]
    expeted_result_large = [[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]]

    assert small_parsed_data == expeted_result_small
    assert large_parsed_data == expeted_result_large

def test_is_visible():
    assert is_visible(small_visible_check, 5)
    assert not is_visible(large_visible_check_1, 3)
    assert is_visible(large_visible_check_2, 5)

def test_is_visible_edges():
    top_edge = [[],[5,8],[1],[3]]
    bottom_edge = [[5,2],[],[7],[9]]
    left_edge = [[1],[7],[],[5,6]]
    right_edge = [[3],[9],[5,4],[]]

    top_right_corner = [[],[6,9],[2,1],[]]
    bottom_left_corner = [[4,1],[],[],[8,9]]

    assert is_visible(top_edge,2)
    assert is_visible(bottom_edge,8)
    assert is_visible(left_edge,4)
    assert is_visible(right_edge,6)

    assert is_visible(top_right_corner,3)
    assert is_visible(bottom_left_corner,7)

def test_get_scenic_score():
    assert get_scenic_score(small_visible_check, 5) == 1
    assert get_scenic_score(large_visible_check_1, 4) == 2
    assert get_scenic_score(large_visible_check_2, 3) == 1

def test_get_visible_trees():
    small_parsed_data = parse_tree_data(small_test_data)
    large_parsed_data = parse_tree_data(large_test_data)

    small_data = get_visible_trees(small_parsed_data)
    assert small_data['count'] == 9
    large_data = get_visible_trees(large_parsed_data)
    assert large_data['count'] == 21