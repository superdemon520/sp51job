# -*- coding: utf-8 -*-
"""
Create on 2018-09-26 15:26:40

@author joshuaZK
"""

import os
import jieba
import numpy as np 
import pandas as pd 
from os import path
from PIL import Image
from random import randint
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS,get_single_color_func


text = ''

da = pd.read_csv('../jobspider.txt', names = ['job_name','job_company_name','job_place','job_salary','job_time'], header = None, sep='[,]', encoding='utf-8')
# print(da['job_name'].value_counts())
job_names=[]


for line in open('../jobspider.txt','r',encoding='utf8'):
    line=line.replace('\n','').split(",")
    job_names.append(line[0])
job_names = list(set(job_names))
# print(job_names)
text += ' '.join(job_names)
'''
    设置背景
    scipy.misc imread()：返回的是 numpy.ndarray 也即 numpy 下的多维数组对象
'''

backgroud_Image = plt.imread('/Users/joshuazk/Downloads/back_image.jpg')
wc = WordCloud(
    background_color='white',# 设置背景颜色
    mask=backgroud_Image,# 设置背景图片   
    font_path='wryh.ttf',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=100, # 设置最大显示词数
    stopwords=STOPWORDS,# 设置停用词
    max_font_size=100,# 设置字体最大值
    # min_font_size=20,
    random_state=10# 设置有多少种随机生成状态，即有多少种配色方案
    # color_func = get_single_color_func('blue')
)

# wc.generate_from_text(text)
wc.generate_from_frequencies(da['job_name'].value_counts())
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc.recolor(color_func=get_single_color_func('green')), interpolation="bilinear")
plt.axis('off')
plt.show()
d = path.dirname(__file__)
wc.to_file(path.join(d, "jobspider.jpg"))

# words = da['job_name']
