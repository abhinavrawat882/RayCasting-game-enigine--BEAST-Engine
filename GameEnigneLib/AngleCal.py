############################################################################

#         ##ABSOLUTE CORDINATE to screed CONVERSTION

############################################################################
def CorToSrc(x, y, ylen):

    i = ylen-1-y
    return(x, i)
############################################################################

#         ##MATRIX TO ABSOLUTE CORDINATE CONVERSTION

############################################################################


def CorToMat(x, y, ylen):
    j = x
    i = ylen-1-y
    return(i, j)

############################################################################

#         ##MATRIX TO ABSOLUTE CORDINATE CONVERSTION

############################################################################


def MatToCor(i, j, ylen):

    x = j
    y = ylen-1-i
    return (x, y)


def giveAbsAngle(angle):
    if(angle < 0):
        return 360+angle
    elif(angle > 359):
        return angle-360
    return angle
