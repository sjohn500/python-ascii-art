print("*" * 40)
print("WELCOME TO SERAH BANNER MAKER")
print("#" * 40)

letters = {}

with open("letter.txt", "r") as file:
    content = file.read().strip()

blocks = content.split("\n\n")
blocks = [block.strip("\n") for block in blocks]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(blocks)):
    letters[alphabet[i]] = blocks[i]
 
user = input("Enter word: ").upper()
lines = 7
for row in range(lines):
   for letter in user:
      if letter in letters:
         block_lines = letters[letter].split("\n")
         print(block_lines[row], end="  ")
      else:
         print("    ", end="  ")
   print()
print("*" * 40)
print("THANK YOU FOR USING SERAH'S BANNER MAKER")
print("*" * 40)
