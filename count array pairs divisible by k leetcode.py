nums=[1,2,3,4,5]
k=2
count=0
for i in range(len(nums)):
    for j in range(len(nums)):
        if (i<j)and((nums[i]*nums[j])%k==0):
            count+=1
print(count)