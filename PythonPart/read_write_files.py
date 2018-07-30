# 'r' is for read-only!
# 'w' is for writing mode. BEWARE! Once you open a file in writing mode,
# anything it contained will be deleted!!!
# If you want to just add to a file, use 'append' instead.
f = open('testFile.txt', 'r')
file_data = f.read()
f.close()

print(file_data)

f = open('nfile.txt', 'w')
f.write('Hello World!')
f.close()



# 'with' allows us to open file, do stuff, and 'with' will automatically close it!
# This is much safer.

with open('testFile.txt', 'r') as f:
    file_data = f.read()

print(file_data)

with open('camelot.txt') as song:
    print(song.read(2))
    print(song.read(9))
    print(song.read())


camelot_lines = []
with open('camelot.txt') as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
