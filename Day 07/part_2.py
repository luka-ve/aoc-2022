from typing import List
from dataclasses import dataclass


test_result = 24933642


def main(input_file):
    with open(input_file, "r") as f:
        terminal_output = f.read().split("\n")

    current_dir: fil = fil(
        name="/",
        parent=None,
        children=[],
        size=-1,
    )

    files: list[fil] = [current_dir]

    i = 0
    while i < len(terminal_output):
        cmd = terminal_output[i]

        if cmd == "$ cd ..":
            current_dir = current_dir.parent
        elif cmd == "$ cd /":
            current_dir = files[0]
        elif cmd == "$ ls":
            while i < len(terminal_output) - 1 and terminal_output[i + 1][0] != "$":
                size, name = terminal_output[i + 1].split()

                new_file = fil(
                    name=name,
                    parent=current_dir,
                    children=[],
                    size=0 if size == "dir" else int(size),
                )

                files.append(new_file)
                current_dir.children.append(new_file)

                i += 1
        else:
            # Go into specified dir
            next_dir = cmd.split()[-1]
            current_dir = next(x for x in current_dir.children if x.name == next_dir)

        i += 1

    get_dir_size(files[0])

    unused_space = 70000000 - files[0].size
    space_needed = 30000000 - unused_space
    dir_sizes = [
        dir.size for dir in files if len(dir.children) > 0 and dir.size > space_needed
    ]
    smallest_dir_to_delete = min(dir_sizes)
    return smallest_dir_to_delete


@dataclass
class fil:
    name: str
    parent: "fil"
    children: List["fil"]
    size: int


def get_dir_size(dir: fil) -> int:
    if dir.children == []:
        return dir.size

    for child in dir.children:
        if child.children == []:
            dir.size += child.size
        else:
            dir.size += get_dir_size(child)

    return dir.size
