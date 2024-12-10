# '''
# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it'''


# def outer (a,b):
#     def inner():
#         return a+b
    
#     result=inner()+5
#     return result

# out=outer(5,10)
# print(out)



'''
Exercise:
Create an outer function that accepts three parameters, x, y, and z.

Inside the outer function, create an inner function that calculates the product of x and y.
The outer function should then multiply the result of the inner function by z and return the final result.'''

def newouter(x,y,z):
    def newinner():
        return x*y
    result=newinner()*z
    return result

s=newouter(2,3,4)
print(s)



'''
2. Exercise: Nested String Manipulation
Create an outer function that accepts a string, s.

Inside the outer function, define an inner function that returns the reverse of the string.
The outer function should then concatenate "Python" to the reversed string and return the result.'''

def out(str1):
    def inn():
        return str1[::-1]
    results=inn()
    return results

o=out("Jayesh")
print(o)


'''
3. Exercise: Double Inner Functions
Create an outer function that accepts a single parameter, num.

Inside the outer function, define one inner function to calculate the square of num.
Define a second inner function to calculate the cube of num.
The outer function should then return the sum of the results of the two inner functions.
'''

def doubleouter(num):
    def firstinner():
        return num **2
    def secondinner():
        return num**3
    
    result=firstinner()+secondinner()
    return result

x=doubleouter(5)
print(x)