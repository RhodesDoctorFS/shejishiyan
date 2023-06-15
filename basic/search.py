a=[1,5,8,7,5,8,4,4,4,7,9]
search=input("输入要找到数字")
search=int(search)
for i in range(len(a)):
    if a[i]==search:
        print("存在")
        break
    if i==len(a)-1:
        print("未找到")

b=[1, 6, 7, 7, 9, 14, 54, 58, 87, 548]
search=input("输入要找到数字")
search=int(search)
start=0
end=len(b)-1
judge=0
while start<=end:
    mid=int((start+end)/2)
    if search>b[mid]:
        start=mid+1
    elif search<b[mid]:
        end=mid-1
    else :
        print("找到了,位于%s" %mid)
        judge=1
        break
if judge!=1:
    print("失败了")

 