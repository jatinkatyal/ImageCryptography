import numpy

def lagBasisFunc(i,x,ids):
	num=1
	denom=1
	for j in ids:
		if i!=j:
			num *= x-j
			denom *= i-j
	res = float(num)/denom
	print(num,denom,res)
	return res

def decrypt(x,f,ids):
	res = numpy.zeros(shares[0].shape)
	for i in range(len(f)):
		v = lagBasisFunc(ids[i],x,ids)
		res+=f[i]*v
	return res

if __name__ == '__main__':
	import os,random,cv2,time
	k = 8
	N=10
	s = os.listdir('Shares')
	shares = []
	ids=[]
	for i in range(k):
		share = random.choice(s)
		ids.append(int(share[:-4]))
		#Remove selected share to prevent redundacy
		index = s.index(share)
		s.pop(index	)

		share = cv2.imread('Shares/'+share)
		#share = cv2.cvtColor(share,cv2.COLOR_RGB2GRAY)
		cv2.imshow('test',share)
		cv2.waitKey(20)
		shares.append(share)

	print(ids)
	res = decrypt(N,shares,ids)
	cv2.imwrite('decrypted-message.png',res)
	cv2.imshow('img',res)
	cv2.waitKey(20)
	time.sleep(1)