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
file = open( fname_in )
fi = []

while 1 :
    line = file.readline()
    if not line :
        break
    fi.append( float(line) )
file.close()

print(fi)


#fourie transform
N = len(fi)

Rk = []
Ik = []

for k in range(N+1) :
    rk,ik=0,0
    #ここを修正する　append(ｘ)は末尾に要素ｘを追加する
    for l  in range(N):
        rk+=fi[l]*math.cos(2.0*math.pi*k*l/N) /N
        ik-=fi[l]*math.sin(2.0*math.pi*k*l/N) /N
    Rk.append(rk)
    Ik.append(ik)



file_out = open(fname_out, 'w') # 書き込みモードで開く
for i in range( N ) :
    file_out.write( str( Rk[i] ) + ' ' + str( Ik[i] ) + '\n')
    printt
file_out.close()