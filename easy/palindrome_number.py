# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

a = -121

def isPalindrome(a):
    return str(a) == str(a)[::-1]

print(isPalindrome(a))