from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter
from matplotlib import pyplot as plt
import cv2
import os
import json

#base_location = 'C:/Users/User/0612_Merge_Json/Test_Image_Complete/'#放未切割圖片資料夾
#image_location = 'C:/Users/User/0612_Merge_Json/Test_Image_Cut/'#放切割完圖片資料夾
# base_location = 'C:/Users/User/0612_Merge_Json/50%_UpperBody_Image_Complete/'#放未切割圖片資料夾
# image_location = 'C:/Users/User/0612_Merge_Json/50%_UpperBody_Image_Cut/'#放切割完圖片資料夾
base_location = 'D:/styler/img/stylenanda_women/0617/readyfor_obdec/'#放未切割圖片資料夾
image_location = 'D:/styler/img/stylenanda_women/0617/pattern_json_new/'#放切割完圖片資料夾
jList = os.listdir(base_location)
print(cv2.__version__)

for file in jList:
    
    if file.endswith(".jpg"):
        img = cv2.imread(os.path.join(base_location,file))
       # cv2.imshow("org", img)
        imgSize = img.shape #大小/尺寸
        pw = imgSize[1]      #图片的宽
        ph = imgSize[0]    #图片的高
    
    if file.endswith(".json"):
        with open(os.path.join(base_location,file) , 'r') as reader:
            jf = json.loads(reader.read())
        strjf = str(jf)
        maxi = strjf.count('Class') + 1
        for i in range (1,maxi):
            stri = str(i)
            # 裁切區域的 x 與 y 座標（左上角）
            x1 = int(jf["item"+stri]["Bounding box"][0]*pw)
            y1 = int(jf["item"+stri]["Bounding box"][1]*ph)
          
            # 長寬
            x2 = int(jf["item"+stri]["Bounding box"][2]*pw)
            y2 = int(jf["item"+stri]["Bounding box"][3]*ph)
            type = jf["item"+stri]["Class"]
            print(type)
            # 裁切圖片
            crop_img = img[y1:y2, x1:x2]
           # cv2.imshow("org", img)
           # cv2.imshow("cropped", crop_img)           
            cv2.waitKey(0)
            cv2.imwrite(image_location +file.split('.')[0]+'_'+type+'.jpg', crop_img)