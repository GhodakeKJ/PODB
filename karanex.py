#karanex.py File Name Acts As Module Name
from userdefineexc import KaranDivisionError
def division(a,b):
    if(b==0):
        raise KaranDivisionError
    else:
        c=a/b
        return c