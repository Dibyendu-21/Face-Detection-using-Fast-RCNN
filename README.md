# Face-Detection-using-Fast-RCNN
# Detect faces from image using Fast RCNN
Keras implementation of Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks to detect multiple faces from an image.
cloned from https://github.com/yhenon/keras-frcnn/

## Dataset Used
A novel dataset from Analytic Vidhya was used which beared the image name and corresponding bbox coordinates of each bbox in that image. It had multiple rows of the same sample image because each image had multiple faces and thereby multiple bboxes.

## Approach
In order to train fast RCNN model from scratch on the dataset provided by Analytics Vidhya, we have to convert our dataset into an annotation file of the form which is processed by Fast RCNN which is accomplished by using ananotation.py.

## USAGE
- simple_parser.py provides an alternative way to input data, using a text file. Create an annotation text file, with each line containing:

    `filepath,x1,y1,x2,y2,class_name`

    For example:

    image_data/10001.jpg,192,199,230,235,4    
    image_data/10001.jpg,247,168,291,211,4

    The classes will be inferred from the file. To train Fast RCNN on native dataset from scratch simple parser was used. The command line option `-o simple` was used. For example `python train_frcnn.py -o simple -p my_data.txt`.


## Model training
Since Fast RCNN was  a very bulky model and the native implementation of it required training of the model to 2000 epochs, I trained the model on Google cloud with GPU for 100 epochs. It required to change keras version and tensorflow version which are present in the native Google cloud platform.

To change the keras and tensorflow version in google colab also required to cuda.
The following lines of code installed a new version of keras, tensorflow and cuda:
!pip uninstall tensorflow
!pip install keras==2.2.0
!pip install tensorflow-gpu==1.8.0
!wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
!dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
!apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
!apt-get update 
!apt-get install cuda=9.0.176-1

  

