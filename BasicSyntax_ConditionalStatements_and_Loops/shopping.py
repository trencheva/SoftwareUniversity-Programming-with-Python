budget = int(input())
command = input()
no_budget_left = False
while command != "End":
    price = int(command)
    if price > budget:
        no_budget_left = True
        break
    budget -= price
    command = input()
if no_budget_left:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")