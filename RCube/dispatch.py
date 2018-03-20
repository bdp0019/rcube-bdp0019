import RCube

def dispatch(parm={}):
    if(not('op' in parm)):
        return {'status':'error: missing op'}
    
    if(not('op' == 'scramble')):
        return {'status':'error: missing op'}
    
    if('op' == 'scramble'):
        return RCube.scramble(3)
    return parm