
#  Take all the names in a list
with open("./input/Names/invited_Names.txt") as NameList:
    names = NameList.readlines()

#  Take all the lines and choose the first line of letter
with open("./input/letter/starting_letter.txt") as letter:
    lines = letter.read()
    for name in names:
        name = name.strip()
        new_letter = lines.replace("[name]", name)
        with open(f"./Output/Ready_to_send/Letter_to_{name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
