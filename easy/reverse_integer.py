# Given a 32-bit signed integer, reverse digits of an integer.
n = -120
a = 120
def reverse(n):
    if n < 0:
        return -int(str(n)[::-1][:-1])
    else:
        return int(str(n)[::-1])

print(reverse(n))
print(reverse(a))