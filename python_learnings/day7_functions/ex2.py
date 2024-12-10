'''
Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.'''


def func1(*args):
    for i in args:
        print(i)

func1("Jayesh","Nalawade",24)