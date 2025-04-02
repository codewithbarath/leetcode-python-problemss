n=5
i=0
new=[]
while(i<n):
    i=i+1
    new.append(i)
for i in range(len(new)):
    if(new[i]%3==0 and new[i]%5==0):
        new[i]="fizzbuzz"
    elif(new[i]%3==0):
        new[i]="fizz"
    elif(new[i]%5==0):
        new[i]="buzz"
    else:
        new[i]=i+1
        

print(new)