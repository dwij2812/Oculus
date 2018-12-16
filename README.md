# Oculus
A Virtual eye for the Blind
## Requirement
- OpenCV 3.4
- Python 3.6    
- Tensorflow-gpu 1.5.0  
- Keras 2.1.3
## Object Detection
*Steps to be followed*

- Download official [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights) and put it on top floder of project.

- Run the follow command to convert darknet weight file to keras h5 file.
```
python yad2k.py cfg\yolo.cfg yolov3.weights data\yolo.h5
```

- Run follow command to show the demo. The result can be found in `images\res\` floder.
```
python demo.py

```
*Some Sample Outputs*

- Sample 1:

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/test43.jpg)

- Sample 2:

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/test39.jpg)

## Raspberry Pi

- The Raspberry pi is interfaced along with a pi camera and is used to get the images at particular moments as required and serve it to the user.

*Steps to be followed*
- Use the capture.py code to capture the images at regular intervals of time.
- The images will be stored in the cwd of the capture.py script.
- The files so generated will be served to the master PC for processing via an HTTP based service.


