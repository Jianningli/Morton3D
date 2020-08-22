import numpy as np
import sys



class zorder(object):
	def __init__(self,bitlength=9):
		self.bitlength=bitlength

	def checklen(self,n):
		bitlength=self.bitlength
		temp=[0]*bitlength
		if len(n)<bitlength:
			j=bitlength-1
			n=n[len(n)::-1]
			for i in range(len(n)):
				temp[j]=n[i]
				j-=1
			strn=''
			for i in range(bitlength):
				strn+=str(temp[i])
			temp=strn
		else:
			temp=n
		return temp


	def xyz2zorder(self,x,y,z,length):
		xb=bin(x)
		xb=xb[2:len(xb)]
		yb=bin(y)
		yb=yb[2:len(yb)]
		zb=bin(z)
		zb=zb[2:len(zb)]
		xb=self.checklen(xb)
		yb=self.checklen(yb)
		zb=self.checklen(zb)
		temp=[]
		for i in range(length):
			temp.append(zb[i])
			temp.append(yb[i])
			temp.append(xb[i])
		bits=''
		for i in range(len(temp)):
			bits=bits+temp[i]
		return int(bits,2), bits

	def zvalbin2xyz(self,bzvaluebin):
		x=''
		y=''
		z=''
		for i in range(0,len(bzvaluebin),3):
			z+=bzvaluebin[i]
			y+=bzvaluebin[i+1]
			x+=bzvaluebin[i+2]
		x=x.encode('utf-8')
		y=y.encode('utf-8')
		z=z.encode('utf-8')
		return [int(x,2),int(y,2),int(z,2)]


	def zval2xyz(self,bzvalue):
		bitlength=self.bitlength
		bina=bin(bzvalue)
		bina=bina[2:len(bina)]
		if len(bina)<bitlength*3:
			bina=bina[len(bina)::-1]
			for i in range(int(bitlength*3-len(bina))):
				bina+='0'
			bina=bina[len(bina)::-1]
		return self.zvalbin2xyz(bina)

	def Morton(self,x,y,z):
		bitlength=self.bitlength
		max_n=max(x,y,z)
		if max_n>=(2**bitlength):
			raise Exception("the coordinate values must be no greater than the maximum value the specified bit length can represent")

		zNum,bits=self.xyz2zorder(x,y,z,bitlength)
		return zNum,bits

	def deMorton(self,inp,isbin):
		if isbin:
			coor=self.zvalbin2xyz(inp)
		else:
			coor=self.zval2xyz(inp)
		return coor











