"""
LINEAR ALGEBRA PROGRAMMING ASSIGNMENT
NAME : Rupanshoo Saxena
ROLL NO. : 2019096
SEC - A   GROUP:6
"""
m = int(input("Enter No. of rows of the matrix:-"))
n = int(input("Enter no. of columns of the matrix:-"))

matrix = []

print("Enter matrix entries row-wise")
for i in range(m):   #loop to take the entries of the matrix as input from the user
	row = []
	for j in range(n):
		row.append(int(input()))
	matrix.append(row)


def print_Matrix(matrix,m,n):  #function to print the matrix
	for i in range(m):
		for j in range(n):
			print(matrix[i][j],end = " ")
		print()

print("Matrix entered by the user is:-")
print_Matrix(matrix,m,n)  #Calling the function to print the matrix entered by the user


def Column_major(matrix,m,n):   #to store the matrix column wise i.e. transpose the matrix
	column = []
	for i in range(n):
		column.append([])
		for j in range(m):
			column[i].append(matrix[j][i])
	return column

ColMatrix = Column_major(matrix,m,n)  #stores the transpose of the user entered matrix
print(ColMatrix)   

def mag(vec):  #return magnitude of a vector
	magnitude = 0
	for i in vec:
		magnitude+=i**2
	magnitude=magnitude**0.5
	return magnitude


def dot_product(v1,v2):  #to find out the dot product of two vectors
	product = 0
	for i in range(len(v1)):
		product = product + (v1[i]*v2[i]) 
	return product


def projection(w,v):  #returns projection of v on w
	proj = []
	for i in range(len(w)):
		dot = dot_product(v,w)  # to find dot product of the two vectors
		proj.append( (dot / ( ( mag(w) )**2) ) * w[i] )  # the formula for finding the projection of vector v on w
	return proj


def multiply(X,Y):  #takes the two matrices to be multiplied and the dimensions of the original row as arguments
	result = []    #list created to store the multiplication result
	for i in range (len(X)): 
		r_1=[]
		for j in range(len(Y[0])):
			prod=0
			for k in range(len(Y)):
				prod += X[i][k] * Y[k][j]   #product value of each element
			r_1.append(prod)  #product value updated in row
		result.append(r_1)  #row appended to result matrix
	
	return result


def Gram_Schmidt(ColMatrix,m,n):  #to find matrix Q using Gram Schmidt process : all processes are being done on column major matrix
	q = [ColMatrix[0]]   #to store the first column of the user entered matrix according to the algorithm
	for i in range(1,n):
		q_1=[]  # to store column wise values after performing algorithm
		for j in range(m):
			proj = 0
			for x in range(i):
				a = projection(q[x],ColMatrix[i])   #storing each projection term in list 'a'
				proj += a[j]
			q_1.append(ColMatrix[i][j] - proj)  #column wise stored term after carrying out the algorithm
			
		q.append(q_1)   #to append column wise values of matrix Q 
	
	for i in range(n):   #loop to normalize the given matrix Q
		magnitude=mag(q[i])
		for j in range(m):
			q[i][j] /= magnitude
	return q  #orthogonal matrix q is returned column-wise

Q = Gram_Schmidt(ColMatrix,m,n)   #stores Q for the matrix entered by the user
R = multiply(Q,matrix)    #stores R for the user entered matrix
print(Q)    # prints Q column-wise
print()
print(R)  #prints R row-wise