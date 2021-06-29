"""Sample prediction script for TensorFlow 2"""
import argparse
import tensorflow as tf
import numpy as np
import PIL.Image
import os

MODEL_FILENAME = 'model.pb'
LABELS_FILENAME = 'labels.txt'


class ObjectDetection:
    INPUT_TENSOR_NAME = 'image_tensor:0'
    OUTPUT_TENSOR_NAMES = ['detected_boxes:0', 'detected_scores:0', 'detected_classes:0']

    def __init__(self, model_filename):
        graph_def = tf.compat.v1.GraphDef()
        with open(model_filename, 'rb') as f:
            graph_def.ParseFromString(f.read())

        self.graph = tf.Graph()
        with self.graph.as_default():
            tf.import_graph_def(graph_def, name='')

        # Get input shape
        with tf.compat.v1.Session(graph=self.graph) as sess:
            self.input_shape = sess.graph.get_tensor_by_name(self.INPUT_TENSOR_NAME).shape.as_list()[1:3]

    def predict_image(self, image):
        image = image.convert('RGB') if image.mode != 'RGB' else image
        image = image.resize(self.input_shape)

        inputs = np.array(image, dtype=np.float32)[np.newaxis, :, :, :]
        with tf.compat.v1.Session(graph=self.graph) as sess:
            output_tensors = [sess.graph.get_tensor_by_name(n) for n in self.OUTPUT_TENSOR_NAMES]
            outputs = sess.run(output_tensors, {self.INPUT_TENSOR_NAME: inputs})
            return outputs


def predict(model_filename, image_filename):
    od_model = ObjectDetection(model_filename)

    image = PIL.Image.open(image_filename)
    return od_model.predict_image(image)


def main():
  
    labels_filename = "labels.txt"
    #path = "C:/Users/User/0612_Merge_Json/Test_Image_Complete/"
    path = "C:/Users/User/0612_Merge_Json/50%_UpperBody_Image/"
    for filename in os.listdir(path):
        predictions = predict(MODEL_FILENAME, path+filename)

        with open(labels_filename) as f:
            labels = [l.strip() for l in f.readlines()]

        #count 用來計算圖片裡的服飾件數
        count = 1
        f1 = open(path+"/"+filename.split('.')[0]+".json", "a") 
        f1.write(str("{"+f"'filename':'{filename}',".replace("'",'"').replace("(",'').replace(")",'')))
        f1.close()
        for pred in zip(*predictions):
            if(pred[1]>0.5):
               
                # print(filename)
                # print(f"Class{count}: {labels[pred[2]]}, Probability: {pred[1]}, Bounding box: {pred[0]}")
                f1 = open(path+"/"+filename.split('.')[0]+".json", "a") 
                f1.write(str(f"'item{count}':".replace("'",'"')))
                f1.writelines(str("{"+f"'Class':'{labels[pred[2]]}', 'Probability': {pred[1]}, 'Bounding box':[{pred[0][0],pred[0][1],pred[0][2],pred[0][3]}]"+"},").replace("'",'"').replace("(",'').replace(")",''))
                f1.close()
            count = count+1

        #去除掉最夠一個逗號
        with open(path+"/"+filename.split('.')[0]+".json", 'rb+') as f1:
            f1.seek(-1, os.SEEK_END)
            f1.truncate()

        #增加右大括號
        f1 = open(path+"/"+filename.split('.')[0]+".json", "a")
        f1.write("}")
        f1.close()
   
               

if __name__ == '__main__':
    main()
