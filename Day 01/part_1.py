test_result = 24000


def main():
    current_elf_calories = 0
    max_calories = 0

    with open("Day 01/input.txt", "r") as f:
        for line in f:
            if line.strip() == "":
                max_calories = max(max_calories, current_elf_calories)
                current_elf_calories = 0
            else:
                current_elf_calories += int(line)

    return max_calories


if __name__ == "__main__":
    print(main())
