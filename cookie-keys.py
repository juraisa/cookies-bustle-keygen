import random

def testkey(input):
	keyarray = {}
	j = 0
	for i in input:
		j = j+1
		keyarray[j] = i

	n1 = int(keyarray[7])
	n2 = int(keyarray[8])
	n3 = int(keyarray[9])
	n4 = int(keyarray[10])
	n5 = int(keyarray[13])
	n6 = int(keyarray[14])
	n7 = int(keyarray[15])

	s1 = ((n1 * 4) + (n2 * 3) + (n3 * 2) + (n4 * 1)) % 10
	s6 = ((n5 * 1) + (n6 * 2) + (n7 * 3)) % 10
	sa = (n4 + s6 + 2) * (n7 + s1 + 1) % 100
	if s1 is not int(keyarray[6]):
		return
	if s6 is not int(keyarray[12]):
		return
	if sa is not int(keyarray[17]+keyarray[18]):
		return
	print(input)
  
while True:
	r1 = "%05d" % random.randint(0,99999)
	r2 = "%04d" % random.randint(0000,9999)
	r3 = "%02d" % random.randint(00,99)
  #replace W with M for mac versions
	key = "CB1W-%s-%s-%s" % (r1,r2,r3)
	testkey(key)
