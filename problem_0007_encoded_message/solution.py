def solve(msg):
	# initialize result
	result = []
	sz = len(msg)

	for i in range(0, sz):
		result.append(0)

	if int(msg[0]) == 0:
		return 0

	result[0] = 1

	for i in range(1, sz):
		if int(msg[i]) == 0:
			if int(msg[i-1]) > 2:
				return 0
			else:
				result[i] = result[i-2]
		else:
			if int(msg[i-1:i+1]) < 27:
				if i - 2 < 0:
					result[i] = 1 + result[i-1]
				else:
					result[i] = result[i-2] + result[i-1]
			else:
				if i - 2 < 0:
					result[i] = 1
				else:
					result[i] = result[i-2]

	return result[sz-1]

if __name__=="__main__":
	assert solve("0123") == 0
	assert solve("1") == 1
	assert solve("12") == 2
	assert solve("123") == 3
	assert solve("1230") == 0
	assert solve("120") == 1
