"""

"""

from math import gcd
from PIL import Image
from transformation import *

class imageT:
    """
    Image processing for bijective transformation class
    """

    def __init__ (self, image, fct_transformation):
        """
        Builds the object

        :parameter: an image
        :type: str
        """
        self.__img = Image.open(image)
        self.__name = image
        self.__width = self.__img.size[0]
        self.__height = self.__img.size[1]
        self.__transfo = fct_transformation

    def __period(self, coord):
        """
        Computes the step needed by the pixel to 
        come back at its original position

        :parameter: coordinate of the pixel
        :type: tuple
        :return: a period and every pixel that has the same period
        :rtype: tuple
        """
        cpt = 1
        x, y = coord
        res = set()
        x1, y1 = self.__transfo((x, y), (self.__width, self.__height))
        res.add((x, y))
        while (x1, y1) != (x, y):
            cpt += 1
            # Adding the pixels that are in the same cycle to avoid
            # computing them again.
            res.add((x1, y1))
            x1, y1 = self.__transfo((x1, y1), (self.__width, self.__height))
        return (res, cpt)
            
            
    def __cycle_l(self):
        """
        Computes the period of every pixel of the image

        """
        l = [[-1 for i in range (self.__width)]\
             for j in range (self.__height)]
        for y in range(self.__height):
            for x in range(self.__width):
                if l[y][x] == -1:
                    coords, p = self.__period((x, y))
                    for c in coords:
                        x1, y1 = c
                        l[y1][x1] = p
        return l

    @staticmethod
    def lcm(n, m):
        """
        Computes the least common divisor of two integers

        :parameter: an integer
        :type: int
        :parameter: an integer
        :type: int
        :return: least common divisor
        :rtype: int
        """
        return n * m // gcd(n, m)
        
    def stepsToOriginal(self):
        """
        Computes the steps to transform the image to come back
        to the original image with a transformation

        :return: steps to have the original image back
        :rtype: int
        """
        tmpl = self.__cycle_l()
        periods = {tmpl[y][x] for y in range(self.__height)\
                   for x in range(self.__width)}
        print(periods)
        res = 1
        for e in periods:
            res = imageT.lcm(res, e)
        return res

    def __transform(self, steps):
        """
        Apply the transformation on the pixels n times
        
        :return: new matrix with the transformation
        :rtype: list
        """
        l = self.__cycle_l()
        for y in range(self.__height):
            for x in range(self.__width):
                tmp = (x, y)
                nb_t = steps % l[y][x]
                for c in range (nb_t):
                    tmp = self.__transfo(tmp, (self.__width, self.__height))
                l[y][x] = tmp
        return l

    def draw(self, steps):
        nimage_l = self.__transform(steps)
        img1 = Image.new(self.__img.mode, self.__img.size)
        if self.__img.mode == 'P':
            img1.putpalette(self.__img.getpalette())
        for y in range(self.__height):
            for x in range(self.__width):
                img1.putpixel(
                    nimage_l[y][x],
                    self.__img.getpixel((x, y)))
        img1.save('images/transformated.png')
        img1.show()
        img1.close()
