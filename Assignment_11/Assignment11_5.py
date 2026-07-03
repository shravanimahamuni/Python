# Write a program which accepts one number and checks whether it is palindrome or not.

def ChkPalindrome(no):
    temp = no
    rev = 0 

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no//10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not palindrome")

ChkPalindrome(121)