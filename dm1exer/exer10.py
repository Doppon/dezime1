# -*- coding: utf-8 -*-
# exer10.py 
#
# *txtファイルから複素数列を読み込み，逆フーリエ変換して出力する
# 入力・出力ともに複素数列であり，以下のフォーマットにて保存されているものとする (sample1.txt参照)
#
# ------fname_out.txt ------
# R0 I0 
# R1 I0
# R2 I0
#   :
# Rk Ik
#   :
# --------------------------
#
# pythonには複素数型が用意されているが今回は利用しない


import numpy as np
import sys
import math

fname_in  = sys.argv[1]
fname_out = sys.argv[2]

#数列データファイル(txt)を開く
Rk, Ik = [], []
for line in open(fname_in).readlines():
    data = line[:-1].split(' ')
    Rk.append( float(data[0]) )
    Ik.append( float(data[1]) )
print(Rk, Ik)


#fourie transform
N = len(Rk)
rl, il = [0]*N, [0]*N


#ここを編集




file_out = open(fname_out, 'w') # 書き込みモードで開く
for i in range( N ) : 
    file_out.write( str( rl[i] ) + " " + str( il[i] ) + "\n") 
file_out.close()



