'''
Generate a Python list of all the even numbers between 4 to 30'''

def even(x,y):
    even_no=[]
    for i in range (x,y+1):
        if i%2==0:
            even_no.append(i)
    return even_no
newlist=even(4,30)
print(newlist)

def maximum(list):
    s=max(list)
    return s
print(maximum(newlist))