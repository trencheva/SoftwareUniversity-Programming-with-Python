fruits_list = input().split()
result = [fruit for fruit in fruits_list if len(fruit) % 2 == 0]
print('\n'.join(result))