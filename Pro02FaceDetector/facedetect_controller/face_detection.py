import dlib
import cv2
import numpy as np

class NewFaceDetection:
    def __init__(self, args=None):
        # 加载人脸检测器
        self.detector = dlib.get_frontal_face_detector()
    
    def __call__(self, image):
        # image = input_ctx['image_mat']
        height, width, _ = image.shape
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 执行检测
        rects_2 = self.detector(gray, 1)
        print("look:",rects_2)
        # 将结果转换为np.array
        res_list = []
        faces_list = []
        for rect in rects_2:
            x_min = int(max(rect.left(), 0))
            y_min = int(max(rect.top(), 0))
            x_max = int(min(width, rect.right()))
            y_max = int(min(height, rect.bottom()))
            res_list.append([x_min, y_min, x_max, y_max])
            # faces_list.append(image[y_min:y_max, x_min:x_max])
        
        # output_ctx = {
        #     'bbox': res_list,
        #     'faces': faces_list
        # }
        
        # return output_ctx
        return res_list

if __name__ == '__main__':
    detector=NewFaceDetection()
    img=cv2.imread('img.png')
    res=detector(img)
    print(res)