#The accumulator function
nums=[1,2,3,4,5,6,7,8,9,10]
accum=0
for w in nums:
    accum=accum+w
    print(accum)

#Now we will see
nums=[1,2,3,4,5,6,7,8,9,10]
accum=0
for w in nums:
    accum=accum+w
print(accum)

#Range function
nums=[1,2,3,4,5,6,7,8,9,10]
print("range(5):")
for i in range(5):
    print(i)
print("range(0,5):")
for i in range(0,5):
    print(i) 
#Notice the casting of range to the list
print(list(range(5)))
print(list(range(0,5)))
print(range(5))
