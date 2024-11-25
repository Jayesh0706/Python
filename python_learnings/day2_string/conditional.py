# age=15
# if(age>=18 and age<=60):
#     print("Eligible")

# else:
#     print("Not eligible")


# light="green"
# if(light=="red"):
#     print("stop")
# elif(light=="Yl"):
#     print("slow")
# elif(light=="green"):
#     print("Go")

#nesting
age=int(input("Enter your age:"))

if(age>=18):
    if(age>80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cant drive")