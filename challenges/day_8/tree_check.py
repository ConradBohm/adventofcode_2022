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

# def get_visible_trees(data):
#     count = 0
#     max_j = len(data) - 1
#     max_i = len(data[0]) -1 # can use first row as all rows are the same length
#     for j in data:          # i is columns, j is rows
#         for i in j:
#             tree_height = data[j][i]
#             trees_up = []
#             trees_down = []
#             trees_left = []
#             trees_right = []

#             for x in range(j,0,-1):
#                 trees_up.append(data[x][i])
#             for x in range(j,max_j,1):
#                 trees_down.append(data[x][i])
#             for x in range(i,0,-1):
#                 trees_left.append(data[j][x])
#             for x in range(i,max_i,1):
#                 trees_right.append(data[j][x])

#             tree_collection = [trees_up,trees_down,trees_left,trees_right]

#             if is_visible(tree_collection, tree_height):
#                 count += 1

#     return count

# def main():
#     parsed_tree_data = parse_tree_data(tree_data)
#     print(get_visible_trees(parsed_tree_data))

# main()