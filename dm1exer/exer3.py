# -*- coding: utf-8 -*-
# exer3.py 
# 画像に横方向sobel filterをかける
#  - 負値となる画素は-1倍，
#  - 255を超える画素には，オーバーフローを避けるため255を代入

import numpy as np
import sys
import cv2

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

        
#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, np.uint8( img_out) )
