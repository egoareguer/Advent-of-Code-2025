from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / '../input.txt'

def isValid(input):
    s=str(input) # We have to process it as a string
    first_half=s[0:len(s)//2]
    second_half=s[len(s)//2:]
    return(not first_half==second_half)

with open(file_path, 'r') as input_file:
    raw_input=input_file.readline().strip()

string_ranges=raw_input.split(',') 
ranges=[]

for pair in string_ranges:
    start, end = pair.split('-')
    ranges.append((int(start),int(end))) # ranges is now a list of int tuples [(a,b), (c,d) ...] 


invalids=[]

def check_range(input, invalids):
    start,end=input
    for i in range(start, end+1):
        if not isValid(i):
            invalids.append(i)
    return (invalids)

for tuples in ranges:
    check_range(tuples, invalids)

answer_sum=0
for invalid_ID in invalids:
    answer_sum += invalid_ID

print(answer_sum)