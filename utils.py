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

def get_coords_at_raduis(centerx, centery, radius):
    XB = []
    YB = []
    return XB, YB