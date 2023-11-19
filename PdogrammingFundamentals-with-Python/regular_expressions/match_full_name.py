import re
names = input()

regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

full_names = re.findall(regex, names)

print(' '.join(full_names))