outfile = open("test.txt", "a")
with open("s.txt") as file:
    for line in file:
        fc = line[0]
        if fc != ' ' and not fc.isnumeric():
            print(line)
            outfile.write(line)


outfile.close()
