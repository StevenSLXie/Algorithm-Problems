# palindrome
# 回文字判断

def palindrome_from_edge_to_mid(s):
    mid = len(s)/2
    for i in range(mid):
        if s[i] != s[-i-1]:
            return False
    return True    

def palindrome_form_mid_to_edge(s):
    mid = len(s)/2
    if is_even(len(s)):
        for i in range(mid):
            if s[mid-1-i] != s[mid+i]:
                return False
        return True
    else:
        for i in range(mid):
            if s[mid-1-i] != s[mid+i+1]:
                return False
        return True
        
def is_even(l):
    if l % 2 == 0:
        return True
    return False
        
print palindrome_from_edge_to_mid('abcddcba')
print palindrome_form_mid_to_edge('abcddcba')
print palindrome_from_edge_to_mid('abbba')
print palindrome_form_mid_to_edge('abbba')

print palindrome_from_edge_to_mid('abcddcbaee')
print palindrome_form_mid_to_edge('abcddcbaee')
print palindrome_from_edge_to_mid('abbbaee')
print palindrome_form_mid_to_edge('abbbaee')
