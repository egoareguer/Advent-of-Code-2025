from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / '../input.txt'


dial=50
halts_at_zero=0

def rotate(dial, input):
    direction=input[0]
    steps=int(input[1:]) % 100 # The dial is modulo 100
    if direction == "L":
        end = (dial - steps) 
        if end < 0 : 
            end += 100 # We should never go under -99 due to modulo operation
    elif direction == "R":
        end = (dial + steps) % 100
    return end 

with open(file_path, 'r') as input:
    for line in input: 
        dial=rotate(dial, line)
        if dial == 0:
            halts_at_zero += 1 
input.close() 

print (halts_at_zero)