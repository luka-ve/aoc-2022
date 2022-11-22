import os
from argparse import ArgumentParser
from datetime import date
from pathlib import Path

part_boilerplate = """
def main():
    return None

if __name__ == "__main__":
    main()
"""


def main():
    parser = ArgumentParser()
    parser.add_argument("day", nargs="?", type=int)
    args = parser.parse_args()
    day = args.day

    if not args.day:
        day = date.today().day

    # Create folder and files
    day_path = Path(__file__).parent / f"Day {day:02}"

    os.mkdir(day_path)
    (day_path / "test_input.txt").touch()
    (day_path / "input.txt").touch()

    # Write boilerplate to new files
    if not (day_path / "part_1.py").exists():
        with open(day_path / "part_1.py", "w") as f:
            f.write(part_boilerplate)

    if not (day_path / "part_2.py").exists():
        with open(day_path / "part_2.py", "w") as f:
            f.write(part_boilerplate)


if __name__ == "__main__":
    main()
