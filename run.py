import os
import importlib
import timeit
from glob import glob
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "days", nargs="*", type=int, help="Space-separated list of days to run"
    )
    parser.add_argument(
        "-n",
        nargs="?",
        default=1,
        type=int,
        help="Number of repeated runs to average out performance differences between runs",
    )
    parser.add_argument(
        "-f",
        action="store_true",
        help="Forces repeated runs, even for long operations (> 10s)",
    )
    args = parser.parse_args()

    days = args.days

    day_folder_pattern = r"Day [0-9][0-9]"
    folders = glob(pathname=day_folder_pattern)
    folders.sort()

    _folders = []
    if args.days:
        _folders = [folder for folder in folders if folder[-2:] in args.days]
        folder = _folders
        _folders = None

    for day in folders:
        run_day_folder(day, args.n, args.f)


def run_day_folder(folder: str, n: int = 1, force: bool = False):
    runtimes = []
    runtimes_info = ""

    for part in (1, 2):
        for i in range(n):
            start_time = timeit.default_timer()

            part_module = importlib.import_module(f"{folder}.part_{part}")
            result = part_module.main()

            runtime = timeit.default_timer() - start_time

            # Safeguard to not repeat long operations
            if n > 1 and (runtime < 10 or force):
                runtimes.append(runtime)
            else:
                break

        if runtimes:
            runtime = sum(runtimes) / len(runtimes)
            runtimes_info = f" on average according to {n} runs. Total runtime: {sum(runtimes):.4f} s"

        print(f"{folder} Part {part}: {result} : {runtime:.4f} s{runtimes_info}")


if __name__ == "__main__":
    main()
