from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / '../input.txt'

def find_joltage(bank):
    a,b=0,0
    for i in range(len(bank)-1):
        c,d=int(bank[i]),int(bank[i+1])
        if c>a:
            a=c
            b=d
        if d>b:
            b=d
    return(a*10+b)

def find_joltage_recursive(bank, width_to_save):
    # Bank a string of integers from 1 to 9, width an integer 
    leftmost=0
    leftovers_starting_index=1
    for i in range(len(bank)-width_to_save):
        c=int(bank[i])
        if c>leftmost:
            leftmost=c
            leftovers_starting_index=i+1
    if width_to_save == 0:
        return(str(leftmost))
    else:
        return(str(leftmost)+find_joltage_recursive(bank[leftovers_starting_index:], width_to_save-1))  

joltages=[]
sum=0

with open(file_path, 'r') as input:
    for line in input: 
        line=line.strip()
        joltages.append(find_joltage_recursive(line,11))
        sum += int(joltages[-1])

print(joltages)
print(sum)