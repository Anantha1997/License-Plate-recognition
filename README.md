# License-Plate-recognition

In order to detect licence we will use Yolo ( You Only Look One ) deep learning object detection architecture based on convolution neural networks.

You can detect car number plates with Python and OpenCV2. Because the number of visible possibilities for number plates are rather limited, it's very easy to do.

As with any Machine Learning program, data is king. First load the data.

Loads the cascade file and input image. Any car image will do:

Then apply the cascade file to the image and find the plates. Run the program to find the number plate.

The program has many more lines of code. But the general idea is to apply a cascade to find the plate object.
