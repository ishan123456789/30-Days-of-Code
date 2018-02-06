a = int(raw_input())
for i in range(0,a):
    b = raw_input()
    tempO = ""
    tempE = ""
    for i in range(0,len(b)):
        
        if(i%2 ==0):
            tempE = tempE+b[i]
        else:
            tempO = tempO+b[i]
        if(i == len(b)-1):
            print tempE,tempO 
            
