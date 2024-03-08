#sets range for the numbers
for n in range(101):
    #logic of printing FizzBuzz for numbers divisible by 5 and 3
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    #logic of printing Fizz for numbers divisible by 3
    elif n % 3 == 0:
        print("Fizz")
    #logic of printing Buzz for numbers divisible by 5 
    elif n % 5 == 0:
        print("Buzz")
    #prints all other numbers
    else:
        print(n)