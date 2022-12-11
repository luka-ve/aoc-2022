import re
import math


test_result = 10605


def main(input_file):
    with open(input_file, "r") as f:
        monkeys: list[Monkey] = [Monkey(monkey) for monkey in f.read().split("\n\n")]

    n_rounds = 20

    for _ in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                target_monkey, item = monkey.process_next_item()
                monkeys[target_monkey].add_item(item)

    inspections = [monkey.n_inspections_performed for monkey in monkeys]
    inspections.sort()
    return math.prod(inspections[-2:])


class Monkey:
    def __init__(self, text_input):
        self.items = [
            int(num)
            for num in re.search(r"Starting items: (.*)$", text_input, flags=re.M)
            .group(1)
            .split(", ")
        ]

        self.operation = re.search(
            r"Operation: new = (.+)$", text_input, flags=re.M
        ).group(1)

        self.division_check = int(
            re.search(r"divisible by (\d+)$", text_input, flags=re.M).group(1)
        )

        target_monkeys = re.search(
            r"If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)",
            text_input,
            flags=re.M,
        )
        self.target_monkeys = {
            True: int(target_monkeys.group(1)),
            False: int(target_monkeys.group(2)),
        }

        self.n_inspections_performed: int = 0

    def add_item(self, item):
        self.items.append(item)

    def process_next_item(self):
        item = self.items.pop(0)
        item = self.inspect(item)
        item = self.get_bored(item)
        next_monkey = self.get_target_monkey(item)
        return (next_monkey, item)

    def inspect(self, item):
        old = item
        new = eval(self.operation)
        self.n_inspections_performed += 1
        return new

    def get_bored(self, item):
        return math.floor(item / 3)

    def get_target_monkey(self, item):
        return self.target_monkeys[item % self.division_check == 0]
