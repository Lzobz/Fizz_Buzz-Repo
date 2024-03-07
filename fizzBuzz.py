numbers = range(101)
for n in numbers:
    if n % 5 == 0 and n % 3 == 0:
        n=("fizzbuzz")
        print (n)
    elif n % 3 == 0:
        n=("fizz")
        print (n)
    elif n % 5 == 0:
        n=("buzz")
        print (n)
    else:
        print (n)