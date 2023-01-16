import pandas

nato_dataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for(index, row) in nato_dataFrame.iterrows()}

name = input("Enter your name = ").upper()

Nato_name = [nato_dict[letter] for letter in name]
print(Nato_name)
