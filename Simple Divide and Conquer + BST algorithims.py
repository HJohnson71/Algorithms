
# Divde and conquer Quicksort Algorithim: O(nlogn)
def quickSort(A):
    if len(A) < 2:
        return A
    pivot = A[-1]
    less = [x for x in A if x < pivot]
    equal = [x for x in A if x == pivot]
    greater = [x for x in A if x > pivot]
    return quickSort(less) + equal + quickSort(greater)

# The following should return [1, 1, 2, 2, 3, 4, 4]
print(quickSort([1, 2, 4, 1, 2, 4, 3]))

#Median of two sorted arrays using Divide and Conquer Method: O(logn)

def median(X, Y):
    n = len(X)
    if n == 1:
        med = (X[0] + Y[0])/2
        return med
    if n == 2:
        med = (max(X[0], Y[0])+min(X[1],Y[1]))/2
        return(med)
    if n % 2  == 0:
        medx = (X[n//2] + X[(n//2)-1])// 2
        medy = (Y[n//2] + Y[(n//2)-1])// 2
        if medx == medy:
            med = medx
            return (med)
        if medx < medy:
            X = X[(n//2): n]
            Y = Y[0:(n//2)]
            return median(X, Y)
        if medy < medx:
            X = X[0:(n//2)]
            Y = Y[(n//2):n]
            return median(X,Y)
    if n % 2 != 0:
        medx = X[(n//2)+1]
        medy = Y[(n//2)+1]
        if medx == medy:
            return(medx)
        if medx < medy:
            X = X[((n//2)+1):n]
            Y = Y[0:((n//2)+1)]
            return median(X,Y)
        if medy < medx:
            X = X[0:((n//2)+1)]
            Y = Y[((n//2)+1):n]
            return median(X,Y)
print(median([1], [2])) # return 1.5
print(median([1, 2], [3, 4])) # returns 2.5
print(median([2, 3], [1, 4])) # returns 2.5
print(median([1,3,5,7], [2,4,6,8])) # returns 4.5
print(median([1,2,3,4], [5,6,7,8])) # returns 4.5
print(median([1,3,5,7,9], [2,4,6,8,10])) # returns 5.5
print(median([10,20,30,100], [15,40,60,90])) # returns 35.0
                   
# Median of two sorted arrays using Binary Search: O(log(min(n,m)))

def median2(X,Y):
    nx = len(X)
    ny = len(Y)
    if nx < ny:
        A = X
        B = Y
        n = len(A)
        totalpart = (nx + ny + 1)//2
        part1 = 0
        part2 = n
        while part1 <= part2:
            a1 = float('-inf')
            a2 = float('inf')
            b1 = float('-inf')
            b2 = float('inf')
            parta = (part1 + part2)//2
            partb = (totalpart - parta)
            if parta -1 >= 0:
                a1 = A[parta - 1]
            if parta < nx:
                a2 = A[parta]
            if partb -1 >= 0:
                b1 = B[partb -1]
            if partb < ny:
                b2 = B[partb]
            if a1 <= b2 and b1 <= a2:
                if ((nx + ny) % 2) == 0:
                    med = (max(a1,b1)+ min(a2,b2))/2
                    return(med)
                if ((nx + ny) % 2) != 0:
                    med = max(a1,b1)
                    return(med)
            elif a1 > b2:
                part2 = parta - 1
            else:
                part1 = parta + 1
        return 0
    if ny < nx:
        A = Y
        B = X
        n = len(A)
        totalpart = (nx + ny + 1)//2
        part1 = 0
        part2 = n
        while part1 <= part2:
            a1 = float('-inf')
            a2 = float('inf')
            b1 = float('-inf')
            b2 = float('inf')
            parta = (part1 + part2)//2
            partb = (totalpart - parta)
            if parta -1 >= 0:
                a1 = A[parta - 1]
            if parta < ny:
                a2 = A[parta]
            if partb -1 >= 0:
                b1 = B[partb -1]
            if partb < nx:
                b2 = B[partb]
            if a1 <= b2 and b1 <= a2:
                if ((nx + ny) % 2) == 0:
                    med = (max(a1,b1)+ min(a2,b2))/2
                    return(med)
                if ((nx + ny) % 2) != 0:
                    med = max(a1,b1)
                    return(med)
            elif a1 > b2:
                part2 = parta - 1
            else:
                part1 = parta + 1
        return 0
print(median2([1], [2, 3])) # return 2.0
print(median2([1, 3], [2])) # return 2.0
print(median2([1,2,3,4], [3,4])) # returns 3.0
print(median2([1,3,5,7,9], [2,4,6,8,10,11])) # returns 6.0
print(median2([1,3,7,8,9], [2,4,5,6,10,11])) # returns 6.0
print(median2([1], [2,3,4,5,6,7])) # returns 4.0
print(median2([10,20,30,100], [40,60])) # returns 35.0
    
