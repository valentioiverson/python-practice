if __name__ == '__main__':
    N = int(input())
    commands = list()
    for i in range(N):
        temp = input().strip().split(" ")
        if temp[0] == "insert":
            commands.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == "print":
            print(commands)
        elif temp[0] == "remove":
            commands.remove(int(temp[1]))
        elif temp[0] == "append":
            commands.append(int(temp[1]))
        elif temp[0] == "sort":
            commands.sort()
        elif temp[0] == "pop":
            commands.pop()
        elif temp[0] == "reverse":
            commands.reverse()
