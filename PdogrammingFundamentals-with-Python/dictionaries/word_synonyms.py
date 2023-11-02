n = int(input())
synonym_dict = {}
for i in range(n):
    word = input()
    synonym = input()

    if word in synonym_dict:
        synonym_dict[word].append(synonym)
    else:
        synonym_dict[word] = [synonym]

for k, v in synonym_dict.items():
    values = ', '.join(v)

    print(f"{k} - {values}")

