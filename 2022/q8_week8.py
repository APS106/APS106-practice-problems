word = (input("Enter a word: ")).lower()
word_count = {}
for character in word:
    word_count[word.count(character)] = character
print("The letter", word_count[max(list(word_count.keys()))], "appears most often:", max(list(word_count.keys())), "times.")

max_count = 0
max_char = None
for character in word:
    count = word.count(character)
    if count >= max_count:
        max_count = count
        max_char = character

print("The letter", max_char, "appears most often:", max_count, "times.")