"""
"""

from PIL import Image

class imageT:
    """

    """

    def __init__ (self, image):
        """
        
        """
        self.__img = Image.open(image)
        self.__name = image
        self.__width = self.__img.size[0]
        self.__height = self.__img.size[1]

    def transform(self, fct_transformation):
        """
        Apply the transformation on the image
        :parameter: a transformation
        :type: function
        """
        img1 = Image.new(self.__img.mode, self.__image.size)
        if self.__img.mode == 'P':
            img1.putpalette(self.__img.getpalette())
        for y in range(self.__height):
            for x in range(self.__width):
                img1.putpixel((
                    fct_transformation((x, y), self.__img.size)),
                    self.__image.getpixel((x, y)))
        img1.save('transformated.png')
        img1.close()

    def __period(self, coord, fct_transformation):
        """
        """
        cpt = 1
        x, y = coord
        res = set()
        x1, y1 = transfo((x, y), (self.__width, self.__height))
        while (x1, y1) != (x, y):
            cpt += 1
            res.add((x1, y1))
            x1, y1 = transfo((x1, y1), (self.__width, self.__height))
        return (res, cpt)
            
            
    def __cycle_l(self, fct_transformation):
        """
        """
        l = [[-1 for i in range (self.__width)]\
             for j in range (self.__height)]
        for y in range(self.__height):
            for x in range(self.__width):
                if l[x][y] == -1:
                    coords, p = _period((x, y), fct_transformation)
                    for c in coords:
                        x1, y1 = c
                        l[x1][y1] = p
        return l
        
        
    def original(self, fct_transformation):
        """
        """
        
