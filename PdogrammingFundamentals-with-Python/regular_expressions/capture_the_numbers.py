import re
line = input()
while line:
     match = re.findall(r'\d+', line)
     if match:
          print(' '.join(match), end=' ')
     line = input()
