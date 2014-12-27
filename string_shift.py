# String shift
# Given a string, say 'abcdefg'. Move the first m string to the end of the string;
# For example, if m ==2, the output would be 'cdefgab';
# Assume the input is a string like 'algorithm', not a string list like ['s','o','m','e']
# Assume the output is also a string

# Requirement: time complexity n, space complexity 1


# Mtd 1: Direct pop and append    
def move(s,m):
    s2 = list(s)
    
    for i in range(m):
        s2.append(s2.pop(0))

    out = listToString(s2)
    return out
    
# Mtd 2: direct concat 
# For Python, this seems most intuitive
def concat(s,m):
    import copy
    s = list(s)
    t = copy.copy(s)
    del s[:]
    s += t[m:] + t[:m]
    out = listToString(s)
    return out

# Mtd 3: invert method
def invert(s):
    s2 = list(s)
    
    for i in range(len(s)):
        s2.append(s2.pop(0))
        
    return s2
    
def invert_solution(s,m):
    s_list = list(s)
    
    s1 = invert(s_list[:m])
    s2 = invert(s_list[m:])
    
    out = invert(s2+s1)
    
    return listToString(out)


# a function to convert list to string
def listToString(l):
    s = ''
    for i in range(len(l)):
        s += l[i]
        
    return s
    
s = 'abcdefgsss'
print move(s,4)
print concat(s,4)
print invert_solution(s,4)
