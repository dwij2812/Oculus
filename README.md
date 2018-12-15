# Oculus
A Virtual eye for the Blind
## Requirement
- OpenCV 3.4
- Python 3.6    
- Tensorflow-gpu 1.5.0  
- Keras 2.1.3
## Quick start

- Download official [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights) and put it on top floder of project.

- Run the follow command to convert darknet weight file to keras h5 file.
```
python yad2k.py cfg\yolo.cfg yolov3.weights data\yolo.h5
```

- run follow command to show the demo. The result can be found in `images\res\` floder.
```
python demo.py
