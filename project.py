def Geometric_mean(a,b):
    if type(a) not in [int,float]:
        raise TypeError("type is incorrect")
    if a < 0 or b < 0:
        return "one argument is negative"
    return (a * b) ** 0.5
