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
