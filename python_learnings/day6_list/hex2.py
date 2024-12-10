'''
Exercise 3: Remove items from a list while iterating
Description:

In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50'''

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in range(len(number_list)-1):
#     if number_list[i]>=50:
#         del number_list[i]
#     else:
#         continue
# print(number_list)

#*******Using for with range assumes a fixed range length, but deleting an element shortens the list, leading to skipped elements.******
i=0
while i<len(number_list):
    if number_list[i]>50:
       del number_list[i]
    else:
       i+=1
print(number_list) 
 
#***while loop, we can manually control the index to avoid skipping elements after deletions.***
#example for why sometimes we use for loops