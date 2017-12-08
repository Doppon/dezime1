# -*- coding: utf-8 -*-
# exer9.py
#
# *txtファイルから数列を読み込み，フーリエ変換して出力する
# フーリエ変換結果の複素数列 Fk = Rk + i*Ik は，以下の通り書き出すこと
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
#以下に Rk = Ik = 0として書き出すコードを示す

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

for k in range(N) :
    rk,ik=0,0
    #ここを修正する　append(ｘ)は末尾に要素ｘを追加する
    for l  in range(N-1):
        rk+=fi[l]*math.cos(2.0*math.pi*k*l/N) /N
        ik-=fi[l]*math.sin(2.0*math.pi*k*l/N) /N
    Rk.append( rk)
    Ik.append(ik)



file_out = open(fname_out, 'w') # 書き込みモードで開く
for i in range( N ) :
    file_out.write( str( Rk[i] ) + " " + str( Ik[i] ) + "\n")
file_out.close()
