

letters = {"T":((1,1,1,1,1), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0)),
           "X":((1,0,0,0,1), (0,1,0,1,0), (0,0,1,0,0), (0,0,1,0,0), (0,0,1,0,0), (0,1,0,1,0), (1,0,0,0,1)),
           "O":((1,1,1,1,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,0,0,0,1), (1,1,1,1,1))}

a = letters['T'][2][1]
b = letters['X'][3][4]

print(a)
print(b)