# Given a string, print out all possible permutations of s

# For example, given 'abc', print out 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'


def solution(s):
    s_list = list(s)
    l = len(s_list)
    # permutation('abc')
    for p in permutation(s_list):
        print p

def permutation(s):
    if len(s)<=1:
        yield s
    else:
        for p in permutation(s[1:]):
            for i in range(len(p)+1):
                yield p[:i] + s[0:1] + p[i:]
        
    
    
solution('abcd')
