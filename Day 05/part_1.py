import re


test_result = "CMZ"


def main(input_file):
    with open(input_file, "r") as f:
        inp = f.read()

    starting_containers, instructions = inp.split("\n\n")

    containers = parse_starting_containers(starting_containers)

    instructions = parse_instructions(instructions)

    for instr in instructions:
        n, fro, to = instr
        containers[to - 1].extend(reversed(containers[fro - 1][-n:]))
        containers[fro - 1] = containers[fro - 1][:-n]

    return "".join([x[-1] if x else "" for x in containers])


def parse_starting_containers(text):
    n_lines = text.count("\n")

    # Second to last character should be the number of containers
    n_containers = int(text[-2])

    text = text.split("\n")
    containers = []

    for container in range(1, n_containers * 4 + 1, 4):
        containers.append([])
        for line in range(n_lines - 1, -1, -1):
            if text[line][container] != " ":
                containers[-1].append(text[line][container])

    return containers


def parse_instructions(instructions):
    instructions_pattern = re.compile(
        r"^.*?(\d+).+?(\d+).+?(\d+)$", flags=re.M)
    instructions = re.findall(instructions_pattern, instructions)
    instructions = tuple(map(lambda instr: tuple(map(
        lambda x: int(x), instr)), instructions))

    return instructions
