import cv2
import numpy as np
import math
class ColorTransf():

    def RGBtoCMYK(filename):
        img = cv2.imread(filename)
        h, w, c = np.shape(img)
        cmyk_img=np.zeros((h,w,4),dtype="uint8")
        print(h,w,c)
        for i in range(h):
            for j in range(w):
                r = img[i][j][2]
                g = img[i][j][1]
                b = img[i][j][0]
                c =1 -r/255
                m = 1 - g/255
                y = 1 - b/255
                min_cmy = min(c,m,y)
                cmyk_img[i][j][0] = 100*(c-min_cmy)/(1-min_cmy)
                cmyk_img[i][j][1] = 100*(m - min_cmy) / (1 - min_cmy)
                cmyk_img[i][j][2] = 100*(y - min_cmy) / (1 - min_cmy)
                cmyk_img[i][j][3] = 100*min_cmy
        return cmyk_img
    # cv2.imshow("cmyk", cmyk_img)
    # cv2.waitKey(0)
    #
    # print(np.shape(cmyk_img))
    # h,w,c = np.shape(cmyk_img)
    #
    # rgb_img = np.zeros((h, w, 3), dtype="uint8")
    # for i in range(h):
    #     for j in range(w):
    #         c=cmyk_img[i][j][0]/100.0
    #         m=cmyk_img[i][j][1]/100.0
    #         y=cmyk_img[i][j][2]/100.0
    #         k=cmyk_img[i][j][3]/100.0
    #         rgb_img[i][j][2] = round(255.0 - ((min(1.0, c * (1.0 - k) + k)) * 255.0))
    #         rgb_img[i][j][1] = round(255.0 - ((min(1.0, m * (1.0 - k) + k)) * 255.0))
    #         rgb_img[i][j][0] = round(255.0 - ((min(1.0, y * (1.0 - k) + k)) * 255.0))
    # cv2.imshow("rgb",rgb_img)
    # cv2.waitKey(0)

    # row, col, c = np.shape(img)
    # hsv_img = np.zeros((row, col, 3), dtype="uint8")
    # print(row, col, c)
    # for i in range(row):
    #     for j in range(col):
    #         r = img[i][j][2] / 255.0
    #         g = img[i][j][1] / 255.0
    #         b = img[i][j][0] / 255.0
    #
    #         maxi = max(r, g, b)
    #         mini = min(r, g, b)
    #
    #         # RGB to HSV implemetation
    #         v = maxi
    #         delta = maxi - mini;
    #         if maxi == 0:
    #             r = 0
    #             g = 0
    #             b = 0
    #             s = 0
    #             h = -1
    #
    #         else:
    #             s = delta / maxi
    #             if r == maxi:
    #                 h = ((g - b) / delta) % 6
    #             elif g == maxi:
    #                 h = 2 + ((b - r) / delta)
    #             elif b == maxi:
    #                 h = 4 + (r - g) / delta
    #             if h < 0:
    #                 h = h + 360
    #             h = h / 6
    #         hsv_img[i][j][0] = h * 255
    #         hsv_img[i][j][1] = s * 255
    #         hsv_img[i][j][2] = v * 255
    #         # print(h, s, v)
    #
    # #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    # cv2.imshow("rgb_hsv", rgb)
    # cv2.waitKey(0)
    # min = hsv_img[0][0][0]
    # max = hsv_img[0][0][0]
    # print(np.shape(hsv_img))
    # row, col, c = np.shape(hsv_img)
    # rgb_img = np.zeros((row, col, 3), dtype="uint8")
    # for height in range(row):
    #     for width in range(col):
    #         val=hsv_img[height][width][0]
    #         if(val>max): max = val
    #         if(val<min): min = val
    # for height in range(row):
    #     for width in range(col):
    #         hsv_img[height][width][0]=360*(hsv_img[height][width][0]-min)/(max-min)
    #
    # for height in range(row):
    #     for width in range(col):
    #         h = hsv_img[height][width][0]
    #         s = hsv_img[height][width][1]
    #         v = hsv_img[height][width][2]
    #         i = math.floor(h * 6)
    #         s = s / 255.0
    #         v = v / 255.0
    #         # h = h/60
    #         # c = v * s
    #         # x = c * (1 - abs(h % 2 - 1))
    #         c = v * s
    #         #c = (1. - abs(2*v-1))*s
    #         x = c *(1-abs((h/60)%2-1))
    #         m = v - c
    #
    #         if h >=0 and h<60:
    #             r,g,b =c,x,0
    #         if h >=60 and h<120:
    #             r, g, b =x,c,0
    #         if h >=120 and h<180:
    #             r, g, b =0,c,x
    #         if h >=180 and h<240: r,g,b = 0,x,c
    #         if h >=240 and h<300: r,g,b =x,0,c
    #         if h >=300 and h<360: r,g,b =c,0,x
    #         r = (r+m)*255
    #         g = (g + m) * 255
    #         b = (b + m) * 255
    #         rgb_img[height][width][0] = r
    #         rgb_img[height][width][1] = g
    #         rgb_img[height][width][2] = b
    # # for height in range(row):
    # #     for width in range(col):
    # #         h = hsv_img[height][width][0]
    # #         s = hsv_img[height][width][1]
    # #         v = hsv_img[height][width][2]
    # #         i = math.floor(h * 6)
    # #         s = s/255.0
    # #         v = v/255.0
    # #         f = h * 6 - i
    # #         p = v * (1. - s)
    # #         q = v * (1. - f * s)
    # #         t = v * (1. - (1 - f) * s)
    # #         i%=6
    # #         if i == 0:
    # #             r,g,b =v, t, p
    # #         if i == 1:
    # #             r, g, b =q, v, p
    # #         if i == 2:
    # #             r, g, b =p, v, t
    # #         if i == 3: r,g,b = p, q, v
    # #         if i == 4: r,g,b =t, p, v
    # #         if i == 5: r,g,b =v, p, q
    # #         r = r * 255
    # #         g = g * 255
    # #         b = b * 255
    # #         # r, g, b = [
    # #         #     (v, t, p),
    # #         #     (q, v, p),
    # #         #     (p, v, t),
    # #         #     (p, q, v),
    # #         #     (t, p, v),
    # #         #     (v, p, q),
    # #         # ][int(i % 6)]
    # #         rgb_img[height][width][0]=b
    # #         rgb_img[height][width][1]=g
    # #         rgb_img[height][width][2]=r
    # # def calc(p, q, t):
    # #     if (t < 0):
    # #         t += 1
    # #     elif (t > 1):
    # #         t -= 1;
    # #     elif (t < 1 / 6):
    # #         return p + (q - p) * 6 * t;
    # #     elif (t < 1 / 2):
    # #         return q;
    # #     elif (t < 2 / 3):
    # #         return p + (q - p) * (2 / 3 - t) * 6;
    # #     return p;
    # #
    # # rgb_img = np.zeros((row, col, 3), dtype="uint8")
    # # for i in range(row):
    # #     for j in range(col):
    # #         # HSV to RGB
    # #         h = hsv_img[i][j][0] / 255.0
    # #         s = hsv_img[i][j][1] / 255.0
    # #         v = hsv_img[i][j][2] / 255.0
    # #
    # #         if s == 0:
    # #             r = g = b = v
    # #
    # #         else:
    # #
    # #             if v < 0.5:
    # #                 q = v * (1 + s)
    # #             else:
    # #                 q = v + s - v * s
    # #             p = 2 * v - q;
    # #
    # #             r = calc(p, q, h + 1 / 3)
    # #             g = calc(p, q, h)
    # #             b = calc(p, q, h - 1 / 3)
    # #
    # #             rgb_img[i][j][2] = int(r * 255)
    # #             rgb_img[i][j][1] = int(g * 255)
    # #             rgb_img[i][j][0] = int(b * 255)
    # #
    # # hsv = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    # cv2.imshow("hsv_rgb", rgb_img)
    # cv2.waitKey(0)