import math
def lineTracer(y,x,lineAngle,Levelmap):##3.0
    
    
    lineLen=0
    #length of line is stored in this variable
    
    ##first thing find slope of the line
    m=math.tan(lineAngle*rd)

    ##now unit distance for this line in any direction will be 
    
    
    
    Sx=(1 + m**2)**(0.5)
    Sy=(1 + 1/(m**2))**(0.5)

    
    
    
    ## now lets find out the direction for the line ...
    muly=1
    mulx=1
    if (lineAngle<180 and lineAngle>90):
        
        mulx=-1
    elif (lineAngle>180 and lineAngle<270):
        mulx=-1
        muly=-1
    elif (lineAngle<360 and lineAngle>270):
        muly=-1
    
    
    
    
    
    # therefore  lets get length of x and y ... that will be added rto get final quardinates 
    
    ylen=0
    
    xlen=0

    ##now calculating deviation from the edge delx and dely
    dely=1
    delx=1

    ### If angle of line is in range 90 and 0 
    
    if lineAngle>0 and lineAngle<90:
        
        dely=y-int(y)
        delx=1-(x-int(x))
    
    ### If angle of line is in range 90 an
    if lineAngle>90 and lineAngle<180:
        dely=y-int(y)
        delx=(x-int(x))
    


    ### If angle of line is in range 180 and 270  
    if lineAngle>180 and lineAngle<270:
        dely=1-(y-int(y))
        delx=(x-int(x))

    ### If angle of line is in range 270 and 360 
    if lineAngle>270 and lineAngle<360:
        dely=1-(y-int(y))
        delx=1-(x-int(x))
    print(dely,delx)
        
    # now calculating the first intersepts
    lx=Sx*delx
    ly=Sy*dely
    
    if(lx<ly):
        lineLen=lx
        leny=ly-lx
        lenx=0
    else:
        lineLen=ly
        lenx=lx-ly
        leny=0
    print("SX",Sx)
    print("SY",Sy)
    print("DX",delx)
    print("DY",dely)
    print("LX",lx)
    print("LY",ly)
    print("lineLen",lineLen)
    tmpdelx=x+(mulx*delx)
    tmpdely=y+(muly*dely)
    if x==-1:
        tmpdelx-=1
    if y==-1:
        tmpdely-=1
    if(Levelmap[int(tmpdely)][int(tmpdelx)]!=0):
        return(lineLen)
        
    
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
            tmpdelx+=1
            
        else:
            lenx-=leny
            lineLen+=leny
            leny=0
            dely+=1
            tmpdely+=1
        ### Checking if a wall or any thing is found in the locaiton reached
        
        #print("SX",Sx)
        #print("SY",Sy)
        print("DX",delx)
        print("DY",dely)
        print("LX",lx)
        print("LY",ly)
        print("lineLen",lineLen)
        
        if x==-1:
            tmpdelx-=1
        if y==-1:
            tmpdely-=1
        print(tmpdely,tmpdelx)
        print(Levelmap[int(tmpdely)][int(tmpdelx)])
        if(Levelmap[int(tmpdely)][int(tmpdelx)]!=0):
            break
    return(lineLen)
