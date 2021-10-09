# it is only an uncompleted demo for the refactoring 
# because of the dataset format and still need to improve the accuracy 
import cv2
import numpy as np
import os

def readImg(imagePath: str, imageName: str, imageNum = 1):
    imgList = []
    if len(imageName)!=0:
        print("2")
        img = cv2.imread(imagePath + "/" + imageName)
        imgList.append(img)
        print(imagePath + "/" + imageName)
    
    else:
        for filename in os.listdir(imagePath):
            if imageNum == 0:
                break
            else:
                imageNum = imageNum - 1
                print("1")
                img = cv2.imread(imagePath + "/" + filename)
                imgList.append(img)
    return imgList

def showImg(imgName: str, img):
    imgSave = imgName+".jpg"
    cv2.imwrite(imgSave,img)
    # cv2.imshow(imgName,img)
    # cv2.waitKey(0)

def colorRange():
    upperList = []
    lowerList = []
    blackLower = np.array([0, 0, 0])
    lowerList.append(blackLower)
    blackUpper = np.array([188, 255, 46])
    upperList.append(blackUpper)
    purpleLower = np.array([125, 43, 46])
    lowerList.append(purpleLower)
    purpleUpper = np.array([155, 255, 255])
    upperList.append(purpleUpper)
    redLower = np.array([156, 43, 46])
    lowerList.append(redLower)
    redUpper = np.array([179, 255, 255])
    upperList.append(redUpper)
    orangeLower = np.array([11, 43, 46])
    lowerList.append(orangeLower)
    orangeUpper = np.array([25, 255, 255])
    upperList.append(orangeUpper)
    yellowLower = np.array([26, 43, 46])
    lowerList.append(yellowLower)
    yellowUpper = np.array([34, 245, 255])
    upperList.append(yellowUpper)
    whiteLower = np.array([0, 0, 221])
    lowerList.append(whiteLower)
    whiteUpper = np.array([180, 30, 255])
    upperList.append(whiteUpper)
    
    return lowerList, upperList

def imgResize(img1,img2):
    height, width, channel = img2.shape
    newH = int(1.2 * width)
    newW = int(1.2 * height)
    img = cv2.resize(img1,(newH, newW))
    return img

def separateByColor(img, lowerList, upperList):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgColorArea = []
    for (lower,upper) in zip(lowerList, upperList):
        mask = cv2.inRange(hsv, lower, upper)
        ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)    
        dilation = cv2.erode(binary, kernel, iterations=1)
        dilation = cv2.dilate(binary, kernel, iterations=3)
        dilation = cv2.erode(binary, kernel, iterations=2)
        dilation = cv2.dilate(binary, kernel, iterations=3)
        dilation = cv2.erode(binary, kernel, iterations=2)
        imgColorArea.append(dilation)
    return imgColorArea

def showCounters(img, printFlag = False):
    contours, hierarchy=cv2.findContours(img , cv2.RETR_TREE ,  cv2.CHAIN_APPROX_NONE )
    if printFlag == 1 :
        cv2.drawContours(img, contours, -1, (255,0,0),2) 
        showImg("counter",img)
    return contours, img


def edge_demo(img):
    image = np.copy(img)
    kernel = np.ones((3, 3), np.uint8)    

    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=3)
    image = cv2.erode(image, kernel, iterations=2)
    image = cv2.dilate(image, kernel, iterations=3)
    image = cv2.erode(image, kernel, iterations=1)
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
    # Y Gradient
    ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv2.Canny(gray, 50, 150)
    showImg('Canny Edge', edge_output)
    return edge_output
 
 
def contours_demo(image, width = 2 ):
    # dst = cv.GaussianBlur(image, (3, 3), 0)
    # gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow('binary image', binary)
    binary = edge_demo(image)
    contours, heriachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv2.drawContours(image, contours, i, (0, 0, 255), width)
        print(i)
    showImg('detect contours', image)

def main():
    imgName = "DJI_0001.JPG"
    imgList = readImg("../Riffle pool extraction/5月29金华/100MEDIA","",imageNum = 2)
    index = 0
    for i in range(len(imgList)):
        print(i)
        
        if i % 2 == 0:
            
            img = imgResize(imgList[i],imgList[i+1])
            imgName = str(i)
            showImg(imgName,img)
            contours_demo(img)
            print(i)
            continue
        else:
            imgName = str(i)
            showImg(imgName,imgList[i])
            lowerList, upperList = colorRange()
            img = imgList[i]
            showImg("origin",img)
            binaryList = separateByColor(img, lowerList, upperList )
            t = 0
            for binary in binaryList:
                t = t + 1
                name = "counter" + str(t)
                contours, hierarchy=cv2.findContours(binary , cv2.RETR_EXTERNAL ,  cv2.CHAIN_APPROX_NONE )
                img = np.copy(imgList[i])
                cv2.drawContours(img, contours, -1, (255,0,0),3) 
                showImg(name,img)
            showImg("origin",imgList[i])
            
        # binary = showCounters(binary,True)
        # i = i + 1
        # imgName = str(i)
        # showImg(imgName,imgList[i])

if __name__ == "__main__":
    main()
