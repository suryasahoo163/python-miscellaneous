lst=['bcdef',
'abcdefg',
'bcde',
'bcdef']
# [lst.remove(lst[i]) for i in range(len(lst)-1,0,-1) if lst.count(lst[i])>1]
lst1=lst[::-1]

[lst1.remove(i) for i in lst1 if lst1.count(i)>1]
print(lst1)