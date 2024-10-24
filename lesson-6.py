
#завадння 1
lst = [1 ,2 ,3 ,'4' ,'5' ,'6']
lst_new = []
list(map(lambda a: lst_new.append(str(a)) if type(a) is int else lst_new.append(int(a)), lst))
print(lst_new)
#завадння 2
def func(a):
    if type(a) is int:
        return str(a)
    else:
        return int(a)
lst_new = list(map(func ,lst))
print(lst_new)
#завадння 3
def func2(*args):
        if len(args) > 10:
            args = args[:10]
            return args
n = func2(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(n)

