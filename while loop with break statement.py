while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line) #first this line will print whatever the uses enters 
print('done')   # if user types done then the program will break by printing done
