HUMAN Face Detection System using HOG


To run:

$ python gather_annotations.py -h

$ python gather_annotations.py --dataset training/ --annotations annot.npy --images images.npy

$ python train.py --annotations annot.npy --images images.npy --detector object_detector.svm

$ python test.py --detector object_detector.svm --image faces1.jpg --annotate Human
