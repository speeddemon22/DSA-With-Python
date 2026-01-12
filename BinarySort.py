#Two methods to do this are recursion and using two pointers#
# method 1#
def binarysearch(seq,v,l,r):
    if (r-l ==0):
        return(False)
    mid =( l+r )//2 
    if v == mid:
        return (True)
    if v < seq[mid]:
        return ( binarysearch(seq,v,l,mid))
    if v > seq[mid]: 
        return (binarysearch(seq,v,mid+1,r))
seq1 = [1,2,3,4,5,6,7,8,9,10]
t = binarysearch(seq1,11,seq1[0],seq1[9])
print(t)
