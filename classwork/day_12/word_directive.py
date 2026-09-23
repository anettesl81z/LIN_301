word = input("Enter a word: ").strip().lower()

first_letter = word[0]
is_vowel = (word[0] == 'a') or (word[0] == 'e') or (word[0] == 'i') or (word[0] == 'o') or (word[0] == 'u')

print("Vowel?", is_vowel)