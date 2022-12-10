import numpy as np
import pandas as pd


test_result = 8


def main(input_file):
    with open(input_file, "r") as f:
        x = np.ones((), dtype=np.int8)
        trees = []

        for treeline in f:
            trees.append([int(tree) for tree in treeline.strip()])

        np_trees_2 = np.array(trees, dtype=np.int64).transpose()
        np_trees = np.stack(
            (np_trees_2, np.zeros(np_trees_2.shape, dtype=np.int64)),
            axis=2,
        )

        # print(f"Shape: {np_trees.shape}")

    for x in range(0, np_trees.shape[1]):
        for y in range(0, np_trees.shape[0]):
            current_tree = np_trees[x, y, 0]

            left = (
                np.argwhere(np.flip(np_trees[:x, y, 0] >= current_tree))[0][0] + 1
                if np.argwhere(np.flip(np_trees[:x, y, 0] >= current_tree)).shape
                != (0, 1)
                else np_trees[:x, y, 0].shape[0]
            )
            right = (
                np.argwhere(np_trees[(x + 1) :, y, 0] >= current_tree)[0][0] + 1
                if np.argwhere(np_trees[(x + 1) :, y, 0] >= current_tree).shape
                != (0, 1)
                else np_trees[(x + 1) :, y, 0].shape[0]
            )
            up = (
                np.argwhere(np.flip(np_trees[x, :y, 0] >= current_tree))[0][0] + 1
                if np.argwhere(np.flip(np_trees[x, :y, 0] >= current_tree)).shape
                != (0, 1)
                else np_trees[x, :y, 0].shape[0]
            )
            down = (
                np.argwhere(np_trees[x, (y + 1) :, 0] >= current_tree)[0][0] + 1
                if np.argwhere(np_trees[x, (y + 1) :, 0] >= current_tree).shape
                != (0, 1)
                else np_trees[x, (y + 1) :, 0].shape[0]
            )

            tree_score = np.prod((up, down, left, right))

            np_trees[x, y, 1] = tree_score

    print((up, down, left, right))
    print(np_trees[:, :, 1])
    return np.max(np_trees[:, :, 1])
