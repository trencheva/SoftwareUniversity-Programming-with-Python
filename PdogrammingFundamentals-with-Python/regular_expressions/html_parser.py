import re

some_string = input()
pattern = r'<title>(.+)<\/title>.*<body>(.*)<\/body>'
matches = re.findall(pattern, some_string)

for match in matches:
    title = match[0]
    raw_content = match[1]

    tabs = re.findall(r'(<\/*.*?>)', raw_content)
    tabs.append('\\n')

    for tab in tabs:
        if tab in raw_content:
            raw_content = raw_content.replace(tab, '')

print(f"Title: {title}")
print(f"Content: {raw_content}")

