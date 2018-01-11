import numpy as np
import os
from scipy.misc import imresize, imread, imsave

def resize_img(input_data):
    input_r, input_c, _ = input_data.shape
    if input_r > input_c:
        output_c = 300
        output_r = np.int32(output_c*1.0/input_c*input_r)
    else:
        output_r = 300
        output_c = np.int32(output_r*1.0/input_r*input_c)
    resized_data = imresize(input_data,(output_r,output_c))

    crop_size = 256
    start_r = output_r/2 - crop_size/2
    start_c = output_c/2 - crop_size/2
    crop_data = resized_data[start_r:start_r+crop_size, start_c:start_c+crop_size, :]

    return crop_data

data_path = '/media/sunguofei/DATA1/road_data/'
data_type = 'rainy'

file_list = os.listdir(data_path+data_type)
if not os.path.exists(data_path+'processed/'+data_type):
    os.mkdir(data_path+'processed/'+data_type)
f = open('log.txt','w')
num=1
for file_obj in file_list:
    if file_obj.find('.jpg') >= 0:
        file_path = os.path.join(data_path+data_type, file_obj)
        img = imread(file_path,mode='RGB')
        process_data = resize_img(img)
        img_name = '/'+str(num).zfill(4)+'.jpg'

        imsave(data_path+'processed/'+data_type+img_name, process_data)
        f.write('{}\n'.format(file_obj))
        num +=1

f.close()    