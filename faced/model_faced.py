import cv2

from faced import FaceDetector
from faced.utils import annotate_image

face_detector = FaceDetector()
img_path = '/Users/wangzifan/Downloads/WIDER_test/images/29--Students_Schoolkids/29_Students_Schoolkids_Students_Schoolkids_29_762.jpg'
img = cv2.imread(img_path)
rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
thresh = 0.5
# Receives RGB numpy image (HxWxC) and
# returns (x_center, y_center, width, height, prob) tuples. 
bboxes = face_detector.predict(rgb_img, thresh)

# Use this utils function to annotate the image.
ann_img = annotate_image(img, bboxes)

# Show the image
cv2.imshow('image',ann_img)
cv2.waitKey(0)
cv2.destroyAllWindows()