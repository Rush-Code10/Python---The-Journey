while True:
    line = input('>>')
    if line[0] == '#':
        continue
    if line == 'done' or line == "DONE":
        break
    print(line)
print("DONE!")

#So in this block of code a person can input anything and the statement
#will be printed only when DONE OR done is entered the code will end