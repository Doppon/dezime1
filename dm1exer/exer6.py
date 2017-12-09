# exer6.py
# ハーフトーン処理（ティザ法）

import numpy as np
import cv2
import sys


fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロードしてグレースケール化
img = cv2.imread( fname_in )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros_like(img)

#ティザパターン
mask = np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]])



#ハーフトーン画像を作成計算
#ここを編集（頑張ると3行くらいで書けます）
for y in range(H) :
  for x in range(W) :
    if( img[y,x]*16/255 >= mask[y%4,x%4]) :
      img_out[y,x] = 255
    else :
      img_out[y,x] = 0



#出力
cv2.imwrite( fname_out, img_out);