with open("smiley.txt", "r") as file:
    content = file.read()

print(content)

with open("smiley.txt", "r") as file:
    for line in file:
        print(line)

with open("smiley.txt", "r") as file:
    for line in file:
        print(line.rstrip())


letters = {}
with open("letter.txt", "r") as file:
    content = file.read()

blocks = content.split("\n\n")

alphabet = "ABC"

for i in range(len(blocks)):
    letters[alphabet[i]] = blocks[i]
word = input("Type a word: ").upper()

lines = 5
for row in range(lines):
    for letter in word:
        if letter in letters:
            block_lines = letters[letter].split("\n")
            print(block_lines[row], end=" ")
    else:
        print("     ", end=" ")
print()