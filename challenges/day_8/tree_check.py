tree_data = open("input.txt", "r")
tree_data = tree_data.readlines()

parsed_tree_data = []

def parse_tree_data(tree_data):
    return_data = []
    for line in tree_data:
        tree_data_row = []
        for tree in line:
            if tree == '\n':
                continue
            tree_data_row.append(int(tree))

        return_data.append(tree_data_row)

    return return_data

def is_visible(surrounding_trees, main_tree_height):
    not_visible_directions = 0
    for direction in surrounding_trees:
        if len(direction) == 0:
            return True     # tree on the edge is automatically visible

        for tree in direction:
            if tree >= main_tree_height:
                not_visible_directions += 1
                break
        
    if not_visible_directions == 4:
        return False
    
    return True

def get_scenic_score(surrounding_trees, main_tree_height):
    count_list = []
    for direction in surrounding_trees:
        count = 0
        if len(direction) == 0:
            continue     # tree on the edge cannot see any other treesn in that direction

        for tree in direction:
            count += 1
            if tree >= main_tree_height:
                break                   # exit loop as no other trees are visible behind it
        
        count_list.append(count)

    result = 1
    for x in count_list:
        result *= x

    return result

def get_visible_trees(data):
    count = 0
    scenic_score = 0
    
    max_j = len(data)
    max_i = len(data[0])    # can use first row as all rows are the same length
    
    for j, row in enumerate(data):
        for i, tree in enumerate(row):
            tree_height = tree
            trees_up = []
            trees_down = []
            trees_left = []
            trees_right = []

            for x in range(j-1,-1,-1):
                trees_up.append(data[x][i])
            for x in range(j+1,max_j,1):
                trees_down.append(data[x][i])
            for x in range(i-1,-1,-1):
                trees_left.append(data[j][x])
            for x in range(i+1,max_i,1):
                trees_right.append(data[j][x])

            tree_collection = [trees_up,trees_down,trees_left,trees_right]

            if is_visible(tree_collection, tree_height):
                count += 1

            current_tree_scenic_score = get_scenic_score(tree_collection, tree_height)
            if current_tree_scenic_score > scenic_score:
                scenic_score = current_tree_scenic_score

    return_tree_data = {'count': count,'scenic_score': scenic_score}
    return return_tree_data


def main():
    parsed_tree_data = parse_tree_data(tree_data)
    final_data = get_visible_trees(parsed_tree_data)
    print('number of visible trees:', final_data['count'])
    print('best scenic score:', final_data['scenic_score'])

main()