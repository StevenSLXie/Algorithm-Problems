# Minimum Coin
# Given several types of coin, say 1, 3, 5 dollars respectively and a total number S. 
# Find the minimum number of coins such that the total is equil to S.

def minCoin(S,type):
    d = [ 100000 for x in range(S+1)]
    d[0] = 0
    d[1] = 1
    for i in range(1,S+1):
        for j in range(0,i):
            for z in type:
                if j+z == i and d[j]+1<d[i]:
                    print z
                    d[i] = d[j]+1
    print '\n'           
    print [x for x in d]
    
minCoin(13,[1,3,5])
