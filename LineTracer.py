import time
import math
def lineTracer(y,x,lineAngle,Levelmap):##3.0
    
    currentItercept=""
    lineLen=0
    #length of line is stored in this variable
   

    ##first thing find slope of the line
    m=math.tan(lineAngle*rd)

    ##now unit distance for this line in any direction will be 
    
    
    
    Sx=(1 + m**2)**(0.5)
    Sy=(1 + 1/(m**2))**(0.5)

    
    
    
    ## now lets find out the direction for the line ...
    muly=-1
    mulx=1

    if(lineAngle>270 or lineAngle<90):
        mulx=1
    else:
        mulx=-1
    
    if(lineAngle<180 and lineAngle>0):
        muly=-1
    else:
        muly=1
    #print("mulx:",mulx)
    #print("muly:",muly)
    # therefore  lets get length of x and y ... that will be added rto get final quardinates 
    
    ylen=0
    
    xlen=0

    ##now calculating deviation from the edge delx and dely
    dely=1
    delx=1

    
    
    if(lineAngle>270 or lineAngle<90):
        delx=1-(x-int(x))
    else:
        delx=(x-int(x))
    
    if(lineAngle<180 and lineAngle>0):
        dely=y-int(y)
    else:
        dely=1-(y-int(y))
  
   
    
    # now calculating the first intersepts
    lx=Sx*delx
    ly=Sy*dely
    tmpdelx=x
    tmpdely=y
    if(lx<ly):
        lineLen=lx
        leny=ly-lx
        lenx=0
        currentItercept="x"
        tmpdelx+=(mulx*delx)
    else:
        lineLen=ly
        lenx=lx-ly
        leny=0
        currentItercept="y"
        tmpdely+=(muly*dely)
        
    
    #print("SX",Sx)
    #print("SY",Sy)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("DX",delx)
    #print("DY",dely)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("LX",lx)
    #print("LY",ly)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #print("lineLen",lineLen)
    #print("currentItercept",currentItercept)
    
    
    
    
    ctmpdelx=tmpdelx
    ctmpdely=tmpdely
    
    if muly==-1 and currentItercept=="y":
        ctmpdely=tmpdely-1
    #print(ctmpdely)
    #print(ctmpdelx)
    #print(Levelmap[int(ctmpdely)][int(ctmpdelx)])
    if(Levelmap[int(ctmpdely)][int(ctmpdelx)]!=0):
        return(lineLen)
        
    #print("#############################################")
    while True: ##main loop
        ##lenfor eaxh axis
        
        if lenx==0:
            lenx=Sx
        if leny==0:
            leny=Sy
        
        #comapring length 
        if lenx<leny:
            leny-=lenx
            lineLen+=lenx
            lenx=0
            delx+=1
            tmpdelx+=(mulx*1)
            currentItercept="x"
        else:
            lenx-=leny
            lineLen+=leny
            leny=0
            dely+=1
            tmpdely+=(muly*1)
            currentItercept="y"
        ### Checking if a wall or any thing is found in the locaiton reached
        
        #print("SX",Sx)
        #print("SY",Sy)
        #print("DX",delx)
        #print("DY",dely)
        #print("LX",lx)
        #print("LY",ly)
        #print("lineLen",lineLen)
        ctmpdelx=tmpdelx
        ctmpdely=tmpdely

        if muly==-1 and currentItercept=="y":
            ctmpdely=tmpdely-1
        #print(ctmpdely,ctmpdelx)
        #print(Levelmap[int(ctmpdely)][int(ctmpdelx)])
        if(Levelmap[int(ctmpdely)][int(ctmpdelx)]!=0):
            break
        #print("#############################################")
    return(lineLen,currentItercept)
            
