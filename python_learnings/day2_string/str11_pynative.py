str=input("Enter string:")
splstr=str.split(" ")

for i in splstr:
    flag_digit=False
    flag_alpha=False
    for y in i:
        if(y.isdigit()):
            flag_digit=True 
        if(y.isalpha()):
            flag_alpha=True
       

    if flag_digit and flag_alpha:
        print(i)
    else:
        print("")

