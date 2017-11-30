from scipy import ndimage
import math
import numpy as np
import cv2
class Smoothing:
    def get_gaussian_low_pass_filter(self, shape, sig):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""
        p = shape[0]
        q = shape[1]
        mask = np.zeros((p, q))
        for u in range(p):
            for v in range(q):
                h = (math.exp(-(((u-(p-1)/2)*(u-(p-1)/2) + (v-(q-1)/2)*(v-(q-1)/2)) / ( 2*sig * sig)))) / (2* math.pi *sig * sig)

                mask[u][v] = h
        print(mask)
        # k = (1 / 16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        # k=(1/273)*np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])
        # print(k)

        return mask

    def get_gaussian_high_pass_filter(self, shape, sig):
        k = (1 / 273) * np.array(
            [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]])
        print(k)
        return k

    def blurring(self,image):
        image = cv2.imread(image)
        b, g, r = cv2.split(image)
        k=self.get_gaussian_low_pass_filter(self,[4,4],2)
        # ndimage.convolve(r, k, mode='constant', cval=1.0)
        # cv2.imshow("image", r)
        # cv2.waitKey(0)
        a = np.array([[1, 2, 0, 0],[5, 3, 0, 4],[0, 0, 0, 7],[9, 3, 0, 0]])
        # k = (1/16)*np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        # t = np.linspace(-10, 10, 30)
        # bump = np.exp(-0.1 * t ** 2)
        # bump /= np.trapz(bump)  # normalize the integral to 1
        #
        # # make a 2-D kernel out of it
        # kernel = bump[:, np.newaxis] * bump[np.newaxis, :]
        blur_red=ndimage.convolve(r, k, mode='constant', cval=0.0)
        blur_blue = ndimage.convolve(b, k, mode='constant', cval=0.0)
        blur_green = ndimage.convolve(g, k, mode='constant', cval=0.0)
        # blurred_face = ndimage.gaussian_filter(image, sigma=3)
        blur = cv2.merge((blur_blue,blur_green, blur_red))
        cv2.imwrite("test.png", blur)
        return blur
    def sharpening(self,image):
        # image=self.blurring(self,image)
        image = cv2.imread(image)
        b, g, r = cv2.split(image)
        e= np.zeros((np.shape(b)[0],np.shape(b)[1]))
        e[int(np.shape(b)[0]/2)][int(np.shape(b)[1]/2)]=1
        k = self.get_gaussian_high_pass_filter(self, [5, 5], 3)
        blur_red = ndimage.convolve(r, k, mode='constant', cval=0.0)
        blur_blue = ndimage.convolve(b, k, mode='constant', cval=0.0)
        blur_green =  ndimage.convolve(g, k, mode='constant', cval=0.0)
        # blurred_face = ndimage.gaussian_filter(image, sigma=3)
        blur = cv2.merge((blur_blue, blur_green, blur_red))
        sharpen= image + 1*(image - blur)
        cv2.imwrite("test.png", sharpen)
        return sharpen