#Mutation
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

def count_substring(string, sub_string):
    count=0
    #for j in range (0, len(sub_string)):
    for i in range (len(string)):
        if string[i:i+(len(sub_string))]==sub_string:
            count +=1
    return count


def string_validator(string):

    for i in s:
        if i.isalnum() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isalpha() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isdigit() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.islower() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isupper() == True:
            print("True")
            break
    else:
        print("False")


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


from itertools import product
def iter():
    A = (map(int, input().split()))
    B = list(map(int, input().split()))
    mylist = []
    mylist = (list(product(A, B)))

    print(*[tuple(map(int, t)) for t in mylist])


from itertools import permutations
A = input()
myList=[]
for i in A:
    if i.isalpha():
        myList.append(i)
B = list(permutations(myList, 2))
C = sorted(B)
for j in C:
    c=''.join(j)
    print(c)
