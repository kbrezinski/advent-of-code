
from anytree import Node, RenderTree


def part1():

    commands = open("7-input.txt", "r").read().splitlines()[1:]

    # anytree init
    root = Node("/")
    parent = root

    for command in commands:

        parsed_cmds = command.split()
        new_command = True if '$' == parsed_cmds[0] else False

        # check for new command
        if new_command:
            if 'cd' == parsed_cmds[1]:
                cmd_arg = parsed_cmds[2]
                if cmd_arg == '..':
                    parent = parent.parent
                elif cmd_arg == '/':
                    parent = root
                else:
                    child = cmd_arg
                    parent = generate_child(child, parent=parent)
                print(f"Currently in {parent}")
            # must be ls command
            else:
                continue

        # either a dir or lst command
        if not new_command:
            child = parsed_cmds[1]
            # check if directory
            if parsed_cmds[0] == 'dir':
                child = generate_child(child, parent)
            # check if size check
            else:
                child = generate_child(child, parent, size=parsed_cmds[0])


def generate_child(child, parent, size=None):
    print(child, parent, size)
    # check if empty
    if parent.children:
        # loop through tuple of children
        for child_tuple in parent.children:
            # check if strings contain name of folder
            if not child_tuple.contains(child):
                return Node(child, parent=parent, size=size)
        return child_tuple
    return parent ## [!]


part1()