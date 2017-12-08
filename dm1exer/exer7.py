# task7.py
# ハーフトーン処理(誤差拡散法)

# 実行コマンドpython exer7.py fname_in.png fname_out.png
import numpy as np
import cv2
import sys

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#画像を読み込み、グレースケール化し、float型に変換
img = cv2.imread( fname_in  )
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = np.float64(img)


#出力画像を準備
H = img.shape[0]
W = img.shape[1]
img_out = np.zeros_like(img)


#誤差拡散法の計算
for y in range(H-1)  :
	for x in range( W-1)  :
		#二値化
		if( img[y,x] > 127	) :
			img_out[y,x] = 255
			e = img[y,x] - 255
		else :
			img_out[y,x] = 0
			e = img[y,x] - 0

		#誤差伝搬（誤差は元画像 img に足していく）
		if (x<W-1):
			img[y,x+1]+=e*5/16
		if (x!=0 or y<H-1):
			img[y+1,x-1]+=e*3/16
		if (y<H-1):
			img[y+1,x]+=e*5/16
		if (x<W-1 or y<H-1):
			img[y+1,x+1]+=e*3/16


		#ここを編集
		#この課題，ヒント出しすぎかも


cv2.imwrite( fname_out, img_out);