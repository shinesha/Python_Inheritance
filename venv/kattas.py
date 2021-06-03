#square each digit
# def square_digits(num):
#     li = []
#     # n = 43365644
#     digits = [int(x) for x in str(num)]
#     for i in digits:
#         li.append(i * i)
#     print(li)
#     s = ''.join(map(str, li))
#     print(s)
#     return int(s)
#
# square_digits(9119)

#count duplicates
# def duplicate_count(text):
#     all = text.lower()
#     MyList = list(all)
#     print(MyList)
#
#     my_dict = {i: MyList.count(i) for i in MyList}
#     print(my_dict)
#     e = len([v for v in my_dict.values() if int(v) > 1])
#     print(e)
#     return e
#
# duplicate_count("Abcdde")

#remove vowels
# def disemvowel(string_):
#     vowels = 'aeiouAEIOU'
#     print(''.join([i for i in string_ if i not in vowels]))
#
# disemvowel("This website is for losers LOL!")

# def namelist(names):
#     namelist = [name['name'] for name in names]
#     if len(namelist) <= 1:
#         return ''.join(namelist)
#     else:
#         lastTwo = ' & '.join(namelist[-2:])
#         #print(lastTwo)
#         first = [n + ',' for n in namelist[:-2]]
#         #print(first)
#         first.append(lastTwo)
#         return ' '.join(first)
#
#
# namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])



# def test1():
#     example_string = '1 2 3 4 5 6 7'
#     mylist = [int(s) for s in example_string.split()]
#
#     A = 6
#
#     newList=[]
#     for i in mylist[:A]:
#       newList.append(i)
#     print(newList)
#     print(mylist)
#
#     print(sum(newList[0::2]))
#     print(sum(mylist[0::2]))
#
# test1()




# def stringx():
#     st = "inspiringte"
#     rst = st[::-1]
#     print(rst)
#     count= sum(1 if c1 == c2 else 0 for c1, c2 in zip(st, rst))
#     print(count)
#
# stringx()

#
# def numbers(mylist, num):
#     count =0
#     for i in mylist:
#         if i<num:
#             count+=1
#     print(count)
#
# numbers(mylist=[1,2,3,4], num=10)

# def listLessThan():
#     n = 2
#     xlist = []
#     ylist = []
#     zlist = []
#     for i in range(1+1):
#         xlist.append(i)
#     for j in range(1+1):
#         ylist.append(j)
#     for k in range(1+1):
#         zlist.append(k)
#
#     a= ([[x, y, z] for x in xlist for y in ylist for z in zlist if x + y + z !=n])
#     print(a)
#
# listLessThan()

# def Print_second_highest_in_list():
#     mylist = [2, 3, 6, 6, 5]
#     newList=[]
#     #mylist.sort()
#     #mylist.reverse()
#     mazVal = max(mylist)
#     for i in mylist:
#         if i <mazVal:
#             newList.append(i)
#     print (max(newList))
#
# Print_second_highest_in_list()



i=0
new_list=[]
while i<len(data_list):
  new_list.append(data_list[i:i+3])
  i+=3







