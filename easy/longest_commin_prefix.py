# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

a = ["flower","flow","flight"]

def longestcommonprefix(a):
    shortest = min(a, key=len)
    for x, y in enumerate(shortest):
        for other in a:
            if other[x] != y:
                return shortest[:x]
    return shortest

print(longestcommonprefix(a))


https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution