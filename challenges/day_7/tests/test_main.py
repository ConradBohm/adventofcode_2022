import main
import classes

sample_data = open("tests/test_data/test_data.txt", "r")
sample_data = sample_data.readlines()

def test_full_run_using_sample_data():
    classes.value_total = 0
    test_root = classes.Node('/')
    test_root.node_type = 'directory'

    main.assemble_directory(test_root,sample_data)
    test_root.calculate_value()
    print(classes.value_total)
    assert classes.value_total == 95437