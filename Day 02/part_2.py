from functools import reduce


test_result = 12


def main(input_file):
    with open(input_file, "r") as f:
        pairs = [line.strip().split(" ") for line in f]

    play_values = {"X": 0, "Y": 1, "Z": 2, "A": 0, "B": 1, "C": 2}

    outcomes = [0, 3, 6]

    ply_results = map(
        lambda pair: outcomes[play_values[pair[1]]]
        + ((play_values[pair[0]] + play_values[pair[1]] - 1) % 3 + 1),
        pairs,
    )

    return sum(ply_results)
