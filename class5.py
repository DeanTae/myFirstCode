# I am so sleepy I wanna sleep right now
# 1,3,5,6

# 1 
def fabricYards(inch):
	count = inch/36
	if inch%36 > 0:
		count = count + 1
	return count

def testFabricYards():
	print("testing Fabric Yards")
	assert(fabricYards(6)==1)
	assert(fabricYards(90)==3)
	assert(fabricYards(72)==2)
	print("everything Fine")

testFabricYards()

#3
def isMultiple(m,n):
	if m == 0:
		return True
	if m%n == 0:
		return True
	return False


def testIsMultiple():
	print("testing Is Multiple")
	assert(isMultiple(9,8)==False)
	assert(isMultiple(198,2)==True)
	assert(isMultiple(0,98)==True)
	print("everything Fine")

testIsMultiple()


print("---------------------------------")
#5
def isLegalTriangle(s1,s2,s3):
	if s1 >= s2 and s1 >= s3:
		return s1 < s2+s3
	if s2 >= s3:
		return s2 < s1+s3
	else:
		return s3 < s1+s2

print(isLegalTriangle(3,3,3))


#6


