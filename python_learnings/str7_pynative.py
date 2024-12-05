str1=input("Enter string ")
search=input("Enter search string:")
searchlow=search.lower()

s2=str1.lower()
s2lst=s2.split(" ")
print(s2lst)
count=0
for word in s2lst:
    if word ==searchlow:
        count+=1
print("Occurences are:",count)
