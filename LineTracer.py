import math
def lineTracer(y,x,LineAngle,levelMap):
  lineTangent=math.tan(angle)
  
  delx=x-int(x)
  dely=y-int(y)
  
  lineTraceStat=0
  
  while lineTraceStat==0:
    
     foundYIntercept=0
        #if y intercept is not found then x axis is calculated
        
        
        ##############       Y AXIS            ################
        if lineAngle<90 or lineAngle>270:
            xa=1-delx
            h=lineTangent(xa)
            
        ##code working ok sudo checked
            
        else:
            if(delx!=0):
                xa=-delx
                h=lineTangent(xa)
                
            else:
                xa=-1
                h=lineTangent(xa)
        
        if (dely-h>=0 and dely-h<=1) or (dely==0 and h<=-1 and h<0):
            x+=xa
            y-=h
            dely-=h
            delx=0
            foundYIntercept=1
        
        
        ##############       X AXIS            ################
        if(foundYIntercept==0):#if y intercept failed find x intercept
            
            if lineAngle>0 or lineAngle<180:
                if dely!=0:
                    b=dely/lineTangent
                else:
                    b=1/lineTangent
            else:
                b=(1-del)/lineTangent
            
            if delx+b==1 or delx+b==0:
                dely=0
                delx=
                
        
    
      
      
      
      
    
    ## CAlculate x if y not found
    
    
