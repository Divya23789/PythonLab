names = ['Andy', 'Eve', 'Sally']
def splicer(mystring):
    if len(mystring)%2==0:
        return 'Even'
    else:
        return mystring[0]
updated_list = list(map(splicer, names))
print(updated_list)
