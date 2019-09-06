# coding:utf-8
#将训练集中同一id但人脸图片数<=2的文件夹删除
import os
import shutil
src = '../lfw'    #lfw数据集
folders_1 = os.listdir(src) # 所有人脸id文件夹
for folder in folders_1:
    imgs = os.listdir(os.path.join(src,folder)) # 该人脸id文件夹下所有图片
    if(len(imgs)<=2):#Aaron_Eckhart
        new_path = os.path.join(src,folder)
        #os.rmdir(new_path)
        #os.remove(new_path)
        shutil.rmtree(new_path)
