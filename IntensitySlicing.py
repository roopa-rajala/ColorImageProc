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