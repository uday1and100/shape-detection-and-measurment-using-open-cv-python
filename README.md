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







