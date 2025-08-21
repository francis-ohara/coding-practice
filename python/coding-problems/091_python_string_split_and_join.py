def split_and_join(line):
    substrs = line.split()
    newstr = "-".join(substrs)
    return newstr

print(split_and_join("Hello World!"))