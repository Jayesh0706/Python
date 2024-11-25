# marks=[54.67,43,23.544]
# print(marks)
# print(type(marks[0]))
# print(type(marks[1]))

# #strings are immutable in python and list are mutable in string

# str="hello"
# #str[0]="a"   #not supported
# print(str)


# print(marks[0])
# marks[0]=90  #supported , list are mutable
# print(marks)


# #******list Methods*****

# list=[23,4,1,231]
# list.reverse()
# print("Reverse of list" ,list)
# list.append(6.4)   #adds element is last
# list.sort()   #sorts list in assending order(small -> large) (together works with int and float)
# print(list)

# list.sort(reverse=True)   #sorts list in (large -> small) (together works with int and float)
# print("reversed sort i.e. sort according to value:",list)


# lstr=["mango","banana","apple"]   #according to alphabetical
# lstr.sort()
# print(lstr)

# lstr.insert(1,"Orange")  #adds elemet at particular index
# print(lstr)

# lnew=[1,2,3,4,5,1,2]
# lnew.remove(1)  #removes first occurence of element
# lnew.pop(1)  #removes element at particular index
# print(lnew)




#******Tuples******
#built-in data type that lets us create immutale sequence of values

tup=(12,2,545,"Jayesh",True)
print(tup)
print(type(tup))
print(tup[0])

#tup[0]="abcd"  #error -->'tuple' object does not support item assignment 
print(tup)


print(tup[3:])


newtup=(1,2,1,2,"Jayesh","Nalawade",2)
print(newtup.index(2))   #first occurence
print(newtup.count(2))      #count of value
