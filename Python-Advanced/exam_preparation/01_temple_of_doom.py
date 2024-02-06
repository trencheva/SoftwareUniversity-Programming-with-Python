from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()

    searched_el = tool * substance

    if searched_el in challenges:
        challenges.remove(searched_el)
    else:
        tools.append(tool + 1)
        if substance > 1:
            substances.append(substance - 1)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(el) for el in challenges)}")

