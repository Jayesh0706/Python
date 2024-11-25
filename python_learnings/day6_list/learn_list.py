tea_var=["ginger","masala","lemon"]
print(tea_var)
print(tea_var[2])
tea_var[1]="kadak masala"
print(tea_var)

tea_var[1:2]="white"  #it take input like array and treats each characters as individual element of array
print(tea_var)


tea_var=["ginger","masala","lemon"]
tea_var[1:2]=["white"]  #so we give input whole string as array so it take all input once
print(tea_var)


tea_var[1:3]=["Green","basundi"]
print(tea_var)

tea_var[1:1]=["Black","Red"]  #to insert value at any index
print(tea_var)

tea_var[1:3]=[] #to delete element/s from list using empty input
print(tea_var)

tea_var.append("Shilong tea")  #adds string at last 
print(tea_var)

tea_var.pop()  #deletes last value
print(tea_var)

tea_var.remove("basundi")  #removes element at particular index
print(tea_var)

tea_var.insert(1,"Green")   #insert(index,value) add value at particular index
print(tea_var)

sqrd_num=[x**2 for x in range(1,5)]
print(sqrd_num)


my_list = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list.extend([25, 75, 100])  # extend method will accept the list of elements and add them at the end of the list. We can even add another list by using this method.
print(my_list)