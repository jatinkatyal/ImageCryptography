import numpy,random

def generateShares(secret,n,k):
	constants = []
	for i in range(k-1):
		constants.append(random.randint(100,5000))
	constants=[500,500]
	print(constants)
	shares = []
	for x in range(n):
		x=x+1
		share = secret.copy()
		for a in constants:
			p = constants.index(a)+1
			share += a*x**p
		shares.append(share)
	return shares


if __name__ == '__main__':
	import cv2
	secret = cv2.imread('Resources/lenna.png')
	#secret = cv2.cvtColor(secret,cv2.COLOR_RGB2GRAY)
	cv2.imshow('orig',secret)
	cv2.waitKey(50)
	N = 20
	k = 15
	shares = generateShares(secret,N,k)
	for i in range(N):
		cv2.imwrite('Shares/'+str(i+1)+'.png',shares[i])
		#numpy.savetxt('Shares/'+str(i+1)+'.csv',shares[i],delimiter=',',fmt='%i')
		cv2.imshow('test',shares[i])
		cv2.waitKey(250)