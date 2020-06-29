num=int(input("Enter iteration times: "))
fst=[]; save=[];


for bk in range(1, num+1):
    
    if bk==1:
        save.insert(0, 1)
        print(save[0])
    
    elif bk==2:
        save.insert(num-1, 1)
        fst= save.copy()
        print(save[0], save[1])
    
    elif bk>2:
        save= fst.copy()
        fst.clear()
        length= len(save)
        
        print("1", end=" ")
        for i in range(0, length-1):
            sum= save[i]+ save[i+1]
            print(sum, end=" ")
            fst.insert(i, sum)      
        print("1")
        
        fst.insert(0, 1)
        fst.insert(num-1, 1)
        save.clear()

