# -*- coding: utf-8 -*-
# exer4.py 
# 勾配強度画像を作成する
# I = math.sqrt(fx^2 + fy*2) 
# 画素値は[0,255]の範囲に切り詰める

import numpy as np
import sys
import cv2
import math

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )


#フィルタ処理

#ここを編集
for y in range( 1, img.shape[0]-1 ) : #端っこは無視
    for x in range( 1, img.shape[1]-1 ) : 
        #横sobel
        fx = -1*img[y-1,x-1]+ 0*img[y-1,x]+ 1*img[y-1,x+1]+\
             -2*img[y  ,x-1]+ 0*img[y  ,x]+ 2*img[y  ,x+1]+\
             -1*img[y+1,x-1]+ 0*img[y+1,x]+ 1*img[y+1,x+1]
        #縦sobel
        fy =  1*img[y-1,x-1]+ 2*img[y-1,x]+ 1*img[y-1,x+1]+\
              0*img[y  ,x-1]+ 0*img[y  ,x]+ 0*img[y  ,x+1]+\
             -1*img[y+1,x-1]- 2*img[y+1,x]- 1*img[y+1,x+1]
        #勾配強度を保存
        img_out[y,x] = math.sqrt( (math.pow(fx,2) + math.pow(fy,2)) )


        
#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
