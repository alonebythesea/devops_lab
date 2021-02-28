num_of_commands = int(input())

result = []

for command in range(num_of_commands):
    command = input().split(' ')
    if 'insert' in command:
        result.insert(int(command[1]), int(command[2]))
    elif 'print' in command:
        print(result)
    elif 'remove' in command:
        result.remove(int(command[1]))
    elif 'append' in command:
        result.append(int(command[1]))
    elif 'sort' in command:
        result.sort()
    elif 'pop' in command:
        result.pop()
        if len(command) > 1:
            result.pop(int(command[1]))
    elif 'reverse' in command:
        result.reverse()
    else:
        break
