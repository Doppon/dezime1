# -*- coding: utf-8 -*-
# exer1.py 
# 画像の赤と青チャンネルを交換する

import numpy as np
import sys
import cv2

#load image
fname_in  = sys.argv[1]
fname_out = sys.argv[2]

img = cv2.imread(fname_in)

H   = img.shape[0]
W   = img.shape[1]

for y in range(H) : 
    for x in    range(W) : 
        r = img[y,x,2]
        g = img[y,x,1]
        b = img[y,x,0]
        # ここを編集
        
#save image
cv2.imwrite(fname_out, img )
