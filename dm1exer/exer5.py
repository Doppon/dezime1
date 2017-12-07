# -*- coding: utf-8 -*-
# exer5.py 
# モザイク画像の作成
# 第2引数はモザイクのサイズ 
# この課題は, nparrayの[スライス表現]を使うと非常に簡単にかける（使わなくともよい）

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
R         = int(sys.argv[2])
fname_out = sys.argv[3]


#画像をロードしfloat型へ
img = cv2.imread(fname_in)
img = np.float64(img)


#モザイク画像の作成

#以下を編集（for文の範囲などは適宜変更すること）
for y in range( int( img.shape[0] / R + 1) ) : 
    for x in range( int( img.shape[1] / R + 1) ) :

        #ヒント：スライス表現により画像の矩形領域を取り出せる 
        # 以下は，[y*R, (y+1)*R) x [y*R, (y+1)*R) の矩形領域のrチャンネル 
        rectR = img[y*R:(y+1)*R, x*R:(x+1)*R, 2]
        rectG = img[y*R:(y+1)*R, x*R:(x+1)*R, 1]
        rectB = img[y*R:(y+1)*R, x*R:(x+1)*R, 0]
        
        
        #代入もできる 
        img[y*R:(y+1)*R, x*R:(x+1)*R, 2] = np.mean(rectR)
        img[y*R:(y+1)*R, x*R:(x+1)*R, 1] = np.mean(rectG)
        img[y*R:(y+1)*R, x*R:(x+1)*R, 0] = np.mean(rectB)
            
        
cv2.imwrite(fname_out, np.uint8( img) )
