'''
Input : a list, and a value (the list may contain lists)
Output : a list (containing all the value indexes)
So it's kinda obvious that we will be using recursion, isn't it ?
'''

def find(value, searchlist):
    indexes = []
    for i in range(len(searchlist)):
        if (searchlist[i] == value):
            indexes.append([i])
        elif isinstance(searchlist[i],list):
            for index in find(value,searchlist[i]):
                indexes.append([i] + index)
    return indexes

print(find(1,[1,[2,3,1],[[1,1],[2,3,1]]]))
