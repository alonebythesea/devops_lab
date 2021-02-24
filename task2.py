list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))

newlist = [x for x in list1 if x in list2]
newlist = list(dict.fromkeys(newlist))

newlist.sort()

print(' '.join(map(str, newlist)))
