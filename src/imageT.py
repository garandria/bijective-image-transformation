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

    def _period(self, fct_transformation):
        """
        """
        pass

    def cycle(self, fct_transformation):
        """
        """
        pass
        
        
    def original(self, fct_transformation):
        """
        """
        
