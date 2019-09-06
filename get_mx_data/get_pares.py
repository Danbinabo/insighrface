# coding:utf-8
import sys
import os
import random
import time
import itertools

src = '../data/valid/'                # 验证集文件夹
dst = open('../data/pairs.txt', 'a')  # .txt文件
same_list = []   # 相同id人脸路径
diff_list = []   # 不同id人脸路径
list1 = []       # 存放所有id人脸
list2 = []       # 存放所有id人脸
folders_1 = os.listdir(src) # 所有人脸id文件夹
same_flag = 0 # 产生相同的图像对
for folder in folders_1:  # 遍历每一个人脸id文件夹
    sublist = []  # 当前相同id文件夹下的人脸图片
    imgs = os.listdir(os.path.join(src,folder)) # 该人脸id文件夹下所有图片
    for img in imgs:#遍历其中每一张图片
        img_root_path = os.path.join(src, folder, img)
        sublist.append(img_root_path)
        list1.append(img_root_path)
    # 相同id的人脸组合--任取2张图片
    for item in itertools.combinations(sublist, 2):
        for name in item:
            same_list.append(name) # 排列组合式添加
for j in range(0, len(same_list), 2):
    print(same_list[j])
    print(same_list[j+1])
    name_img = same_list[j].split('\\')[-1].split('_0')[0]
    num_1 = int(same_list[j].split('\\')[-1].split('_')[-1].split('.png')[0])  # 第几张
    num_2 = int(same_list[j+1].split('\\')[-1].split('_')[-1].split('.png')[0])# 下一张
    dst.writelines(name_img + ' ' + str(num_1) + ' ' + str(num_2) + '\n')
    same_flag += 1
    if same_flag >= 3000:
        break
print('制作相同数据id数：',same_flag)

list2 = list1.copy()
# 产生不同的图像对
diff = 0
# 如果不同的图像对远远小于相同的图像对，则继续重复产生，直到两者相差很小
while True:
    random.seed(time.time() * 100000 % 10000)
    random.shuffle(list2)
    for p in range(0, len(list2), 2):
        if list2[p].split('\\')[-1].split('_0')[0] != list2[p - 1].split('\\')[-1].split('_0')[0]:
            name_img_1 = list2[p].split('\\')[-1].split('_0')[0]
            num_1_1 = int(list2[p].split('\\')[-1].split('_')[-1].split('.png')[0])
            name_img_2 = list2[p - 1].split('\\')[-1].split('_0')[0]
            num_1_2 = int(list2[p - 1].split('\\')[-1].split('_')[-1].split('.png')[0])
            #dst.writelines(list2[p] + ' ' + list2[p - 1] + '\n')
            dst.writelines(name_img_1 + ' ' + str(num_1_1) + ' ' + name_img_2 + ' ' + str(num_1_2) + '\n')
            diff += 1
        if diff >= 3000:
            break
    if diff >= 3000:
        break

