def maximum (x,y):
    if (x>y):
        return x
    else:
        return y

def complete(a):
    aux =[0, a[0]]
    for i in range(2,len(a)-1,1):
        aux.append(maximum(aux[i-1],aux[i-2]+a[i-1]))
    return aux

 
def mount(a, aux):
    s = []
    ind = len(aux)-1
    while (ind >= 1):
        if (a[ind-1] >= a[ind-2]+a[ind-1]):
            ind-=1
        else:
            s.append(aux[ind])
            ind-=2
    return s

def mwis(a):
    return(mount(complete(a),a))
    
