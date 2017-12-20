import io
import picamera
import cv2
import numpy

class capture(object):
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




