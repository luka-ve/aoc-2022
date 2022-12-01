test_result = 24000


def main(input_file):
    current_elf_calories = 0
    calories = []

    with open(input_file) as f:
        for line in f:
            if line.strip() == "":
                calories.append(current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

    calories.sort()

    return sum(calories[-3:])
