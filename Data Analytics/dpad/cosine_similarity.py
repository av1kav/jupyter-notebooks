import math

def dotProduct(flist_a, flist_b, nrows, matrix):
	sum = 0
	for i in range(nrows):
		sum += (matrix[i][flist_a] * matrix[i][flist_b])
	return sum

def euclideanNorm(flist, nrows, matrix):
	result = 0
	for i in range(nrows):
		result += (matrix[i][flist] ** 2)
	result = math.sqrt(result)
	return result

def cosineSimilarity(nrows,matrix,flist_a,flist_b):
	""" 
	cosineSimilarity(nrows,ncols,matrix,flist_a,flist_b):
		Given the indices flist_a and flist_b of 2 features in a matrix[nrows][ncols], returns the 
		cosine similarity X using the dot product and euclidean normalization sub-functions. Note that
		flist_a and flist_b should be matrix indices indicating column numbers (start from 0)
	"""
	numerator = dotProduct(flist_a,flist_b,nrows,matrix)	
	denominator = euclideanNorm(flist_a,nrows,matrix)*euclideanNorm(flist_b,nrows,matrix)
	returnVal = numerator/denominator
	return returnVal







