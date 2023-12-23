a=[1,2,4,5,6,7,8,9,10,11,14,15,21,17]
print(a)
a.insert(0,a[-1])
del a[-1:]
print(a)