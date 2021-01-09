x = 25
def func():
    global x
    print(f'x is {x}')
    x = 'NEW VALUE'
    print(f'I just changed global x to {x}')
res = func()
print(res)
print(x)



