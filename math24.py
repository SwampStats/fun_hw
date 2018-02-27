import itertools

a = input("Please enter first number ")
b = input("Please enter second number ")
c = input("Please enter third number ")
d = input("Please enter fourth number ")
symbols = ('*', '+', '/', '-')
symCombs = (list(itertools.combinations_with_replacement((symbols),3)))
numPerms = (list(itertools.permutations([a,b,c,d])))

# print(numPerms)
# print(symCombs)
for num in numPerms:
    for sym in symCombs:
        result = eval(str(num[0]) + sym[0] + str(num[1]) + sym[1] + str(num[2])
                      + sym[2] + str(num[3]))
        if result == 24: print((str(num[0]) + sym[0] + str(num[1]) + sym[1] + str(num[2])
                      + sym[2] + str(num[3]) + ' = ' + str(result)))
