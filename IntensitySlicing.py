import cv2
import numpy as np
import math
class IntensitySlicing:
    def scale(self,image, cuttoff):
        image = cv2.imread(image,0)
        r=np.shape(image)[0]
        c=np.shape(image)[1]
        b = np.zeros((r,c,3))
        for i in range(0,r):
            for j in range(0,c):
                if image[i][j] < 38 and image[i][j] > 0:
                    b[i][j] = [0, 0, 0]
                if image[i][j] < 68 and image[i][j] >= 38:
                    b[i][j] = [255, 0, 255]
                if image[i][j] < 97 and image[i][j] >= 68:
                    b[i][j] = [255, 0, 0]
                if image[i][j] < 136 and image[i][j] >= 97:
                    b[i][j] = [255, 255, 0]
                if image[i][j] < 164 and image[i][j] >= 136:
                    b[i][j] = [0, 255, 0]
                if image[i][j] < 193 and image[i][j] >= 164:
                    b[i][j] = [0, 255, 171]
                if image[i][j] < 221 and image[i][j] >= 193:
                    b[i][j] = [0, 255, 255]
                if image[i][j] < 250 and image[i][j] >= 221:
                    b[i][j] = [0, 0, 255]

                if image[i][j] < 256 and image[i][j] >= 250:
                    b[i][j] = [255, 255, 255]

        # cv2.imshow("image", b)
        # cv2.waitKey(0)
        cv2.imwrite("test.png ",b)
        return b

    def transform(self, image):
        image = cv2.imread(image, 0)
        fft_image = np.fft.fft2(image)
        shift_image = np.fft.fftshift(fft_image)
        dftfinalmag = np.uint8(np.log(np.absolute(shift_image)) * 10)
        mask = self.get_gaussian_low_pass_filter(self, np.shape(image), 100)
        filter_image = shift_image * mask
        mask = self.get_gaussian_low_pass_filter(self, np.shape(image), 110)
        lowpass = shift_image * mask
        mask = self.get_gaussian_high_pass_filter(self, np.shape(image), 100)
        bandpass = filter_image * mask
        mask = self.get_gaussian_high_pass_filter(self, np.shape(image), 110)
        highpass = shift_image * mask
        # filtermaglow = np.log(np.absolute(lowpass)) * 10
        # filtermaghigh = np.log(np.absolute(highpass)) * 10
        # filtermaglow = np.log(np.absolute(bandpass)) * 10
        ishift_imagelow = np.fft.ifftshift(lowpass)
        ifft_imagelow = np.fft.ifft2(ishift_imagelow)
        ishift_imagehigh = np.fft.ifftshift(highpass)
        ifft_imagehigh = np.fft.ifft2(ishift_imagehigh)
        ishift_imageband = np.fft.ifftshift(bandpass)
        ifft_imageband = np.fft.ifft2(ishift_imageband)

        newr = self.post_process_image(self, np.absolute(ifft_imagelow))
        newg = self.post_process_image(self, np.absolute(ifft_imageband))
        newb = self.post_process_image(self, np.absolute(ifft_imagehigh))
        finalimage = cv2.merge((newb, newg, newr))
        cv2.imwrite("test.png ", finalimage)
        return finalimage

    def get_gaussian_high_pass_filter(self, shape, cutoff):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        # Hint: May be one can use the low pass filter function to get a high pass mask
        p = shape[0]
        q = shape[1]
        mask = np.zeros((p, q))
        for u in range(p):
            for v in range(q):
                d = math.sqrt((u - (p - 1) / 2) * (u - (p - 1) / 2) + (v - (q - 1) / 2) * (v - (q - 1) / 2))
                h = math.exp(-(d * d) / (2 * cutoff * cutoff))

                mask[u][v] = 1 - h

        # cv2.imshow("Image", mask)
        # cv2.waitKey(0)

        return mask

    def get_gaussian_low_pass_filter(self, shape, cutoff):
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
                d = math.sqrt((u - (p - 1) / 2) * (u - (p - 1) / 2) + (v - (q - 1) / 2) * (v - (q - 1) / 2))
                h = math.exp(-(d * d) / (2 * cutoff * cutoff))

                mask[u][v] = h

        # cv2.imshow("Image", mask)
        # cv2.waitKey(0)

        return mask

    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage)
        """
        a = 0
        b = 255
        c = np.min(image)
        d = np.max(image)
        # print(c, d)
        display = np.zeros((np.shape(image)[0], np.shape(image)[1]), dtype="uint8")
        for i in range(0, np.shape(image)[0]):
            for j in range(0, np.shape(image)[1]):
                display[i][j] = (image[i][j] - c) * ((b - a) / (d - c)) + a

        return display