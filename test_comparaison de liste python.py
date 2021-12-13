x_a = [122.000, 124.954, 126.97564, 126.986, 127,130,131]
x_b = [123.234, 124.965, 125.87, 126.978, 5.2]

y_a = [12.000, 14.754, 16.97564, 16.986, 127,130,131]
y_b = [13.234, 14.765, 15.87, 16.978, 5]

zipped = zip(x_a, x_b)

#print(tuple(zipped))

#print("lista",a)
#print("listb",b)

def longest(list1):
    longest_list = max(len(elem) for elem in list1)
    return longest_list

max_len = longest([x_a,x_b])

"""
index = [i for i in range(max_len)]
print("index",index)  
c = set(a) & set(b) & set(b)
print(c)

"""

#on arrondi les listes des coordonnées x&y

round_to_tenths_xa = [round(num, 1) for num in x_a]

round_to_tenths_xb = [round(num, 1) for num in x_b]


round_to_tenths_ya = [round(num, 1) for num in y_a]

round_to_tenths_yb = [round(num, 1) for num in y_b]

#on cherche les valeurs des coordonnées x puis y ou il elles sont egales

test_x = [i == j for i, j in zip(round_to_tenths_xa, round_to_tenths_xb)]
test_y = [i == j for i, j in zip(round_to_tenths_ya, round_to_tenths_yb)]


print(test_x)
print(test_y)

#test_g = [i == j for i, j in zip(test_x, test_y)]
#print(test_g)

#si on a True des une des listes de test au meme index on renvoie l'index en question

find_true_in_testx=[i for i, x in enumerate(test_x) if x]
find_true_in_testy=[i for i, x in enumerate(test_y) if x]

print(find_true_in_testx)
print(find_true_in_testy)



test_g = [i == j for i, j in zip(find_true_in_testx, find_true_in_testy)]
print(test_g)

list_des_index_true=[]
j=0
for i in test_g:
    if i == True:
        list_des_index_true.append(find_true_in_testx[j])
    j=j+1


print(list_des_index_true)

#on recup l'index des listes des presences True
find_true_in_test_g=[i for i, x in enumerate(test_g) if x]

#print(find_true_in_test_g)

#modif sur la liste b

for i in list_des_index_true: 
    for j in range(10):
        x_b[i+j] = x_b[i-1]
        y_b[i+j] = y_b[i-1]


print(x_b)
print(y_b)