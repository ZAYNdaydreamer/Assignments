# Assignment 3
#Functions :

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is:", factorial(num))

#list:

numbers = [12, 5, 7, 20, 15]

numbers.append(25)
print("After append:", numbers)

numbers.remove(7)
print("After removing 7:", numbers)

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)