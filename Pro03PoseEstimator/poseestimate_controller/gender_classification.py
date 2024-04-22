import cv2
import os

import numpy as np

# from face_detection import FaceDetection
class GenderClassification:
    def __init__(self, args=None):
        ori_dir = os.getcwd()
        os.chdir(os.path.dirname(__file__) or '.')
        
        # 加载性别分类器
        self.gender_model = cv2.dnn.readNetFromCaffe('../Models/deploy_gender.prototxt', '../Models/gender_net.caffemodel')
        
        os.chdir(ori_dir)
    
    def __call__(self, input_ctx):
        faces = input_ctx['faces']
        output_ctx = {}
        gender_list = []
        for face in faces:
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
            self.gender_model.setInput(blob)
            gender_preds = self.gender_model.forward()
            gender = "Male" if gender_preds[0][0] > gender_preds[0][1] else "Female"
            gender_list.append(gender)
        
        output_ctx['gender_result'] = gender_list
        output_ctx['bbox'] = input_ctx['bbox']
        
        return output_ctx
        

# if __name__ == '__main__':
#     res=cv2.imread('img.png')
#     input_ctx = {'image': res}
#     face_detector = FaceDetection()
#     result=face_detector(input_ctx)
#     gender_detector=GenderClassification()
#     print(result)
#     temp=gender_detector(result)
#     print(temp)
#     # for i in range(0,len(result['faces'])):
#     #     res=gender_detector(result['faces'][i])
#     #     print(res)

