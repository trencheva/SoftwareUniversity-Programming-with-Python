version = [int(version) for version in input().split('.')]

for index in range(len(version)-1, -1, -1):
    if version[index] != 9:
        version[index] += 1
        break
    else:
        version[index] = 0


print('.'.join(str(number_for_version) for number_for_version in version))