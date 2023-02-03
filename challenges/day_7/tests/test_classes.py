import classes

single_child_file = '6262 abc.de'
single_child_dir = 'dir foff'
multiple_children = ['dir aaa\n','773 fii.ahe\n','44404 ppw.mbj\n','dir vahr\n']
aaa_data = ['9668 gga.ty\n','160 ppe.q\n']

def test_assign_child_single_child():
    test_node = classes.Node('test')

    test_node.assign_child(single_child_file)
    assert test_node.children[0].name == 'abc.de'
    assert test_node.children[0].value == 6262
    assert test_node.children[0].node_type == 'file'

    test_node.assign_child(single_child_dir)
    assert test_node.children[1].name == 'foff'
    assert test_node.children[1].value == 0
    assert test_node.children[1].node_type == 'directory'

def test_assign_child_multiple_children():
    test_node = classes.Node('test')
    for line in multiple_children:
        test_node.assign_child(line)

    assert test_node.children[0].name == 'aaa'
    assert test_node.children[1].value == 773
    assert test_node.children[2].name == 'ppw.mbj'
    assert test_node.children[3].node_type == 'directory'

def test_calculate_value():
    test_node = classes.Node('test')
    for line in multiple_children:
        test_node.assign_child(line)

    test_node.calculate_value()
    assert test_node.value == (773 + 44404)

def test_total_value():
    classes.value_total = 0
    test_node = classes.Node('test')
    for line in multiple_children:
        test_node.assign_child(line)
    for line in aaa_data:
        test_node.children[0].assign_child(line)

    test_node.calculate_value()
    assert classes.value_total == ((9668 + 160)*2 + 773 + 44404)
    