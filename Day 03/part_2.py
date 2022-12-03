test_result = None


def main(input_file):
    with open(input_file, "r") as f:
        rucksacks = f.read().split("\n")

    rucksacks = [r for r in rucksacks]

    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i : i + 3])

    priorities = {
        letter: count + 1
        for count, letter in enumerate(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
    }

    common_letters = map(
        lambda r: (set(r[0]).intersection(set(r[1]))).intersection(set(r[2])).pop(),
        groups,
    )

    return sum(map(lambda x: priorities[x], common_letters))
