def insertion_sort(numbers):
    a=numbers[:]; c=0
    for i in range(1,len(a)):
        k=a[i]; j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]; j-=1; c+=1
        a[j+1]=k
    return a,c

call = (insertion_sort([5, 3, 4]))
print(call)