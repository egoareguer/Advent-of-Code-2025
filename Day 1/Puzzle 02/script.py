from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / '../input.txt'


dial=50
halts_at_zero=0

def rotate(dial, input):
    direction = input[0]
    clicks = int(input[1:]) 
    rotations = clicks // 100 # The number of full rotations, which necessarily pass 0
    steps = clicks % 100 # The dial is modulo 100
    en_passant = False
    if steps == 0:
        if dial == 0:
            return (dial, rotations-1) # We already count the remaining 0 in the loop
        else:
            return (dial, rotations) # Full rotations only, no landing on 0
    if direction == "L":
        if dial != 0: 
            end = (dial - steps) 
            if end < 0 : 
                end += 100 # We should never start from below -99 due to modulo operation
                en_passant = True
        else: # Meaning we START from 0, thus don't cross it
            end = (dial - steps) 
            end += 100
    elif direction == "R":
        end = (dial + steps) 
        if end > 99 :
            end -= 100 
            if end > 0: # Means we didn't stop at 0, thus crossed it
                en_passant = True
    if en_passant:
        rotations += 1 
    return (end, rotations)

with open(file_path, 'r') as input:
    for line in input: 
        passages=0
        dial, passages=rotate(dial, line)
        halts_at_zero += passages
        if dial == 0:
            halts_at_zero += 1 
input.close() 

print (halts_at_zero)