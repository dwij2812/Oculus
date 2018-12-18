# Oculus

## ℹ️ Project information


- **Project Name**: Oculus
- **Short Project Description**: Virtual eye for the Blind
- **Team Members**: Dwij Sukeshkumar Sheth (@dwij2812), Shantanu Singh (@shan1322), Siddharth Jain (@sid25298)
- **Demo Link**: https://dwij2812.github.io/Oculus/
- **Repository Link**: https://github.com/dwij2812/Oculus

## 🔥 About the Project
In order to complete day-to-day activities effectively and efficiently, Technology plays vital role in human life. Especially, Assistive Technology devices support to differently abled people, in order to live their life very comfortably. Realizing the importance of Assistive Technology, this product idea gives comprehensive solution for the blind people and provide them an end to end solution. With the power of embedded systems and advanced Artificial Intelligence techniques applied to the field of computer vision we aim to make a Hat/cap that can help the blind perceive the world around them. Oculus harnesses the power of AI to describe people, text and objects. It can tell visually-impaired persons, what is around them. If the camera on the hat is pointed at a park, the device can describe how the scene looks like. Oculus is made using a camera module which will be mounted on the cap in order to capture images of the world around the person which will be interfaced with an SBC (Raspberry Pi). Using advanced analytics and several machine learning algorithms for image segmentation like YOLO, CNNs (Convolutional Neural Networks) we have process the image using a trained model and narrate the scene in the picture to the user in real-time. Once the analytics part is done the image description so created is converted into speech format and sent to the audio device like a speaker, earphone so that the user can hear the description about it. This process is carried out repeatedly again and again at fixed intervals and sent to the user. The device is planned to be built on a cap to make it easy to use and trendy. The system will be powered by a rechargeable LiPo battery that is light weight and easy to mount on the cap. Further features like smartphone connectivity, safety features and ambience monitoring can be added to the cap and connect it with the cloud services so that the known contacts of the person can get to know any emergency situations or alerts immediately. Oculus uses frameworks like TensorFlow and Keras along with OpenCV in order to train and run the machine learning models that are used for the image captioning. Apart from that the Gtts (Google text to speech) library is used to convert the captions so generated into audio files which can be presented to the user for a hassle-free UX.


## 🔦 Highlights
- Easy to use
- Minimal hardware setup required
- Cost effective solution (Prototype cost: INR 4000, Expected production cost: INR 2500)
- Accurate and Reliable
- Hassle free UX

## Requirements
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

- Sample 3:

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/test7.jpg)

## Video Captioning

By the means of the classes obtained in the object detection section we now pass the images through a network of CNNs and RNNs to generate the captions for the video stream and describe it to the user via the use of audio devices which is discussed in the next section.

- Sample Input:

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/face.jpg)

- Sample Output:

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/caption.PNG)

## Raspberry Pi

- The Raspberry pi is interfaced along with a pi camera and is used to get the images at particular moments as required and serve it to the user.

*Steps to be followed*
- Use the capture.py code to capture the images at regular intervals of time.
- The images will be stored in the cwd of the capture.py script.
- The files so generated will be served to the master PC for processing via an HTTP based service.
- The speak.py is used to fetch the data from the processing unit and is conveted into speech using the gTTS (Google Text to Speech) library and the audio so generated is sent to the user via the headphones.

## Final Output

Here is the view of our final device.

![alt text](https://raw.githubusercontent.com/dwij2812/Oculus/master/samples/device.jpg)
