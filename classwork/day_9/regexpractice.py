re = __import__("re")
with open("../../data/gutenberg/alice.txt", encoding="utf-8") as f:
    text = f.read()
matches_aou = re.findall(r"c[aou]t", text)   # finds "cat", "cot", or "cut"
print(len(matches_aou))                      # counts how many were found
print(*matches_aou, sep="\n")                # prints each match on a separate line