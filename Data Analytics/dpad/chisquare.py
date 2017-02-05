#chi square test.


def chiSquareTest(nrows,ncols,matrix):
	"""
	chiSquareTest(nrows,ncols,matrix):
		Returns the Chi-Square value (float) for a given matrix[nrows][ncols] of data.
	"""
	expectedMatrix = [[0.0 for j in range(ncols)] for i in range(nrows)]
	rowSum = [0 for i in range(nrows)]
	colSum = [0 for j in range(ncols)]

	currentRow = 0
	currentCol = 0

	for i in range(nrows):
		for j in range(ncols):
			rowSum[currentRow] = rowSum[currentRow] + matrix[i][j]
			if(j == currentCol):
				colSum[currentCol] = colSum[currentCol] + matrix[i][j]
			currentCol = currentCol + 1 
		currentRow = currentRow + 1
		currentCol = 0

	totalSum = sum(rowSum)
	chiSquareValue = 0.0

	for i in range(nrows):
		for j in range(ncols):
			expectedMatrix[i][j] = float((rowSum[i]*colSum[j])/totalSum)
			chiSquareValue += ((matrix[i][j] - expectedMatrix[i][j])**2/expectedMatrix[i][j])
	
	return chiSquareValue

