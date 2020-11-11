import glob
import os
import re
import cv2

def change_name() :
     a=1380
     for file in glob.glob(r"F:\100.Lesis_final_last\1.create_databse/set_5/*.jpg") :

     #print(images_list)
     #for frame in images_list:
      #cap = cv2.VideoCapture(0)
     #for file in glob.glob("data_safe_set/*"):
        #print(file)
        a +=1

        image = cv2.imread(file, 1)           
        cv2.imshow("Face Recognizer", image)
        cv2.imwrite('final_safe_baseset/image_test_{}.jpg'.format(a),image)
    #cv2.destroyAllWindows()

change_name()
#cv2.destroyAllWindows()
	    