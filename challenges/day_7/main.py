import classes

file_logs = open("input.txt", "r")
file_logs = file_logs.readlines()


def assemble_directory(directory,file_logs):
    while True:
        line = file_logs[0]
        if line[0] == '$':
            if 'ls' in line:
                file_logs.pop(0)
                continue
            elif 'cd ..' in line:
                file_logs.pop(0)
                return
            else:
                for node in directory.children:
                    if node.name in line[5:]:
                        new_directory = node
                file_logs.pop(0)
                assemble_directory(new_directory)

        directory.assign_child(line)
        file_logs.pop(0)

def main():
    root = classes.Node('/')
    root.node_type = 'directory'

    assemble_directory(root,file_logs)
    root.calculate_value()

    print(classes.value_total)
    
        
