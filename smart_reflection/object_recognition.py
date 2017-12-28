from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#import io
#import picamera
import os
import cv2
import numpy
import pytesseract
from PIL import Image
from classify_image import classify_image

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class object_recognition(metaclass=Singleton):

    def __init__(self):
        self.is_enabled = False
        self.frame = None

    def set_enable_state(self, b):
        self.is_enabled = b

    def get_enable_state(self):
        return self.is_enabled

    def __detected_object_to_answer(self, d):
        f = 0
        s = ""
        for i in d:
            if f < d[i]:
                f = d[i]
                s = i
        return s

    def detect_image(self):
        path = "pt.png"
        cap = None
        if False == self.is_enabled:
            cap = cv2.VideoCapture(0)
            ret, self.frame = cap.read()
        cv2.imwrite(path, self.frame)
        if cap != None:
            cap.release()
            cv2.destroyAllWindows()
        c_img = classify_image()
        s = self.__detected_object_to_answer(c_img.detect_image(path))
        os.remove(path)
        if s == "":
            return "I am sorry but I don\'t know."
        return "This is " + s

    def text_from_image(self):
        path1 = "pt.png"
        path2 = "pt1.png"
        cap = None
        if False == self.is_enabled:
            cap = cv2.VideoCapture(0)
            ret, self.frame = cap.read()
        cv2.imwrite(path1, self.frame)
        if cap != None:
            cap.release()
            cv2.destroyAllWindows()
        image = cv2.imread(path1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 256, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        cv2.imwrite(path2, gray)
        text = pytesseract.image_to_string(Image.open(path2))
        os.remove(path1)
        os.remove(path2)
        if text == "":
            return "I am sorry but I can\'t read the text."
        return text

    def enable_camera(self):
        cap = cv2.VideoCapture(0)
        while(True):
            ret, self.frame = cap.read()
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', self.frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')) or False == self.is_enabled:
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

'''class capture(object):
    def __init__(self):
        self.stream = io.BytesIO()
        self.camera = picamera.PiCamera()
        #self.camera.resolution = (320, 240)
    def __delete__(self):
        pass
    def get_path(self):
        self.camera.capture(self.stream, format='jpeg')
        buff = numpy.fromstring(self.stream.getvalue(), dtype=numpy.uint8)
        self.image = cv2.imdecode(buff, 1)
        self.save_pic("tmp.jpg")
        return "tmp.jpg"
    
    def save_pic(self, fileName):
        #Save the result image
        cv2.imwrite(fileName,self.image)

class face_detection(object):
    def __init__(self):
        #Create a me2mory stream so photos doesn't need to be saved in a file
        self.stream = io.BytesIO()
        self.camera = picamera.PiCamera()
        self.camera.resolution = (320, 240)
    def __delete__(self):
        pass
    def detect_face(self):
        #Get the picture (low resolution, so it should be quite fast)
	#Here you can also specify other parameters (e.g.:rotate the image)
        self.camera.capture(self.stream, format='jpeg')
        
        #Convert the picture into a numpy array
        buff = numpy.fromstring(self.stream.getvalue(), dtype=numpy.uint8)
	
        #Now creates an OpenCV image
        self.image = cv2.imdecode(buff, 1)
	
        #Load a cascade file for detecting faces
        face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
	
        #Convert to grayscale
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
	
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	
        print ("Found "+str(len(faces))+" face(s)")
	
        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,255,0),2)
        
        self.save_pic("result.jpg")
    
    def save_pic(self, fileName):
        #Save the result image
        cv2.imwrite(fileName,self.image)

'''



