import time
count =input("Enter the number of processes you want to enter in the ready queue : ")
list=[]
for a in range(int(count)):
  x=input("Enter the process number like p1 ,p2....  ")
  y=input("Enetr the arrival time:  ")
  z=input("Enter the burst time: ")
  list.append([y,z,x])
list.sort()
print(list)
print(" ")
time.sleep(int(list[0][1]))
print("process ",list[0][2]," started at ",list[0][0]," and ended at ",int(list[0][1])+int(list[0][0]))
print("waiting time = ",0)
t=int(list[0][1])+int(list[0][0])
f=0
      
for b in range(int(count)-1):
    f=int(list[b+1][1])+t
    time.sleep(int(list[b+1][1]))
    if int(list[b+1][0])>t:
      print("process ",list[b+1][2]," started at ",list[b+1][0]," and ended at ",int(list[b+1][0])+int(list[b+1][1]))
      print("Waiting time = ", 0)
      t=int(list[b+1][1])+int(list[b+1][0])
    else  :
      print("process ",list[b+1][2]," started at ",t," and ended at ",f)
      print("waiting time = ", t-int(list[b+1][0]))
      t=int(list[b+1][1])+t

