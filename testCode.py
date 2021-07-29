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
            
            
###########################
#  Player motion Handeler 
###########################

    ## this moves the player stratigically int the map 
    ## What this function does .
    ## Calculation of new location of the player 
    ## Collision detection.
    ## the movement should be acording to where the player is looking
            
            
