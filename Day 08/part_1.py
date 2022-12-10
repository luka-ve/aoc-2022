import numpy as np
import pandas as pd


test_result = 21


def main(input_file):
    with open(input_file, "r") as f:
        x = np.ones((), dtype=np.int8)
        trees = []

        for treeline in f:
            trees.append([int(tree) for tree in treeline.strip()])

        np_trees = np.array(trees, dtype=np.int8)

    # Edges are always visible
    n_visible_trees = len(trees) * 2 + len(trees[0]) * 2 - 4

    for y in range(1, np_trees.shape[1] - 1):
        for x in range(1, np_trees.shape[0] - 1):
            current_tree = np_trees[x, y]

            if (
                np.all(np_trees[:x, y] < current_tree)
                or np.all(np_trees[(x + 1) :, y] < current_tree)
                or np.all(np_trees[x, :y] < current_tree)
                or np.all(np_trees[x, (y + 1) :] < current_tree)
            ):
                n_visible_trees += 1

    return n_visible_trees
