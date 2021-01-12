# shape-detection-and-measurment-using-open-cv-python
detecting shapes of objects on a conveyor in industries and measuring them. 

# contents
1. [concept of the project](#concept-of-the-project)
2. [libraries used](#libraries-used)
3. [code and algorithm](#Code-and-Algorithm)

## concept of the project
Ill start with a little background on this project .This is my final semester mechanical engineering project.Being a mechanical engineer, i wanted to do something related to programming and machine vision seemed to the technology which connected both the worlds. The project is based on the concept of machine vision i.e using computer vision to identify and measure objects. In mechanical engineering , this project comes under the metrology domain which is concerned with measuring objects. The objective of the project is to provide an alternative to  manual quality control process which involves measuring objects one by one using required instruments which in general is very time consuming and more prone to errors. Implementing this technology would reduce the time and errors significantly and thereby increase the production.

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/Example_of_a_machine_vision_conveyor_belt_application.jpg)


## Libraries used
[open cv](https://opencv-python.readthedocs.io/_/downloads/en/latest/pdf/) is the only library that has been used for this project. Open computer vision library is used for operating the camera , image/video capturing and processing. It connects the algorithms with the object in front of the camera. 

## code and algorithm

The code is written in python. The code has the following parts .

  1. ### gray scaling
  2. ### thresholding
  3. ### contour detection
  4. ### processing the contour coordinates
  
### gray scaling
The camera is turned on and everything captured by it is converted to gray scale(black and white). This is followed by a process called thresholding.

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/coloured-image-to-grayscale-using-opencv.jpg)

### thresholding

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/ConvertIntensityImageToBinaryImageUsingLevelThresholdExample_01.png)
after gray scaling the frames are now in black and white. The gray scale frame now has pixel values ranging from 0 to 255 where 0 is complete black and 255 is completely white. while applying **binary thresholding** , we specify two values say x and y. The pixel values in the frame which are less than x are set to 0 and pixel values greater than x are set to y.
![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/thresh.jpg)

### contour detection
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.The inbuilt function in python open cv called find contours is used. 

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/contours.png)


### processing the contour coordinates

The find contour method gives us a numpy array of the  coordinates of the curve joining all the continous points around the object. 
using the contours we find the following , 

- **max x coordinate**
- **max y coordinate**
- **min x coordinate**
- **min y coordinate**

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/contour%20coordinate.jpg)

####  width = max x - min x
####  height = max y - min y 

### shape detection 
![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/distance%20point.png)

we use this formula in a for loop to find the distance between each and every adjacent point . **adding all these points gives us the perimeter of the shape**. 
![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/forloop.png). this perimeter is stored in the variable called **distance**

after this we calculate the perimeter for **rectangle and circle** using formuals. we subtract width and height for **square**.
we then append them to a list and sort them. 
we compare it with another list which has the same values in the order squares ,circle and rectangle. 

![](https://github.com/uday1and100/shape-detection-and-measurment-using-open-cv-python/blob/main/algo.png)





