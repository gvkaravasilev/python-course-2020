raw_input = int(input().strip())
list = []

for i in range(raw_input):
    args = input().strip().split(" ")
    if args[0] == "append":
        list.append(int(args[1]))
    elif args[0] == "insert":
        list.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        list.remove(int(args[1]))
    elif args[0] == "pop":
        list.pop()
    elif args[0] == "sort":
        list.sort()
    elif args[0] == "reverse":
        list.reverse()
    elif args[0] == "print":
        print(list)