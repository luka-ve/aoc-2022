test_result = None


def main(input_file):
    with open(input_file, "r") as f:
        rucksacks = f.read().split("\n")

    rucksacks = [[r[: int(len(r) / 2)], r[int(len(r) / 2) :]] for r in rucksacks]

    priorities = {
        letter: count + 1
        for count, letter in enumerate(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )
    }

    common_letters = map(lambda r: (set(r[0]).intersection(set(r[1]))).pop(), rucksacks)
    return sum(map(lambda x: priorities[x], common_letters))
