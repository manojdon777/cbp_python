def swapCharacters(s, B, C):
	N = len(s)
	C = C % N
	s = list(s)
	for i in range(B):
		s[i], s[(i + C) % N] = s[(i + C) % N], s[i]
	return ''.join(s)

def isEqual(string1, string2):
    if string1 is string2:
          print('Strings are equal')
    else:
          print('Strings are not equal')


if __name__ == '__main__':
    s = swapCharacters("ABCDEF", 3, 4)
    print(s)

    t = isEqual('Abc', 'Abc')
    print(t)




