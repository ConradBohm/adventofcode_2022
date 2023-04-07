import classes

file_logs = open("input.txt", "r")
file_logs = file_logs.readlines()


def assemble_directory(directory,file_logs):
    while len(file_logs) > 0:
        line = file_logs[0]

        if '$ cd /' in line:    # line 1 exception
            file_logs.pop(0)
            continue
        
        if '$ ls' in line:
            file_logs.pop(0)
            continue
        elif '$ cd ..' in line:
            file_logs.pop(0)
            break
        elif '$ cd ' in line:
            dir = [node if node.name in line[5:] else '' for node in directory.children]
            new_dir = list(filter(None,dir))
            file_logs.pop(0)
            assemble_directory(new_dir[0],file_logs)
        else:
            #print('making a child with line:',line)
            directory.assign_child(line)
            file_logs.pop(0)

def main():
    root = classes.Node('/')
    root.node_type = 'directory'

    assemble_directory(root,file_logs)
    root.calculate_value()

    space_free = 70000000 - root.value
    space_needed = 30000000 - space_free

    root.find_dir_to_delete(space_needed)

    print(classes.value_total, " - value total of directories < 100000")
    print(classes.dir_to_delete[0].value, " - value of smallest dir to delete")
    
main()
