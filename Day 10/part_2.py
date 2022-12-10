import re
import numpy as np

test_result = None


def main(input_file):
    with open(input_file, "r") as f:
        instructions = [line.strip() for line in f.read().split("\n")]

    X = 1
    X_checks = 0
    cycles = 1

    K_pattern = re.compile(r"-?\d+")

    sprite_width = 3
    screen_x, screen_y = 40, 6
    pixels = ["." for _ in range(screen_x * screen_y)]

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

            # Draw sprite
            sprite_pos = X
            crt_draw = cycles - 1
            crt_draw_x = (cycles - 1) % screen_x
            if sprite_pos in (crt_draw_x - 1, crt_draw_x, crt_draw_x + 1):
                pixels[crt_draw] = "#"
            print(f"{crt_draw} {sprite_pos}")
            cycles += 1

        X += after_cycle

    return render_pixels(pixels, screen_x, screen_y)


def render_pixels(pixels, line_length, line_height):
    screen = ""
    for y in range(line_height):
        screen += (
            " ".join(pixels[(y * line_length) : (y * line_length + line_length)]) + "\n"
        )
    return screen
