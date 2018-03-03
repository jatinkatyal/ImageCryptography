import numpy,random

def generateShares(secret,n,k):
	constants = []
	for i in range(k-1):
		constants.append(random.randint(1,1000))
	constants=[5,6]
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
	secret = cv2.imread('lenna.png')
	secret = cv2.cvtColor(secret,cv2.COLOR_RGB2GRAY)
	cv2.imshow('orig',secret)
	n = 10
	k = 3
	shares = generateShares(secret,n,k)
	for i in range(n):
		numpy.savetxt('Shares/'+str(i+1)+'.csv',shares[i],delimiter=',',fmt='%10.5f')
		cv2.imshow('test',shares[i])
		cv2.waitKey(3000)