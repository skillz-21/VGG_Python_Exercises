def prime():
    num = int(input("Enter number: "))
    if num > 1:
        for i in range (2,num):
            if(num%i)==0:
                print(f"The number {num} is not prime")
                break
        else:
            print(f"The number {num} is prime")
    else:
        print(f"The number {num} is not prime")
prime()