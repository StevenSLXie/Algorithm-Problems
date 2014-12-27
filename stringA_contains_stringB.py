# given string s1 and string s2, tell whether all letters in s2 are in s1;
# return true or false


# Mtd 1: use Python's string.count()
def direct_count(s1, s2):
    for i in range(len(s2)):
        if s1.count(s2[i]) == 0:
            return False
    return True
    
    
# Mtd 2: sort and linear search
def sort_and_count(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    # example
    # giilnrsstt
    # ilrrstt

    n = len(s1)
    m = len(s2)
    i,j = 0,0
    
    while i < n and j < m:
        while s1[i] < s2[j] and i < n-1:
            i += 1
        if s1[i] != s2[j]:
            return False
        j += 1
    return True

    
# Mtd 3: Python 'in' Method:
def whether_in(s1,s3):
    for i in range(len(s2)):
        if s2[i] not in s1:
            return False
    return True

s1 = 'stringlist'
s2 = 'listrr1'

print direct_count(s1,s2)
print sort_and_count(s1,s2)
    
