# 图片信息压缩

import cv2
import numpy as np

path = ".\\pic.png"


def processor(imgPath):
    imgraw = cv2.imread(imgPath)
    # imgRGB = cv2.cvtColor(imgraw, cv2.COLOR_BGR2RGB)
    height = imgraw.shape[0]
    width = imgraw.shape[1]
    # print(height,width)
    newheight = height //2 *2
    newwidth = width //2 *2
    
    imgResized = imgraw[:newheight, :newwidth]
    imgR, imgG, imgB = colorAvg(imgResized)

    

    imgHex = np.zeros((int(newheight/2), int(newwidth/2)), dtype='U7')
    for row in range(newheight//2):
        for col in range(newwidth//2):
            color = '#{:02x}{:02x}{:02x}'.format(int(float(imgR[row][col])), int(float(imgG[row][col])), int(float(imgB[row][col])))
            imgHex[row][col] = color
        
    return [imgHex, newheight, newwidth]
    

def colorAvg(img: np.ndarray):
    
    height = img.shape[0]
    width = img.shape[1]
    # print(height/2, width/2)
    imgcAvg = np.zeros((int(height/2), int(width/2)))
    # imgcAvg = [[f'{i}' for i in range(int(width/2))] for i in range(int(height/2))]
    # print(imgcAvg[int(height/2)-1][0])
    imgR = np.zeros((int(height/2), int(width/2)))
    imgG = np.zeros((int(height/2), int(width/2)))
    imgB = np.zeros((int(height/2), int(width/2)))
    
    for row in range(0, height-1, 2):
        for col in range(0, width-1, 2):
            block = img[row:row+1, col:col+1]
            
            # deepSeek告诉我的可以减少颜色失真的方法，不过好像没什么用...
            luminance = 0.299*block[:,:,2] + 0.587*block[:,:,0] + 0.114*block[:,:,1]
            weight = luminance / np.sum(luminance) if float(np.sum(luminance)) > 0 else np.ones_like / luminance.size
            
            weighedR = int(float(np.sum(block[:,:,2] * weight)))
            weighedG = int(float(np.sum(block[:,:,0] * weight)))
            weighedB = int(float(np.sum(block[:,:,1] * weight)))
            # print(col//2, row//2)
            imgR[row//2][col//2] = weighedR
            imgG[row//2][col//2] = weighedG
            imgB[row//2][col//2] = weighedB
            # print(imgcAvg[row//2][col//2])
    
    return imgR, imgG, imgB
            
if __name__ == "__main__":
    imgHex = processor(path)
    print(imgHex)
