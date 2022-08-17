# Face-Detection
---
The method by which the programme detects the face is by using haar cascades its accuracy is dependent on the lighting condition of the subject in frame and the quality of the image being processed. The programme utilizes the opencv module to use the camera and the convert the image into black and white from color to ensure that it is able to meet the haar cascde requirements for input is able to process the image.
## File location
---
<<<<<<< HEAD
<p>In order for the programme to call the haar cascade ensure that the location of the variable haar_cascade is set to the location where the haar cascade is downloaded.</p>
<code>haar_cascade = cv.CascadeClassifier("C:/Users/...../haar_face.xml")</code>
## Programme in action
---
The programme is able to detect face with a proper lighting and background to high degree of accuracy.
<p align="center">
  <img src="Photos/face.png" width="300" height="300"/>
</p>
It can also detect multiple faces with ease
<p align="center">
  <img src="Photos/face1.png" width="300" height="300"/>
</p>
=======
In order for the programme to call the haar cascade ensure that the location of the variable haar_cascade is set to the location where the haar cascade is downloaded.`haar_cascade = cv.CascadeClassifier("C:/Users/...../haar_face.xml")`
>>>>>>> 1e7a7dcb875ad266f38000e790171579e5e920c1
