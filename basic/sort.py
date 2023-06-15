a=[7,9,6,1,7,54,58,548,87,14]
n=len(a)
for i in range(n):
    for i2 in range(0,n-i-1):
        if a[i2]>a[i2+1]:
            a[i2],a[i2+1]=a[i2+1],a[i2]
print(a)

b=[7,9,6,1,7,54,58,548,87,14]
def qs_one(arr,left,right):
    mid=arr[right]#定义中值
    r=right
    for l in range(left,right):#左指针从左到右
        if r==l:               #停判条件
            arr[r]=mid
            return r
        while arr[l]<= mid:         #左边正确则后移
            l+=1
            if r==l:               #停判条件
                arr[r]=mid
                return r
        else:                  #否则交换比较右指针
            arr[l],arr[r]=arr[r],arr[l]
            r-=1
        while arr[r]>= mid:         
            r-=1
            if r==l:               #停判条件
                arr[r]=mid
                return r
        else:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
    return r
def qs_dg(arr,left,right):
    q=qs_one(arr,left,right)
    if left<q-1:
        qs_dg(arr,left,q-1)#递归左子列
    if q+1<right:
        qs_dg(arr,q+1,right)#递归右子列
    return

qs_dg(b,0,len(b)-1)
print(b)
'''
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i]),    
    
    '''