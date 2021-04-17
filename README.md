# Social Distance Detector - GRIP-APRIL21- The Spark Foundation
Social distancing in Real-Time using live video stream/IP camera in OpenCV.


Output       |  Output
:-------------------------:|:-------------------------:
![Output](mylib/videos/output.gif?raw=true "Output")  |  ![Output](mylib/videos/output1.gif?raw=true "Output")

- Use case: counting the number of people in the stores/buildings/shopping malls etc., in real-time.
- Sending an alert to the staff if the people are way over the social distancing limits.
- Optimizing the real-time stream for better performance (with threading).
- Acts as a measure to tackle COVID-19.

---

## Setup Local Environment
- Install all the required Python dependencies:
```
pip install -r requirements.txt
```
- If you would like to use GPU, set ```USE_GPU = True``` in the config. options at 'mylib/config.py'.

- Note that you need to build OpenCV with CUDA (for an NVIDIA GPU) support first:


- Download the weights file from [**here**](https://drive.google.com/file/d/1O2zmGIIHLX8SGs24W7mjRyFKvE_CSY8n/view?usp=sharing) and place it in the 'yolo' folder.

- To run inference on a test video file, head into the directory/use the command:
```
python run.py -i mylib/videos/test.mp4
```
- To run inference on an IP camera, Setup your camera url in 'mylib/config.py':

```
# Enter the ip camera url (e.g., url = 'http://191.138.0.100:8040/video')
url = ''
```
- Then run with the command:

```
python run.py
```
> Set url = 0 for webcam.


## References
***GRIP***
- 1. https://analyticsindiamag.com/covid-19-computer-vision/
- 2. https://www.pyimagesearch.com/2020/06/01/opencv-social-distancing-detector/

***Main:***
- YOLOv3 paper: https://arxiv.org/pdf/1804.02767.pdf
- YOLO original paper: https://arxiv.org/abs/1506.02640
- YOLO TensorFlow implementation (darkflow): https://github.com/thtrieu/darkflow

***Optional:***
- More theory: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
- Other trained model weights from official doc: https://pjreddie.com/darknet/yolo/

---

## Thanks for the read & have fun! GRIP@Spark #GRIPAPRIL21

