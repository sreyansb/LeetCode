isprime=[1 for i in range(201)]
isprime[0]=0
isprime[1]=0

for  i in range(2,int(201**0.5)+1):
	if isprime[i]:
		for j in range(i*i,201,i):
			isprime[j]=0

#We need to create a dpt table of 3 indices
#sum  - the sum till that length,
#length - the length of the number
#tight - whether the number at that position is bound
dpt=[[[-1 for i in range(2)]for j in range(22)]for k in range(201)]
def caller(X):
	for i in range(201):
		for j in range(22):
			for k in range(2):
				dpt[i][j][k]=-1
	return count1X(0,0,1,X)


def count1X(sumy,curlen,tight,X):
	if curlen==len(X):
		return isprime[sumy]
	if dpt[sumy][curlen][tight]!=-1:
		return dpt[sumy][curlen][tight]
	upperbound=9
	if tight:
		upperbound=int(X[curlen])
	res=0
	for i in range(upperbound+1):
		if i==upperbound:
			res+=count1X(sumy+i,curlen+1,tight&1,X)
		else:
			res+=count1X(sumy+i,curlen+1,0,X)
	dpt[sumy][curlen][tight]=res
	return res

left=10
right=10**20
#REMEMBER TO MAKE DPT's all elements=-1 after call to each
print(caller(str(right))-caller(str(left-1)))
'''
# Python3 program to implement
# the above approach
isPrime = [True] * 100001

dp = [[[-1 for i in range(2)]
	for i in range(100)]
	for i in range(1000)]

# Function to find all prime numbers
# in the range [1, 100000] using
# Sieve of Eratosthenes technique


def sieve():

	# 0 is not a prime number
	isPrime[0] = False

	# 1 is not prime number
	isPrime[1] = False

	# Traverse the range to check if
	# i is a prime number or not
	for i in range(2, 100001):
		if i * i > 100001:
			break

		# If i is a prime number
		if (isPrime[i]):
			for j in range(i * i, 100001, i):

				# Mark its multiples non-prime
				isPrime[j] = False

# Function to count all numbers in
# the range[1, X] whose sum of digits
# is a prime number


def cnt1XPrime(sum, lenn, tight, X):

	# If count of digits in current number
	# is equal to the count of digits in X
	if (lenn == len(X)):

		# If sum is a prime number
		return isPrime[sum]

	# If already computed subproblem
	# occurred
	if (dp[sum][lenn][tight] != -1):
		return dp[sum][lenn][tight]

	# Stores maximum possible value
	# at current digit of the number
	end = 9

	if tight:
		end = ord(X[lenn]) - ord('0')

	# Stores count of numbers by placing
	# all possible values at current index
	res = 0

	# Place all possible values at
	# current position
	for i in range(end + 1):

		# Update res
		res += cnt1XPrime(sum + i,
						lenn + 1,
						(tight & (i == end)), X)

	dp[sum][lenn][tight] = res
	return dp[sum][lenn][tight]

# Function to count the numbers in
# the range[L, R]


def cntLRprime(L, R):

	# Stores the value of (L - 1)
	# in the form of string
	LStr = str(L - 1)

	# Stores the value of (R)
	# in the form of string
	RStr = str(R)

	# isPrime[i] stores if i
	# is a prime number or not
	sieve()

	# Stores count of numbers in range
	# [1, LStr] with the given conditions
	cntL = cnt1XPrime(0, 0, 1, LStr)

	# Initalize dp[][][] array.
	for i in range(1000):
		for j in range(100):
			for z in range(2):
				dp[i][j][z] = -1

	# Stores count of numbers in range
	# [1, RStr] with the given conditions
	cntR = cnt1XPrime(0, 0, 1, RStr)

	# Return numbers in the range [L, R]
	# whose sum of digits is a prime number
	return (cntR - cntL)


# Driver code
if __name__ == '__main__':

	L = 12
	R = 10000000

	print(cntLRprime(L, R))

# This code is contributed by mohit kumar 29
'''