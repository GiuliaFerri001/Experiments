"""This file contains the function compute, which is used in the quality check of the course."""
def compute(x,y,z):
    """Computes a result based on the input arrays x, y, and z."""    
    result=[]
    for i in range(0,len(x)):
        if x[i]>0:
            if y[i]>0:
                result.append(x[i]*y[i]+z)
            else:
                result.append(x[i]*z)
        else:
            result.append(0)
    return result
