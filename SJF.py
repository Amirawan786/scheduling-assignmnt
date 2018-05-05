def sorting(arr,burst,pname):
    for a in range(len(arr)-1):
        for b in range(len(arr)-1-a):
            if arr[b]>arr[b+1]:
                arr[b], arr[b+1]=arr[b+1],arr[b]
                burst[b],burst[b+1]=burst[b+1],burst[b]
                pname[b],pname[b+1]=pname[b+1],pname[b]
    return arr,burst,pname


def sort2(arr1,arr2,arr3,x):
    for a in range(x-1):
        for b in range(x-1-a):
            if arr1[b]>arr1[b+1]:
                arr1[b],arr1[b+1]=arr1[b+1],arr1[b]
                arr1[b],arr2[b+1]=arr2[b+1],arr2[b]
                arr1[b],arr3[b+1]=arr3[b+1],arr3[b]
    return arr1,arr2,arr3            


import time
count1=input("enter the count of processes :")
count=int(count1)
arr=[]
burst=[]
pname=[]
for a in range(count):
    z=input("enter the process name like p1,p2.... " )
    x=input("enter the arrival time: ")
    y=input("enter the burst time:  ")
    arr.append(x)
    burst.append(y)
    pname.append(z)

print("\nprocess names: ",pname," their arrival time : ",arr," and burst time ",burst)    
print("after sorting :\n")
print(sorting(arr,burst,pname))
time.sleep(int(burst[0]))
print("process ",pname[0]," started at ",arr[0]," and ended at ",int(burst[0])+int(arr[0]))
z=int(burst[0])
arr2=[]
burst2=[]
pname2=[]
for p in range(count-1):
    x=p+1
    arr2.append(arr[x])
    burst2.append(burst[x])
    pname2.append(pname[x])
for p in range(count-1):
    y=0
    x=p       
    for j in range(count-p):
        arr2[j]=arr2[x]
        burst2[j]=burst2[x]
        pname2[j]=pname2[x]
        x=x+1
    
    while (z >=int(arr2[y]) and y<int(len(arr2))):
        y+=1
           
    sort2(burst2,arr2,pname2,y)
    time.sleep(int(burst2[0]))
    print("process ",pname2[0], " started at ", z," and ended at ",z+int(burst2[0]))
    z=int(burst2[0])+z
