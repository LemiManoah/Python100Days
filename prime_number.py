n = int(input("Enter a number: \n"))


def primeNumber(number):
    is_Prime = True
    for i in range (2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime == True:
        print("its a prime number")
    else:
        print("its not a prime number")
            
            
primeNumber(n)



