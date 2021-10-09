# Paper Review of Detectability of Objects at the Sea Surface in Visible Light and Thermal Camera Images
## Background
- Visible Light Cameras:
	- Provide high spatial and high resolution image.
	- Suitable for detect 
         - very small objects (high resolution);
    	 - objects slightly below water (光能穿透水面).
- Thermal Cameras:
	- Provide low spatial and low resolution image.
	- Suitable for detect 
        - in low visible light situations;
        - objects at the sea surface （海洋表面在红外图里显得更光滑）

## Analysis and Questions about Background
- 对于成像特点的描述基本符合我们的设备。
- Suitable 的问题有待我们进一步的考量，需要对我们的设备的成像图进行分析。目前比较认同： 
    - Visible Light Cameras could detect smaller objects because it has 	    higher resolution.
    - Water surface in thermal cameras may appear to be more smooth.
  
## Methodology
- Grayscale Conversion: Separate Red, Green and Blue Channel
- Noise Reduction: Apply a low-pass filter
- Edge Detection: Sobel operator in Canny edge detection algorithm
- Location Objetcs in images: 
    - Visible Light Cameras – manually selected 
    - Thermal Cameras – first apply a GMM to separate the background and foreground, then manually selected

## Error Metric and Evaluation
- Metric - give a higher score when the difference between the object edges and background edges are larger.
- Specifically, An object is then considered detectable if its average edge value (the intensity of the image gradient) is larger than the average edge in a predefined fraction of the background windows.

## Parameter Tuning
- For Grayscale Conversion: The choice of channel: Red, Blue, Green or the average
- For Noise Reduction: 
    - The choice of 𝜎 
    - The choice of Gaussian kernel size: 1×1 ~ 15×15
- For Edge Detection: The choice of Sobel kernel size: 3×3 ~ 7×7
- NOTE: Parameters tuning for Visible Light Cameras and Thermal Cameras are carried out separately, due to different image characteristic.

## Experimental Results and Evaluation
### Visible Light Cameras 
- For Grayscale Conversion: The choice of the best channel highly depends on the color of the object which aims to detect.
- For Noise Reduction: The choice of 𝜎 depends on the size of the smallest object. (Such object must be greater than 1 pixel)
- For Edge Detection: The choice of Sobel kernel size depends on the size of the smallest object. (Such object must be greater than 1 pixel)
- **In general, edge detector reducing noise rather than emphasizing the edges produces better results.**

### Thermal Cameras
- For Edge Detection:
    - The choice of Sobel kernel sizedepends on the size of the 	smallest object. (Such object must be greater than 1 pixel)
    - Larger kernel resulting in more objects detected.
- **In general, edge detector emphasizing edge detection over noise reduction produces better results.**

## Analysis and Questions
- 这个算法（思路）在结构上可以借鉴，而且结果成功率较高。然而此算法在我们的具体情境下的表现需要进一步验证：
    - 能否detect出草、树枝、石头等复杂物体；
    - 能否经过改进用于detect riffle and pool；
    - 在我们的具体情况下，parameter tuning如何做出调整；
    - 在我们的具体情况下，能否找出更好的改进方法作用于Noise 	Reduction 和 Edge Detection；
    - 在我们的具体情况下，能否调整该算法的结构，增添步骤以	达到更好的效果。
- 该文章在算法实验上存在的问题：
    - parameter tuning在Grayscale Conversion上没有一个统一的标	准，也并没有深入分析出为什么要这么调整。
    - 虽然文章对Visible Light Cameras 和 Thermal Cameras 都进行了	分析，但没有找到一个能够将两者结合起来，共同提高	detection 准确性的方法。

