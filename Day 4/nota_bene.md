### Mistakes made

+ Erroneous range use (again), forgetting python's `range` is `(included, excluded)` values. 
+ Mistook a `var2 = var1` call to make a copy, it makes a reference. Fixed with ` = copy.deepcopy(var1)` instead.

### Other notes

+ Definitely could make something cleaner/less tangled with (x,y) coordinates; also not "clean" (factored) code with borders.