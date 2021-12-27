import GameEnigneLib.AngleCal as ac
import math
rd = 0.0174533


def checkY(x, y, Levelmap,a,inte):
    #print("Intercept : ",inte)
    x = int(x)
    #print("ABS Y : ",y)
    y = len(Levelmap)-1-y
    y=int(y)

    #print("MAT Y :",y)
    if(inte==0):
        if(a<180 and a>0):
            y-=1

        #else:
        #    y+=1
    if(inte==1):
        if(a>90 and a<270):
            x-=1
    elif(inte==2):
        if(a<90 and a>0):
            y-=1
        elif(a>90 and a<180):
            y-=1
            x-=1
        elif(a>180 and a<270):
            x-=1
        elif(a<360 and a>270):
            y==y
    #if(inte==2):
        #print("Intercept")
    #print("MatLoc :")
    #print( y,x)
    try:
        if(Levelmap[y][x] == 1):
            return True
        else:
            return False
    except:
        print("Exception occured")
        print("loc :",x,y)
        print("Angle ",a)
        return True


def lineTracer(x, y, lineAngle, Levelmap):  # 4.0
    #print("Player Position")
    #print("X: ", x, " Y: ", y, " ANGLE: ", lineAngle)
    
    dely = 0
    delx = 0
    mdy = y % 1
    mdx = x % 1
    if(lineAngle==0,lineAngle==45,lineAngle==90,lineAngle==135,lineAngle==180,lineAngle==225,lineAngle==270,lineAngle==315):
        lineAngle+=0.0001
    rlineA=lineAngle*math.pi/180
    dy = math.sin(rlineA)
    dx = math.cos(rlineA)
    
    if(lineAngle > 0 and lineAngle < 90):
        
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0
    elif(lineAngle > 90 and lineAngle < 180):
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
        else:
            delx = 0
    elif(lineAngle > 180 and lineAngle < 270):
        if(mdy > 0):
            dely = -1*(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
        else:
            delx = 0
    elif(lineAngle > 270 and lineAngle < 360):
        if(mdy > 0):
            dely = -1*(y % 1)

        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0
    #print("Initial Delta :")
    #print("DX: ", delx, " DY: ", dely)
    lineLen = 0

    llpy =abs( 1/math.sin(rlineA))
    llpx = abs(1/math.cos(rlineA))

    #print("llpy:  ", llpy, "  llpx: ", llpx, "  dy: ", dy, "  dx: ", dx,)
    tllpy = abs(llpy*dely)
    tllpx = abs(llpx*delx)
    intercept=-1
    while True:
        if(tllpy < tllpx):
            lineLen += tllpy
            tllpx -= tllpy


            x += tllpy*dx
            y += tllpy*dy
            tllpy = llpy
            intercept=0
        elif(tllpy > tllpx):
            lineLen += tllpx
            tllpy -= tllpx

            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            intercept=1
        else:
            lineLen += tllpx
            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            tllpy = llpy
            intercept=2
        #print("CRR")
        #print("X: ", x, " Y: ", y)
        
        if checkY(x, y, Levelmap,lineAngle,intercept):
            break

    #print("Line Length", lineLen)
    #print("Line Rendered")

    return lineLen,intercept,x,y

def lineTracerp(x, y, lineAngle, Levelmap):  # 4.0
    print("Player Position")
    print("X: ", x, " Y: ", y, " ANGLE: ", lineAngle)
    
    dely = 0
    delx = 0
    mdy = y % 1
    mdx = x % 1
    if(lineAngle==0,lineAngle==45,lineAngle==90,lineAngle==135,lineAngle==180,lineAngle==225,lineAngle==270,lineAngle==315):
        lineAngle+=0.01
    rlineA=lineAngle*math.pi/180
    dy = math.sin(rlineA)
    dx = math.cos(rlineA)
    
    if(lineAngle >= 0 and lineAngle < 90):
        
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0
    elif(lineAngle >= 90 and lineAngle < 180):
        if(mdy > 0):
            dely = 1-(y % 1)
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
            
        else:
            delx = 0
    elif(lineAngle >= 180 and lineAngle < 270):
        if(mdy > 0):
            dely = -1*(y % 1)
  
        else:
            dely = 0
        if(mdx > 0):
            delx = -1*(x % 1)
  
        else:
            delx = 0
    elif(lineAngle >= 270 and lineAngle < 360):
        if(mdy > 0):
            dely = -1*(y % 1)

        else:
            dely = 0
        if(mdx > 0):
            delx = 1-(x % 1)
        else:
            delx = 0
    print("Initial Delta :")
    print("DX: ", delx, " DY: ", dely)
    lineLen = 0

    llpy =abs( 1/math.sin(rlineA))
    llpx = abs(1/math.cos(rlineA))

    print("llpy:  ", llpy, "  llpx: ", llpx, "  dy: ", dy, "  dx: ", dx,)
    tllpy = abs(llpy*dely)
    tllpx = abs(llpx*delx)
    intercept=-1
    while True:
        if(tllpy < tllpx):
            lineLen += tllpy
            tllpx -= tllpy
            x += tllpy*dx
            y += tllpy*dy
            tllpy = llpy
            intercept=0
        elif(tllpy > tllpx):
            lineLen += tllpx
            tllpy -= tllpx

            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            intercept=1
        else:
            lineLen += tllpx
            x += tllpx*dx
            y += tllpx*dy
            tllpx = llpx
            tllpy = llpy
            intercept=2
        print("CRR")
        print("X: ", x, " Y: ", y)
        
        if checkY(x, y, Levelmap,lineAngle,intercept):
            break

    print("Line Length", lineLen)
    print("Line Rendered")

    return lineLen,intercept,x,y


def threDRenderer(x, y, a, surface, mp, pygame):
    # Define Variable :-
    gh = 480
    gw = 480
    FOV = 44
    
    EndAngle = ac.giveAbsAngle(a+FOV)
    naea=a+FOV
    AngularStep = (FOV*2)/gh
    PlayerHeight = 0
    center = (gh/2)-1

    ############################################
    #             FRAME DRAWING
    ###########################################

    for i in range(480, 480*2):

        ###########################################
        # .    Get line length
        ###########################################
        
        la = EndAngle
        la = ac.giveAbsAngle(la)
        #print("Line Angle :",la)
        ln,inter,xe,ye = lineTracer(x, y, la, mp)

        ###########################################
        # .    Get perpendicular length
        ###########################################
        angleBeetweenLines = 0
        if(naea>a):
            angleBeetweenLines=naea-a
        elif(naea<a):
            angleBeetweenLines=a-naea

        #print("Angle Beetween  :",angleBeetweenLines)
        ln = ln*math.cos(angleBeetweenLines*rd)
        ln *= 2

        ###########################################
        # height calculation
        ###########################################
        try:
            height = gh/(ln)
        except:
            height=gh
        # print(height)

        ###########################################
        # Draw Column
        ###########################################
        sy = 0
        ey = 0
        if(height >= gh):
            sy = 0
            ey = gh-1

        else:
            sy = center-(height/2)
            ey = center+(height/2)
        if(inter==0):
            pygame.draw.line(surface, (0, 0, 255), (i, sy), (i, ey))
        else:
            pygame.draw.line(surface, (0, 255, 255), (i, sy), (i, ey))
        EndAngle -= AngularStep
        naea-=AngularStep

# 2D Engine


def d2renderer(screen2d, x, y, a, pygame, mp):

    ################################
    #       RENDER MAP
    ################################
    factor = 480/16
    for i in range(len(mp)):
        for j in range(len(mp)):
            if(mp[i][j] == 1):
                pygame.draw.rect(screen2d, (10, 10, 255), pygame.Rect(
                    j*factor, i*factor, factor, factor))

    #####################################
    # Render player
    #####################################

    xi, yi = ac.CorToSrc(x, y, 16)
    pygame.draw.circle(screen2d, (225, 0, 0), (xi*factor, yi*factor), 5)

    #####################################
    #         Render Line
    #####################################

    # Calculate point of line
    
    #i=a-29
    #while(i<a+29):
    #    ln,inter,xe,ye = lineTracer(x, y, ac.giveAbsAngle(i), mp)
    #    endx, endy = ac.CorToSrc(xe, ye, 16)
    #    pygame.draw.line(screen2d, (255, 255, 255), (xi*factor,yi*factor), (endx*factor, endy*factor))
    #    i+=1
    ln,inter,xe,ye = lineTracer(x, y, a, mp)
    endx, endy = ac.CorToSrc(xe, ye, 16)
    pygame.draw.line(screen2d, (255, 255, 255), (xi*factor,yi*factor), (endx*factor, endy*factor))
    