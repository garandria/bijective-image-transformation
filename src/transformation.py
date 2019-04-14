"""
Transformation functions
"""

def boulanger (coord, dim):
    """
    Compute the new coordinate of the pixel after one step of 
    the transformation
    :parameter: coordinate of the pixel like (x, y)
    :type: tuple
    :parameter: the dimension of the image like (height, width)
    :type: tuple
    :return: the new coordinate of the pixel 
    :rtype: tyuple        
    What we are trying to do :  
+---+---+---+---+                                                            +---+---+---+---+
|X  |X  |X  |X  |                                                            |X  |0  |X  |0  |
+---+---+---+---+             +---+---+---+---+---+---+---+---+              +---+---+---+---+
|0  |0  |0  |0  | (etirement) |X  |0  |X  |0  |X  |0  |X  |0  | (repliement) |X' |0' |X' |0' |
+---+---+---+---+   ------>   +---+---+---+---+---+---+---+---+   ------->   +---+---+---+---+
|X' |X' |X' |X' |             |X' |0' |X' |0' |X' |0' |X' |0  |              |0  |X  |0  |X  |   
+---+---+---+---+             +---+---+---+---+---+---+---+---+              +---+---+---+---+ 
|0' |0' |0' |0' |                                                            |0' |X' |0' |X' |
+---+---+---+---+                                                            +---+---+---+---+

    Exemples:
    
    >>> from random import shuffle
    >>> from random import randint
    >>> lp = [p for p in range (1000) if p & 1 == 0]
    >>> shuffle(lp)
    >>> l = lp[randint(0, len(lp)-1)]
    >>> boulanger( (0, 0), (l, l) )
    (0, 0)
    >>> larg = lp[randint(0, len(lp)-1)]
    >>> haut = larg
    >>> d = larg, haut
    >>> c =  larg - 1, haut - 1
    >>> boulanger( c, d ) == (0, haut/2) # (1)
    True

    (1) Soient x0, y0 deux entiers dans l'intervalle [0; a0[ et [0; b0[, tel que x0 = a0 - 1, y0 = b0 - 1
    x1, y1 = 2x0 + 1, y0 // 2
    
 -  x2, y2 = 2 * a0 - 1 - (2*x0 + 1) , b0 - 1 - ( y0 // 2 )
    x2 = 2 * a0 - 2*x0 - 1 - 1
       = 2 * ( a0 - x0 - 1), or x0 = a0 - 1
       = 2 * ( x0 - x0)
    x2 = 0
 -  y2 = b0 - 1 - ( y0 // 2), comme b0 - 1 = y0,on a:
    y2 = y0 ( 1 - 1/2 )
    y2 = y0 / 2
    Donc, pour tout a0, b0 pairs, le dernier pixel en bas à droite a pour coordonnées, apres transformation: (0, b0/2)
    soit (0, hauteur/2) ( 'hauteur' car il y a b0 pixels entre 0 et y0 ) 
    """
    x, y = coord
    larg, haut = dim
    assert 0 <= x < larg and 0 <= y < haut, 'Invalid coordinate'
    assert larg & 1 == 0 and haut & 1 == 0, 'Invalid dimention'
    # This first version only deals with dimension like (x, y)
    # such as x == y and x even
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    #REPLIEMENT
    if y & 1 == 0:
        x1, y1 = 2*x, y/2
    else:
        x1, y1 = 2*x+1, y//2
    #ETIREMENT
    if x1 < larg:
        x2, y2 = x1, y1
    else:
        x2, y2 = 2*haut - 1 - x1, larg - 1 - y1
    return int(x2), int(y2)

def photomaton(coord, dim):
    """
    Compute the new coordinate of the pixel after one step of 
    the transformation
    :parameter: coordinate of the pixel like (x, y)
    :type: tuple
    :parameter: the dimension of the image like (height, width)
    :type: tuple
    :return: the new coordinate of the pixel 
    :rtype: tyuple        

    Exemples:
    >>> from random import shuffle
    >>> from random import randint
    >>> lp = [p for p in range (1000) if p & 1 == 0]
    >>> shuffle(lp)
    >>> l = lp[randint(0, len(lp)-1)]
    >>> boulanger( (0, 0), (l, l) )
    (0, 0)
    >>> larg =  lp[randint(0, len(lp)-1)]
    >>> haut = larg
    >>> d = larg, haut
    >>> x, y = randint(0, d[0]), randint(0, d[1])
    """
    x, y = coord
    larg, haut = dim
    assert 0 <= x < larg and 0 <= y < haut, 'Invalid coordinate'
    assert larg & 1 == 0 and haut & 1 == 0, 'Invalid dimension'
    x1, y1 = 0, 0
    if x & 1 == 0 and y & 1 == 0:
        x1, y1 = x/2, y/2
    elif x & 1 == 0 and y & 1 != 0:
        x1, y1 = x/2, y//2 + larg/2
    elif x & 1 != 0 and y & 1 == 0:
        x1, y1 = x//2 + haut/2, y/2
    else:
        x1, y1 = x//2 + haut/2, y//2 + larg/2
    return int(x1), int(y1)

def boustrophedon(coord, dim):
    """
    Compute the new coordinate of the pixel after one step of 
    the transformation
    :parameter: coordinate of the pixel like (x, y)
    :type: tuple
    :parameter: the dimension of the image like (height, width)
    :type: tuple
    :return: the new coordinate of the pixel 
    :rtype: tyuple        

    Exemples:
    >>> from random import shuffle
    >>> from random import randint
    >>> lp = [p for p in range (1000) if p & 1 == 0]
    >>> larg = lp[randint(0, len(lp)-1)]
    >>> haut = lp[randint(0, len(lp)-1)]
    >>> dim = larg, haut
    >>> boustrophedon ( (0, 0), dim )
    (1, 0)
    >>> boustrophedon ( (larg - 1, 0), dim) == (larg - 1, 1)
    True
    >>> boustrophedon ( (larg - 1, 0), dim) == (larg - 1, 1)
    True
    >>> boustrophedon ( (larg - 1, haut - 1), dim) == (larg - 2, haut - 1)
    True

    """
    x, y = coord
    larg, haut = dim
    assert 0 <= x < larg and 0 <= y < haut, 'Invalid coordinate'
    assert larg & 1 == 0 and haut & 1 == 0, 'Invalid dimension'
    x1, y1 = 0, 0
    if y & 1 == 0:
        if x == larg - 1:
            x1, y1 = x, (y + 1) % haut
        else:
            x1, y1 = x + 1, y
    else:
        if x == 0:
            x1, y1 = x, (y + 1) % haut
        else:
            x1, y1 = x - 1, y
    return x1, y1

def concentrique ( coord, dim ):
    """
    Compute the new coordinate of the pixel after one step of 
    the transformation
    :parameter: coordinate of the pixel like (x, y)
    :type: tuple
    :parameter: the dimension of the image like (height, width)
    :type: tuple
    :return: the new coordinate of the pixel 
    :rtype: tyuple        

    Exemples:
    >>> from random import randint
    >>> lp = [n for n in range (1000) if n & 1 == 0]
    >>> larg = lp[randint(0, len(lp)-1)]
    >>> dim = larg, larg
    >>> concentrique( (0, 0), dim )
    (1, 0)
    >>> concentrique( (larg - 1, 0), dim ) == (larg - 1, 1)
    True
    >>> concentrique( (larg - 1, larg -1), dim) == (larg - 2, larg - 1)
    True
    >>> concentrique( (0, larg - 1), dim ) == (0, larg - 2)
    True
    """
    x, y = coord
    larg, haut = dim
    assert 0 <= x < larg and 0 <= y < haut, 'Invalid coordinate'
    assert larg & 1 == 0 and haut & 1 == 0, 'Invalid dimention'
    x1, y1 = 0, 0
    if x >= larg/2 and x == y :
        x1, y1 = x - 1, y
    elif x - y >= 0 :
        if x + y < larg - 1:
            x1, y1 = x + 1, y
        else:
            x1, y1 = x, y + 1
    else:
        if x + y <= larg - 1:
            x1, y1 = x, y - 1
        else:
            x1, y1 = x - 1, y
    return x1, y1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
