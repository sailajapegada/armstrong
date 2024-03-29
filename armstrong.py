def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    
    if sum_of_digits == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
