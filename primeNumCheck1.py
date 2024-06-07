# #create the logic this way:
# A prime number is a number greater than 1, wchich has only 2 factors; 1 and the number itself
# An example of a Prime Number is 23, only 1 and 23=> so is a Prime Number
# An example of a number which is not a Prime Number is 27 => divisible factors are more than 2..i.e 1,3,9,27

num1= 23
count=0 # will help us count how many factors are there

if num1>1:
    for i in range(1,num1+1):
        if (num1%i)==0:
            count= count+1
    if count==2:
            print(str(num1)+ " is a Prime Number")
    else:
            print(str(num1)+ " is not a Prime Number")

#python primeNumCheck1.py Runs this on the terminal