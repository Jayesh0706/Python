# count=1
# while count<=5:
#     print(count,"--> Hello")
#     count +=1


# cnt=10
# while cnt >= 1:
#     print(cnt ,"Reversed")
#     cnt-=1



# #WAP print multiplication table of N
# N=int(input("Enter number: "))
# i=1
# while i<=10:
#     print(f"{N} x {i} = {N*i}")
#     i+=1


# #WAP to print element in list

# l1=[1,2,3,5,6,7,13,35,56]
# ln=int(len(l1)-1)
# i=0
# while i<=ln:
#     print(l1[i])
#     i+=1

# l2=['jayesh',706,"devops",23.4]
# i=0
# while i<=(len(l2)-1):
#     print(l2[i])
#     i+=1




#WAP to search element in tuple

tup=(12,56,45,89,16,82,100,18)

x=int(input("Enter element to search:"))

i=0
ln=len(tup)

while i<ln:
    if(tup[i]==x):
        print("Element found at index -->", i)
        break
    else:
        print("Finding....")
    i+=1
