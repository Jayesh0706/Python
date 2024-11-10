a=input("Enter a word: ")
b=a.lower()
vowels=0
other=0
for i in b:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vowels+=1
    else:
        other+=1

print(f"vowels:{vowels}")
print(f"others:{other}")
