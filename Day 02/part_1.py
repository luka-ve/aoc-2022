import pandas as pd


test_result = 15

lose_to = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
    'X': 'B',
    'Y': 'C',
    'Z': 'A'
}

player_values = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

outcome_values = {
    'lose': 0,
    'draw': 3,
    'win': 6
}


def main(input_file):
    pairs = pd.read_csv(input_file, sep=" ", header=None, names=["elf", "player"])

    results = pairs.apply(get_ply_result, axis=1)
    
    return results.sum()


def get_ply_result(ply):
    play_points = 0
    
    if lose_to[ply.elf] == ply.player:
        play_points = outcome_values['win']
    elif lose_to[ply.player] == ply.elf:
        play_points = outcome_values['lose']
    else:
        play_points = outcome_values['draw']

    return play_points + player_values[ply.player]