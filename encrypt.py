import numpy, random

def f(a0,x,constants):
	pow = 1
	res = a0
	for a in constants:
		res += a * (x ^ pow)
		pow += 1
	return res

def genrateShares(image,n,k):
	x = image.shape[1]
	y = image.shape[0]
	random.seed()

	constants = []
	for i in range(k):
		constants.append(random.randrange(0,1000))
	print(len(constants))
	shares=[]
	for i in range(n):
		share = numpy.empty((y,x))
		for row in range(y):
			for col in range(x):
				share[row,col] = f(image[row,col],i,constants)
		shares.append(share)
		print('Share ',i,' created.')
	return shares

if __name__ == '__main__':
	import cv2

	img = cv2.imread('lenna.png')
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	n = 10#int(input('Number of shares: '))
	k = 3#int(input('Threshold to unlock: '))
	print('Generating shares...')
	shares = genrateShares(img,n,k)
	for i in range(n):
		numpy.savetxt('Shares/'+str(i),shares[i],delimiter=',',fmt='%10.5f')
		print('Saved ',i)