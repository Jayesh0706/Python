# #Python coding tasks grouped by topic to help you practice strings, lists, dictionaries, loops, and tuples.
# '''
# 1)Reverse a String
# Write a function to reverse a given string (e.g., input: "hello", output: "olleh").'''


# str1=input("Enter your string:")
# str2=str1[::-1]
# print(str2)


# '''Check Palindrome
# Write a program to check if a string is a palindrome (reads the same backward and forward).'''

# lg=len(str1)-1
# is_pal=True
# for i in range(lg):
#     if(str1[i]!=str1[lg]):
#         is_pal=False
#         break

#     lg-=1
# if is_pal:
#     print(f"{str1} is palindrome")
# else:
#     print(f"{str1} is not palindrome")

# '''3)Find Duplicate Characters
# Identify duplicate characters in a string.
# '''

# str4=input("Enter a string :")
# is_duplicate=False
# for i in str4:
#     if str4.count(i)>1: 
#         print("duplicate occured")
#         is_duplicate=True
#         break

# if not is_duplicate:
#     print("no dupliate")


'''
5)Word Frequency
Write a function to count the frequency of each word in a string.
'''

str5=input("enter your string :")
str6=str5.split(" ")
is_again=False
again=[]
for i in str6:
    if str6.count(i) > 1 and i not in again:
        again.append(i)
    

if again:
    print("Duplicates are:",again)
else:
    print("No duplicates")

        
        
