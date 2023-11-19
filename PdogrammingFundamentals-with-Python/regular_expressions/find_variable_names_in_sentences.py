import re

sentence = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
variable_names = re.findall(pattern, sentence)
print(','.join(variable_names))
