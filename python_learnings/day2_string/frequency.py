a=input("Enter a word:")
freq={}
for char in a:
    if char in freq:
        freq[char] += 1
    else:
        freq[char]=1
print(freq)


str=input("Enter a string:")
splitstr=str.split()
freq={}
for word in splitstr:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)
