# Write a Program to find a prime number
# num = 23
num = int (input("Enter The Number:"))
if num == 1 :
    print("num is not a Prime number",num)
elif num > 1 :
    for i in range (2,num) :
        if (num % i ) == 0 :
            print(num ,"is not  a Prime number as it is divisible by", i )
            break
    else :
            print ("num is a prime number",num)
