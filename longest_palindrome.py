# Find the length of the longest Palindrome
# Given a string s
# Output the length l

def odd_longest(s,i):
    # setrtes
    # 0123456
    iteration_time = min(i,len(s)-i-1)
    for j in range(iteration_time):
        if s[i-j-1] != s[i+j+1]:
            return 2*j+1
            
    return 2*iteration_time + 1
            
def even_longest(s,i):
    # settes
    # 012345
    iteration_time = min(i+1,len(s)-i-1)
    for j in range(iteration_time):
        if s[i-j] != s[i+j+1]:
            return 2*j 
            
    return 2*iteration_time
    
def find_longest(s):
    l  = len(s)
    max = 1
    for i in range(0,l):
        c = odd_longest(s,i)
        print 'odd:'+ str(c)
        max = bigger(max,c)
        
        c = even_longest(s,i)
        print 'even:' + str(c)
        max = bigger(max,c)
        
    return max
        
def bigger(a,b):
    if a>b:
        return a
    else:
        return b

            
print find_longest('wwww')
