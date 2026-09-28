austen_opening = ["it", "is", "a", "truth", "universally", "acknowledged", "that", "a",
                   "single", "man", "in", "possession", "of", "a", "good", "fortune",
                   "must", "be", "in", "want", "of", "a", "wife"]

bronte_opening = ["there", "was", "no", "possibility", "of", "taking", "a", "walk",
                   "that", "day", "we", "had", "been", "wandering", "in", "the",
                   "leafless", "shrubbery", "an", "hour", "in", "the", "morning"]

tokens = len(austen_opening)
tokens = len(bronte_opening)
types = len(set(austen_opening))
lens = len(set(bronte_opening))
aust = austen_opening
aust_typ = set(austen_opening)
bront = bronte_opening
bront_typ = set(bronte_opening)
#   print(len(aust_typ)/len(aust))
#   print(len(bront_typ)/len(bront))

austen_word = aust_typ
#   print(austen_word)
bronte_word = bront_typ
#   print(bronte_word)

austen_words = austen_word

#   print(austen_words & bronte_word)
#   print(austen_words | bronte_word)
#   print(austen_words - bronte_word)
#   print(aust.count("a"))
print("a" in aust_typ)