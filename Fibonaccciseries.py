# write a program to generate fibonacci series up to n terms where n is provided by user input.
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series       

n=int(input("Enter the number of terms for Fibonacci series: "))
result = print(fibonacci_series(n))  

#write a program to reverse a list  using the function and take user input for the list elements using slicing or loop
def reverse_list(lst):
    return lst[::-1] 
user_input = input("Enter the list elements separated by spaces: ")
lst = user_input.split()
reversed_lst = reverse_list(lst)
print("Reversed list:", reversed_lst)

   

#write a program to check if a string starts with a capital letter and ends with a period and output True or False
def check_string(s):
    return s[0].isupper() and s.endswith('.')
user_string = input("Enter a string: ")
result = check_string(user_string)
print("Does the string start with a capital letter and end with a period?", result)
print(result)





#write a function to add elements upto n
def add_upto_n(n):
    return sum(range(1, n + 1))
# Take user input for n
n = int(input("Enter a number n to add elements up to n: "))    

# Call the function and print the result
result = add_upto_n(n)
print("Sum of elements up to", n, "is:", result)

#write a program to add elements upto n  and print output
def add_elements_upto_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a number n to add elements up to n: "))
result = add_elements_upto_n(n)
print("Sum of elements up to", n, "is:", result)


#write a program Summing Digits of a Number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
num = int(input("Enter a number to sum its digits: "))
result = sum_of_digits(num)
print("Sum of digits:", result)






