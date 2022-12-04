test_result = 2


def main(input_file):

    pairs = []

    with open(input_file, "r") as f:
        for line in f:
            elves = line.strip().split(",")
            sections = [[int(section) for section in elf.split("-")] for elf in elves]

            pairs.append(sections)

    return sum(
        [
            (p[0][0] >= p[1][0] and p[0][1] <= p[1][1])
            or (p[1][0] >= p[0][0] and p[1][1] <= p[0][1])
            for p in pairs
        ]
    )
