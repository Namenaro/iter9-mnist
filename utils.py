def get_sensory_array(pic, centerx, centery, side):
    xmin = centerx - int(side / 2)
    ymin = centery - int(side / 2)
    xmax = xmin +side
    ymax = ymin + side

    xlen = pic.shape[1]
    ylen = pic.shape[0]
    if xmin >=0 and ymin>=0 and xmax <=xlen and ymax <= ylen:
        return pic[ ymin:ymax, xmin:xmax]
    return None

def get_coords_less_or_eq_raduis(centerx, centery, radius):
    XB = []
    YB = []
    for r in range(0, radius+1):
        X, Y = get_coords_for_radius(centerx, centery, r)
        XB = XB + X
        YB = YB + Y
    return XB, YB

def get_coords_for_radius(centerx, centery, radius):
    #x+y=radius ->  y=radius-x
    X=[]
    Y=[]
    for x in range(0,radius+1):
        y=radius-x
        X.append(x+centerx)
        Y.append(y+centery)
    return X,Y