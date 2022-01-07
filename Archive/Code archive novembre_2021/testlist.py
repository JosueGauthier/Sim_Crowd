list = [["matplotli"], ["matplo"]]
print(list)

liste2=[]
for group in list:
    print(", ".join(group))
    liste2.append(", ".join(group))
    
print(liste2)

print( ", ".join( repr(e) for e in liste2 ) )

s = 'abc12321cba'

print(s.replace("'", ''))