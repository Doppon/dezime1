# -*- coding: utf-8 -*-
# exer8.py
# 5x5メディアンフィルタを実装する
# ヒント1: numpyには中央値を出力する関数があるのでそれを利用するとよい
# ヒント2: スライス表現(a:b)を利用するとより簡単に計算可能
# ヒント書きすぎか。。。

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

H = img.shape[0]
W = img.shape[1]


#フィルタ処理
for y in range( int(H/5+1) ) :
    medi_np = np.zeros(25)
    for x in range( int(W/5+1) ) :

        #ここを編集
        medi_np = img[y*5:(y+1)*5, x*5:(x+1)*5]
        img_out[y*5:(y+1)*5, x*5:(x+1)*5] = np.median(medi_np)


#float型からuint8型に変換し、書き出し
cv2.imwrite(fname_out, img_out )
