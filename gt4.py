#program for implementation of heap sort in python
                
def heapsort(A):
    n=len(A)
    for i in range(n-1,-1,-1):
        heapify(A,n,i)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)


def heapify(A,n,i):
    leftchild=2*i +1
    rightchild=2*i +2
    largestvalue=i
    if rightchild<n and A[i]<A[rightchild]:
        largestvalue=rightchild
    if leftchild<n and A[largestvalue]<A[leftchild]:
        largestvalue=leftchild
    if largestvalue!=i:
        A[i],A[largestvalue]=A[largestvalue],A[i]
        heapify(A,n,largestvalue)


A=list()
n=input("Enter the number of elements in the array:")
print("Enter the numbers in the array")
for i in range(int(n)):
    val=input("Number is:")
    A.append(int(val))
print("Input array",A)
heapsort(A)
print("Sorted array:",A)
