
#Find all pairs of numbers in the list whose product is even and whose sum is odd

L = [1,2,3,4,5]

end = [] 

for i in range(len(L)-1):
    for k in range (1,len(L)):
        tmp = []
        if  (L[i] * L[k]) % 2 == 0 and (L[i] + L[k]) % 2 == 1:
            tmp.append(L[i])
            tmp.append(L[k])
            end.append(tmp)

#Print formatted list of the pair
count  = 1
for item in end:
    print("Pair " + str(count) +": " + str(item))
    count +=1
            
