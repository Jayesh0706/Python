chai="  Masala Chai "
chai=chai.strip()   #used while taking user input cause users give spaces mistakenly

print(chai.lower())   #to check string we use this , first low all string and then check / same for upper

print(chai.upper())

#inp=input("Give your type: ")
#print(chai.replace("Masala",inp))


types="Lemon, Ginger, Masala, Basundi"
print(types.split(", "))   #used to convert string to list
print("a,asdb,fc,ad".split(","))


type_list=["Lemon","Ginger","Masala","Basundi"]
print(type_list)
type_str="-".join(type_list)  #List to string,used in url joining
print("type str is: ",type_str)
print(type(type_str))


print(types.find("Masala"))  #used to finf particular word from string


course="Devops"
type="IT"

job="{} course and type is {}"

print(job.format(course,type))  #used in api to add values