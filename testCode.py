#this file contains test code ... this contains the rendering code ... but its not full code ...
# and is just so that i can understand the working thn make full sable code .
#though this code will also run .


########################################################################################
                                #IMPORT LIBRARY
########################################################################################
import numpy as np
import cv2
import matplotlib.pyplot as plt
########################################################################################
########################################################################################


########################################################################################
                                # INTIALIZATTION VARIABLE
########################################################################################

fov=100
ppx=13 #player position in x 
ppy=2 #player position in y
pva=0 #player view angle
GameResolution=[720,1280]
miniMapResolution=[480,854]
MapSize=[16,16]
########################################################################################
########################################################################################



########################################################################################
                                # TEST MAP
########################################################################################

# Real code will import map that can be made from level designer


mp=[[1,1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1.,1],    #DEFAULT MAP
    [1,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.,1],
    [1,0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0.,1],
    [1,1., 1., 1., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0.,1],
    [1,0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0.,1],
    [1,0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 1., 0.,1],
    [1,0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.,1],
    [1,0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.,1],
    [1,0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.,1],
    [1,0., 1., 1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0, 1],
    [1,0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0.,1],
    [1,1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0.,1],
    [1,1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 0, 0.  ,1  ],
    [1,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,1],
    [1,0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,1],
    [1,1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1.,1]]

########################################################################################
########################################################################################    



########################################################################################
                        #MAP UPSCALER CODE
######################################################################################## 
##map upscler code

map_Y_Miltiplier=int(miniMapResolution[0]/MapSize[0]) 
map_X_Miltiplier=int(miniMapResolution[1]/MapSize[1])
#these multiplier no whn multiplies to orignal size of the map gives map in almost 480p Res


#this is where the higher resolution is calculated.
mapy=MapSize[0]*map_Y_Miltiplier    #first using y multiplier 
mapx=MapSize[1]*map_Y_Miltiplier
if(mapx>miniMapResolution[1]):      #thn if the resolution is not corrrect 
    mapy=MapSize[0]*map_X_Miltiplier#we will use x multipler 
    mapx=MapSize[1]*map_X_Miltiplier
    map_Y_Miltiplier=map_X_Miltiplier#the main multipler in all eq will be y multiplier so... put the right multiplier in it 
    
    



#this is the map resolution close to 480p

miniMap=np.zeros([mapy,mapx])
miniMapInfo=np.zeros([mapy,mapx])
i=0
y=0
mmi=0
mmy=0
while True:
    if(mmi<MapSize[0]):
        y=0
        mmy=0
        while True:
            if(mmy<MapSize[1]):
                #print(mmi)
                #print(mmy)
                if(mp[mmi][mmy]==1):
                    for x in range(i,i+map_Y_Miltiplier):
                        for z in range(y,y+map_Y_Miltiplier):
                            miniMap[x][z]=1
                            miniMapInfo[x][z]=1
                y+=map_Y_Miltiplier
                mmy+=1
            else:
                break
    else:
        break
    i+=map_Y_Miltiplier
    mmi+=1
########################################################################################
######################################################################################## 


########################################################################################
                                #1. GAME METHODS
########################################################################################

##Draws the player and the direction stick ahead of the player 
def DrawPlayer(posi,posy,mapar):#gets player position in x and y cordinates in the frame matrix
    for i in range(posi-playerSize,posi+playerSize+1):
        for y in range(posy-playerSize,posy+playerSize+1):
            mapar[i][y]=1            
##Removes remains of the player and the direction stick of the player 
def RemPlayer(posi,posy,mapar):#gets player position in x and y cordinates in the frame matrix
    for i in range(posi-playerSize,posi+playerSize+1):
        for y in range(posy-playerSize,posy+playerSize+1):
            mapar[i][y]=0    
######################################  
    # LINE FUNCTIONS    #
######################################

def drawLine(thickness,lar,mapvr):
    thickness=int(thickness/2)
    for i in lar:
        for x in range(i[0]-thickness,i[0]+thickness+1):
            for y in range(i[1]-thickness,i[1]+thickness+1):
                mapvr[x][y]=1
    
def remLine(thickness,lar,mapvr):
    thickness=int(thickness/2)
    for i in lar:
        for x in range(i[0]-thickness,i[0]+thickness+1):
            for y in range(i[1]-thickness,i[1]+thickness+1):
                mapvr[x][y]=0
                
def isWall(MpInfo,x,y):
    if(mpInfo[x][y]>=1):
        return(True)
    return(False)
    
def lineTracer(posi,posy,dist,pva):
    lineAr=[] # will keep track of all the points of the line 
    
    if(dist==0):
        dist=80
    

    if(pva==0 or pva==360):
        pva+=0.3
    elif(pva==270 or pva==90):
        pva+=0.3
       
    disy = abs(1/math.tan(rd*pva))
    disx = abs(math.tan(rd*pva))
    print(disy,disx)
    flg=0
    xadder=0
    yadder=0
    multiplierxa=-1
    multiplierya=1
    if(pva>90 and pva<=180):
        multiplierya=-1
    elif(pva>180 and pva<=270):
        multiplierxa=1
        multiplierya=-1
    elif(pva>270 and pva<=360):
        multiplierxa=1
        multiplierya=1
    
    #################################################
    #Cases to look at
    #1. x>y
    #2. Y<x
    #3  y==x
    #################################################
    #if x is greater than y 
    lineAr.append([posi,posy])
    if(disy>disx):
        
        
        print("y is bigger")
         
        y=disy #so this for every increase in y there will be y no of x increase 
        #initial y 
        prev_y=0
        
        
        
        
        
        noOfSteps=0
        while True:
            prev_y=y
            y+=disy
            
            
            for x_lp in range(1,(int(y)-int(prev_y))+1):
                yadder+=(1*multiplierya)
                
                lineAr.append([posi+xadder,posy+yadder])
                
                noOfSteps+=1
                if(noOfSteps==dist):
                    flg=1
                    break
            
            xadder+=(1*multiplierxa)
            lineAr.append([posi+xadder,posy+yadder])
            noOfSteps+=1
            if(noOfSteps==dist or flg==1):
                break
                
                
                
    elif(disx>disy):
        print("x is bigger")
        x=disx #so this for every increase in y there will be y no of x increase 
        #initial y 
        prev_x=0
        
        
        noOfSteps=0
        while True:
            prev_x=x
            x+=disx
            for x_lp in range(1,(int(x)-int(prev_x))+1):
                xadder+=(1*multiplierxa)
                lineAr.append([posi+xadder,posy+yadder])
                noOfSteps+=1
                if(noOfSteps==dist):
                    flg=1
                    break
            yadder+=(1*multiplierya)
            lineAr.append([posi+xadder,posy+yadder])
            noOfSteps+=1
            if(noOfSteps==dist or flg==1):
                break
    else: ##When both x and y are equal or andle is multiple of 45 something
        print("they are same")
        noOfSteps=0
        while True:
            step+=1
            xadder+=(1*multiplierxa)
            yadder+=(1*multiplierya)
            lineAr.append([posi+xadder,posy+yadder])
            if(noOfSteps==dist):
                break
    print("Ar",lineAr)
    return(lineAr)
###########################
#  Player motion Handeler 
###########################

    ## this moves the player stratigically int the map 
    ## What this function does .
    ## Calculation of new location of the player 
    ## Collision detection.
    ## the movement should be acording to where the player is looking
def MovPlayer(posi,posy,pva,mapar,direction,dis,        na):  ## this is work in progress.  (Changes to the line(pva,dis,na))
                                               #,#new angle(add it to current player angle)
    RemPlayer(posi,posy,mapar)
    if(direction=='w'):
        posi-=(StepSize*dis)
    elif(direction=='s'):
        posi+=(StepSize*dis)
    elif(direction=='d'):
        posy+=(StepSize*dis)
    elif(direction=='a'):
        posy-=(StepSize*dis)
    DrawPlayer(posi,posy,mapar)
    return(posi,posy)
  
#########################################################################################################
###################################### THE 3D RENDERER ##################################################
#########################################################################################################


def threDRenderer(posi,posy,pva,frame):
    
    #### Define Variable :-

    FOV=45
    StartAngle=pva+FOV;
    EndAngle=pva-FOV;
    AngularStep=(FOV*2)/GameResolution[1]
    PlayerHeight=0
    center=(GameResolution[0]/2)-1

    for i in range(GameResolution[1]):
      #Gooing column by column 
      ln,ty,lineIntercept=lineTracer(posi,posy,0,StartAngle-(AngularStep*i),1)
      
      ### Choosing the texture collumn (for now only from wall texture)(WAllTextur=[]).
      hori,verti=WAllTextur.shape

      clmno=int(lineIntercept*(verti-1))




      ##height calculation........

      height=GameResolution[1]/ln

      startPoint=center-(height/2)

      endPoint=center+(height/2)

      for y in range(startPoint,endPoint+1):
          frame[y][i][0]=1
          #frame[y][i][0]=1
          #frame[y][i][0]=1
    return (frame)
      
##########################################

#MAIN GAME LOOP INITIALIZATION

##########################################




ppx=int(ppx*map_Y_Miltiplier)
ppy=int(ppy*map_Y_Miltiplier)
pva=0
lar=[[ppx,ppy]]
print(ppx)
print(ppy)
print
DrawPlayer(ppx,ppy,miniMap)


while True:
    plt.imshow(miniMap)
    plt.show()
    #cv2.imshow('Doom', miniMap)
    print("Dir dis ang")
    
    #make a try catch block here
    
    direction,dis,ang=input().split()
    if direction=="exit":
        break
    dis=int(dis)
    ang=int(ang)
    ppx,ppy,lar,pva=MovPlayer(ppx,ppy,pva,miniMap,direction,dis,ang,lar)
    print(ppx)
    print(ppy)

            
