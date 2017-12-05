# -*- coding: utf-8 -*-
# exer8.py 
# 3x3メディアンフィルタを実装する
# ヒント1: numpyには中央値を出力する関数があるのでそれを利用するとよい
# ヒント2: スライス表現を利用するとより簡単に計算可能

import numpy as np
import sys
import cv2

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像をロード, グレースケール化, float型へ変換
img = cv2.imread(fname_in)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#出力画像を準備(グレースケール，float型)
img_out = np.zeros_like( img )


#フィルタ処理
for y in range( 2, img.shape[0]-2 ) : 
    for x in range( 2, img.shape[1]-2 ) : 
        
        #ここを編集 
        


#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, img_out )
