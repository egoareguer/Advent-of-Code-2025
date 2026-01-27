### Mistakes made

+ Erroneous range use (again), forgetting python's `range` is `(included, excluded)` values. 
+ Mistook a `var2 = var1` call to make a copy, it makes a reference. Fixed with ` = copy.deepcopy(var1)` instead.

### Other notes

Definitely could make something **much** cleaner/less tangled with (x,y) coordinates; also not "clean" (factored) code with borders.
Better approach: Use a common pattern of dx, dy. That is:
+ Change my hardcoded matrix changes (spawned from not coming up with clean 3*3 assignments) to 

```
for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]: # Just use lists, duh
        if dy == 0 and dx == 0: # I needed a center cell check, didn't know how to put it elegantly
            continue # continue -> goto start of loop
        if 0 <= ny < height and 0 <= nx < width:
            if grid[ny][nx] == '@':
                += the count/sum
```