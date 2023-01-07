from tree_check import *
small_test_data = open("tests/test_data/small_test_data.txt", "r")
small_test_data = small_test_data.readlines()

def test_parse_tree_data():
    parsed_data = parse_tree_data(small_test_data)
    expeted_result = [[1,2,3],[4,5,6],[7,8,9]]

    assert parsed_data == expeted_result