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


joltages=[]
sum=0

with open(file_path, 'r') as input:
    for line in input: 
        line=line.strip()
        joltages.append(find_joltage(line))
        sum += joltages[-1]

print(joltages)
print(sum)