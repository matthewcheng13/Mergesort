a = [3,1,4,1,5,9,2,6]

def merge(a,lo,mid,hi):
    n1 = mid - lo + 1
    n2 = hi - mid

    L = list()

    R = list()

    x = 0
    while x < n1:
        L.append(a[lo + x])
        x += 1
    
    y = 0
    while y < n2:
        R.append(a[mid + 1 + y])
        y += 1

    i = 0
    j = 0
    k = lo

    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def mergesort(a,lo,hi):
    if hi <= lo:
        return
    mid = lo + (hi-lo)//2
    mergesort(a,lo,mid)
    mergesort(a,mid+1,hi)
    merge(a,lo,mid,hi)
    if lo < hi:
        print(str(lo),str(mid),str(hi),a)

mergesort(a,0,7)
