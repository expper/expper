
Compile openCV  https://docs.opencv.org/trunk/dd/dd5/tutorial_py_setup_in_fedora.html
                https://computervisiononline.com/blog/install-opencv-31-and-python-27-centos-7

We need CMake to configure the installation, GCC for compilation, Python-devel and Numpy for creating Python extensions etc.

yum install cmake
yum install python-devel numpy
yum install gcc gcc-c++

Next we need GTK support for GUI features, Camera support (libdc1394, libv4l), Media Support (ffmpeg, gstreamer) etc.

yum install gtk2-devel
yum install libdc1394-devel
yum install libv4l-devel
yum install ffmpeg-devel
yum install gstreamer-plugins-base-devel

OpenCV comes with supporting files for image formats like PNG, JPEG, JPEG2000, TIFF, WebP etc. But it may be a little old.
If you want to get latest libraries, you can install development files for these formats.

yum install libpng-devel
yum install libjpeg-turbo-devel
yum install jasper-devel
yum install openexr-devel
yum install libtiff-devel
yum install libwebp-devel

Several OpenCV functions are parallelized with Intel's Threading Building Blocks (TBB).
But if you want to enable it, you need to install TBB first.
( Also while configuring installation with CMake, don't forget to pass -D WITH_TBB=ON. More details below.)

yum install tbb-devel

OpenCV uses another library Eigen for optimized mathematical operations.
So if you have Eigen installed in your system, you can exploit it.
( Also while configuring installation with CMake, don't forget to pass -D WITH_EIGEN=ON. More details below.)

yum install eigen3-devel


If you want to build documentation ( Yes, you can create offline version of OpenCV's complete 
official documentation in your system in HTML with full search facility so that you need not 
access internet always if any question, and it is quite FAST!!! ),
you need to install Doxygen (a documentation generation tool).

yum install doxygen


Installing OpenCV
The preparation steps are done and now we are ready to get the OpenCV source code and install it. To check out the OpenCV core library, run the following commands

yum install python3-devel.i686 python3-devel.x86_64
pip3 install numpy

cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.1.0
We also should check out the contributed modules for the same version. These modules are not released as a part of official OpenCV distribution but provide some of the most interesting functionalities in OpenCV and perhaps are the main reason for you to use OpenCV library.

cd ~
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.1.0
Now that we checked out both OpenCV and its contributed modules, we can set up the build where cmake plays its role.

cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=ON \
    -D BUILD_OPENCV_PYTHON2=ON ..
Then compile and install

sudo make
sudo make install
sudo ldconfig

pip3 install tensorflow
pip3 install GoogleMaps
pip3 install wikipedia
pip3 install SpeechRecognition
dnf install python3-pyaudio
dnf install portaudio-devel
dnf install python3-devel.x86_64 python3-devel.i686 boost-python3-devel.x86_64 boost-python3-devel.i686
pip3 install --upgrade PyAudio
pip install --upgrade google-cloud-speech
https://cloud.google.com/speech/docs/streaming-recognize

https://pypi.python.org/pypi/google_speech/
dnf install sox
pip3 install --upgrade google-cloud-speech

pip3 install Pillow
pip3 install pytesseract
dnf  install tesseract
