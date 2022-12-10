import re


test_result = 13140


def main(input_file):
    with open(input_file, "r") as f:
        instructions = [line.strip() for line in f.read().split("\n")]

    X = 1
    X_checks = 0
    cycles = 1

    K_pattern = re.compile(r"-?\d+")

    for instr in instructions:
        after_cycle = 0
        if instr == "noop":
            blocked_cycles = 1
        else:
            K = re.search(K_pattern, instr)
            after_cycle = int(K.group())
            blocked_cycles = 2

        for c in range(blocked_cycles):
            # Check every 40th cycles starting at 20
            if cycles == 20 or (cycles - 20) % 40 == 0:
                X_checks += X * cycles

            cycles += 1

        X += after_cycle

    return X_checks
