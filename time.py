# Python3 program for the above approach

# Function to find a pair in the given
# array whose sum is equal to z
def findPair(a, n, z) :
	
	# Iterate through all the pairs
	for i in range(n) :
		for j in range(n) :

			# Check if the sum of the pair
			# (a[i], a[j]) is equal to z
			if (i != j and a[i] + a[j] == z) :
				return True

	return False

# Driver Code

# Given Input
a = [ 1, -2, 1, 0, 5 ]
z = 0
n = len(a) 

# Function Call
if (findPair(a, n, z)) :
	print("True")
else :
	print("False")
	
	# This code is contributed by splevel62.
