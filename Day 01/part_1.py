test_result = 24000


def main(input_file):
    current_elf_calories = 0
    max_calories = 0

    with open(input_file, "r") as f:
        for line in f:
            if line.strip() == "":
                max_calories = max(max_calories, current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

    return max_calories
