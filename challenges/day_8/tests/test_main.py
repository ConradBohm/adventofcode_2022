from tree_check import *
small_test_data = open("tests/test_data/small_test_data.txt", "r")
small_test_data = small_test_data.readlines()

large_test_data = open("tests/test_data/large_test_data.txt", "r")
large_test_data = large_test_data.readlines()

def test_parse_tree_data():
    small_parsed_data = parse_tree_data(small_test_data)
    large_parsed_data = parse_tree_data(large_test_data)

    expeted_result_small = [[1,2,3],[4,5,6],[7,8,9]]
    expeted_result_large = [[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]]

    assert small_parsed_data == expeted_result_small
    assert large_parsed_data == expeted_result_large