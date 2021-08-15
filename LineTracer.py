import math
def lineTracer(y,x,LineAngle,levelMap):
  lineTangent=math.tan(angle)
  
  delx=x-int(x)
  dely=y-int(y)
  
  lineTraceStat=0
  
  while lineTraceStat==0:
    
    isYInterceptSucess=0
    
    
    ##Calculate Y intercept 
    if  LineAngle<90 or LineAngle>0:
      
        if dely !=0:
            b=dely/lineTangent
        else:
            b=1/lineTangent
     else:
        b=(1-del)/lineTangent
        
     if delx+b==1v
        
    
      
      
      
      
    
    ## CAlculate x if y not found
    
    
