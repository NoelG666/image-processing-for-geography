# OpenCV Learning

**1.** Read image: <br>
Program read the image for the subsequent processing of the image
```
def testimage():
    print("彩色图")
    img = cv2.imread("opencvlearning\\001.jpg")
    print(img)
    #cvdisplay('image',img)
    print(img.shape)
    print("灰度图")
    greyimg = cv2.imread("opencvlearning\\001.jpg",cv2.IMREAD_GRAYSCALE)  #将图片处理为灰度图
    #cvdisplay('grey',greyimg)
    print(greyimg)
        #cv2.imwrite("D:\\Programming\\Python\\opencvlearning\\001grey.jgp", greyimg) 目前实现不了，也暂时用不到
    return
```

**2.** Video Processing: <br>
Separate the video into several frames and then produce every frame as image processing by using while loop or for loop. 
```
def testvideo():
    video = cv2.VideoCapture('opencvlearning\\001.MP4')   #读取视频
    if video.isOpened():    #用isopened函数判定读取成功与否
        open, frame = video.read()         #如果视频被成功打开了，判定video.read是不是读取到了这一帧，如果读取到了存到frame中并set open true
    else:
        open = False
    while open:
        ret, frame = video.read()  #.read()函数每一次调用会从前面的对象中读取一帧（第一次调用读取video的第一帧，顺次每调用一次往后读一帧
        if frame is None:                   #在numpy中对于逻辑表达式的判断不明确，利用is可以一定程度上避免
       #if frame.all == None                #它可以返回False如果等号两边两个式子是数值相等，也可以返回True因为等号两边两个式子是逻辑相等
                                            #因此在这个地方其对于逻辑表达式的判断直接采取 .all和 .any的方式更精确地判定
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #将上面读取到的一帧灰度化处理
            cv2.imshow('result', gray)                     #把这一帧展示出来
            if cv2.waitKey(1) & 0xFF == 27:               #如果ESC被按下或者展示的时间到了10s进行下一个循环（读取下一帧并灰度化处理）
                break
    video.release()
    cv2.destroyAllWindows()
```
**3.** Intercept Picture
```
def jiequ():
    img = cv2.imread("opencvlearning\\003.jpg")
    part = img[0:200,0:200]        #利用数组的方法截取图片的范围
    cvdisplay("part", part)
```

**4.** Separate RGB values of an image:<br>
```
def separate():
    img = cv2.imread("opencvlearning\\003.jpg")
    b1, g1, r1 = cv2.split(img)       #将img中存储的图片的rgb分离开存储到三个变量中
    print(b1)
    print(b1.shape)                 #但是其中每一个变量的数组大小都是不变的而且一样的
    img = cv2.merge((b1, g1, r1))  #用merge把分散开的三组数值重新组合在一起
    cvdisplay("merge", img)

    cur_img = img.copy()
    cur_img[:,:,0] = 0             #设定B矩阵（颜色为蓝色的所有像素）的所有值为 0
    cur_img[:,:,1] = 0             #设定g矩阵（颜色为蓝色的所有像素）的所有值为 0
    cvdisplay("red", cur_img)      #分离图片的红色部分

    cur_img = img.copy()
    cur_img[:,:,1] = 0
    cur_img[:,:,2] = 0             #设定R矩阵（颜色为蓝色的所有像素）的所有值为 0
    cvdisplay("blue",cur_img)      #分离图片的蓝色部分

    cur_img = img.copy()           
    cur_img[:,:,0] = 0
    cur_img[:,:,2] = 0
    cvdisplay("green", cur_img)
``` 

**5.** Add a border to an image
```
def Bordmaker():
    img = cv2.imread("opencvlearning\\003.jpg")
    replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, borderType=cv2.BORDER_CONSTANT, value = (255,255,255))
    #                                    |   |    \   \                           |
    #                                  top bottom left right          BORDER_REPLACE, BORDER_REFLECATE,etc.
    cvdisplay("replicate", replicate)
    return
```

**6.** Apply arithmetical operation on an image
```
def calculate():
    img = cv2.imread("opencvlearning\\001.JPG") 
    img2 = img + 10                             #Add the value of R,G,B with 10
    print(img2)
    return
```

**7.**  Superimposed images
```
img1=cv2.imread('opencvlearning\\001.JPG')
img2=cv2.imread('opencvlearning\\002.JPG')
res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)  #用不同比重将两张图片合并
```

**8.** Blur
```
def blur():
    img1 = cv2.imread('opencvlearning\\001.JPG')
    blur = cv2.blur(img1,(3,3))                               #均值滤波
    cvdisplay('blur', blur)
    
    box = cv2.boxFilter(img1, -1, (3,3), normalize = Ture)    #区块滤波
    cvdisplay("box", box)

    box2 = cv2.boxFilter(img1, -1, (3,3), normalize = False)
    cvdisplay("box2", box)

    aussian = cv2.GaussianBlur(img, (5,5), 1)                 #高斯滤波
    cvdisplay("aussian", aussian)

    median = cv2.medianBlur(img, 5)                           #中值滤波
    cvdisplay("median", median)
```


