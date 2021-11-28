import time
import math
def checkY(y,x,Levelmap):
    
def lineTracer(y,x,lineAngle,Levelmap):##4.0
    
    dely=math.tan(lineAngle)
    delx=1/dely
    
    llpy=math.sin(lineAngle)
    llpx=math.cos(lineAngle)
    
    
    tllpy=llpy
    tllpx=llpx
    lineLen=0
    while True:
        
        if(tllpy<tllpx):
            lineLen+=tllpy
            tllpx-=tllpy
            tllpy=llpy
            y+=1
            x+=delx
            
        else
            lineLen+=tllpx
            tllpy-=tllpx
            tllpx=llpx
            x+=1
            y+=dely
        if checkY(y,x,Levelmap):
            break
    
