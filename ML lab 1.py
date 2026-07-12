def countpairs(elements):
    count=0
    for i in range(len(elements)):
        for j in range(i+1,len(elements)):
            if elements[i] + elements[j]==10:
                count=count+1
    return count
elements=[2,7,4,1,3,6]
number=countpairs(elements)
print("Number of pairs with sum 10 are=",number)
