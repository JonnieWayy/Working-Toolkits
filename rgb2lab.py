from PIL import ImageCms

class ColorTrans:

    '''Class for transforming RGB<->LAB color spaces for PIL images.'''
    
    def __init__(self):
        self.srgb_p = ImageCms.createProfile("sRGB")
        self.lab_p  = ImageCms.createProfile("LAB")
        self.rgb2lab_trans = ImageCms.buildTransformFromOpenProfiles(self.srgb_p, self.lab_p, "RGB", "LAB")
        self.lab2rgb_trans = ImageCms.buildTransformFromOpenProfiles(self.lab_p, self.srgb_p, "LAB", "RGB")
    
    def rgb2lab(self, img):
        return ImageCms.applyTransform(img, self.rgb2lab_trans)

    def lab2rgb(self, img):
        return ImageCms.applyTransform(img, self.lab2rgb_trans)
