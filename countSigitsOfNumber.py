def countDigitsOfNumberr(n):
    print("n = ",n)
    count=0
    while n>0:        
        count+=1
        n=n//10
        # print(n)

    return count

res=countDigitsOfNumberr(111324876444987321787)
print(res)
