#team203


n = input()

def isnumber(a):
	if (a >= '0' and a <= '9') or a == '?':
		return True
	else:
		return False

def isletter(a):
	if a == '+' or a == '-' or a == '*':
		return True
	else:
		return False

def isequal(a):
	if a == '=':
		return True
	else:
		return False

def handlenumber(s, num):
	res = 0
	negflag = False
	if s[0] == '-':
		negflag = True
	dec = 1
	for i in range(len(s)-1,-1,-1):
		if i == 0 and s[i] == '-':
			break
		if s[i] != '?':
			res += dec*(ord(s[i])-ord('0'))
		else:
			res += dec*num
		dec *= 10
	if negflag:
		res *= -1
	return res

def checkfirst(a):
	if a[0] == '-':
		if a[1] == '?':
			return True
		else:
			return False
	if a[0] != '-':
		if a[0] == '?' and len(a) != 1:
			return True
		else:
			return False		
def exists(a,i):
	for j in range(0,len(a)):
		if i == (ord(a[j]) - ord('0')):
			#print "I is: ",
			#print i,
			#print "Variable digit is: ",
			#print ord(a[j])-ord('0')
			return True
	return False				

while n:
	n -= 1
	Kase = raw_input()
	opflag = False
	for i in range(0,len(Kase)):
		if i == 0 and isletter(Kase[i]):
			continue
		if opflag == False and isletter(Kase[i]):
			opflag = True
			posop = i
		if isequal(Kase[i]):
			poseq = i
	firstnumber = Kase[:posop]
	secondnumber = Kase[posop+1:poseq]
	thirdnumber = Kase[poseq+1:]
	operator = Kase[posop]
	
	fail = True
	for i in range(0,10):
		if i == 0 and (checkfirst(firstnumber) or checkfirst(secondnumber) or checkfirst(thirdnumber)):
			continue
		if (exists(firstnumber, i) or exists(secondnumber, i) or exists(thirdnumber, i)):
			continue
		if operator == '+':
			if handlenumber(firstnumber, i) + handlenumber(secondnumber, i) == handlenumber(thirdnumber,i):
				print i
				fail = False
				break
		if operator == '-':
			if handlenumber(firstnumber, i) - handlenumber(secondnumber, i) == handlenumber(thirdnumber,i):
				print i
				fail = False
				break
		if operator == '*':
			if handlenumber(firstnumber, i) * handlenumber(secondnumber, i) == handlenumber(thirdnumber,i):
				print i
				fail = False
				break
	if fail == True:
		print -1
			
