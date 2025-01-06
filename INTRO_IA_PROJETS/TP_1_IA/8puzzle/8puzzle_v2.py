import importlib
import random
import time



puzzle = importlib.import_module('8puzzle')

def is_solvable(p):
    # Sépare la chaîne en une liste de chiffres
    puzzle_list = p.split()
    
    # Vérifie que la liste contient exactement 9 chiffres
    if len(puzzle_list) != 9:
        return False
    
    # Vérifie que chaque élément est un chiffre
    for digit in puzzle_list:
        if not digit.isdigit():
            return False
    
    inversions = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if int(puzzle_list[i]) > int(puzzle_list[j]) and puzzle_list[i] != '0' and puzzle_list[j] != '0':
                inversions += 1
    
    return (inversions % 2) == 0  # inversions pair


def generate_solvable_puzzle():
    while True:
        r = [str(i) for i in range(9)]
        random.shuffle(r)
        puzzle_str = " ".join(r)
        if is_solvable(puzzle_str):
            return puzzle_str

initial = puzzle.EightPuzzle('5 0 2 6 7 1 8 4 3')
goal = puzzle.EightPuzzle('1 2 3 4 5 6 7 8 0')    
h1 = puzzle.EightPuzzle.tile_switches_remaining
h2 = puzzle.EightPuzzle.manhatten_distance
output = puzzle.EightPuzzle.state_transition

print(initial.a_star(goal, h1, output))
start_time = time.time()
print(initial.a_star(goal, h1, output))
temps_exec = time.time() - start_time
print("Temps execution: ",temps_exec,"s")
