import json

def load_data(fname):
    """
    Load the 3D points from the given file.

    The plot library wants the list of 3D points separated
    into 3 lists -- one for X, one for Y, and one for Z.

    Args:
        fname (string): The name of the JSON file to load.

    Returns
        tuple: Separate lists for X, Y, and Z coordinates
    """

    with open(fname) as f:
        data = json.load(f)

    xdata = []
    ydata = []
    zdata = []
    
    for x,y,z in data:
        xdata.append(x)
        ydata.append(y)
        zdata.append(z)

    return xdata,ydata,zdata