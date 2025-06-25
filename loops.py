nums=[1,3,5,7,9,12]
#for loop
for num in nums:
    print(num)
# while loop 
i=0

while i<5:
    print(i)
    i += 1 #i=i+1

nums=[1,3,5,7,9,12]

# for loop with range 0 to 3
for i in range(len(nums[0:3])):
    print(nums[i])

# List comprehension to square each number in nums
out=[]

for num in nums:
    out.append(num**2)
    print(out)
