def convFr2Gr(ch):
	nouvC = ""
	for car in ch:
		code = ord(car)
		if (code == 65) or (code == 97):
			code = 945
		elif (code == 66) or (code == 98):
			code = 946
		elif (code == 67) or (code == 99):
			code = 947
		elif (code == 68) or (code == 100):
			code = 948
		elif (code == 69) or (code == 101):
			code = 949
		elif (code == 70) or (code == 102):
			code = 950
		elif (code == 71) or (code == 103):
			code = 951
		elif (code == 72) or (code == 104):
			code = 952
		elif (code == 73) or (code == 105):
			code = 953
		elif (code == 74) or (code == 106):
			code = 954
		elif (code == 75) or (code == 107):
			code = 955
		elif (code == 76) or (code == 108):
			code = 956
		elif (code == 77) or (code == 109):
			code = 957
		elif (code == 78) or (code == 110):
			code = 958
		elif (code == 79) or (code == 111):
			code = 959
		elif (code == 80) or (code == 112):
			code = 960
		elif (code == 81) or (code == 113):
			code = 961
		elif (code == 82) or (code == 114):
			code = 962
		elif (code == 83) or (code == 115):
			code = 963
		elif (code == 84) or (code == 116):
			code = 964
		elif (code == 85) or (code == 117):
			code = 965
		elif (code == 86) or (code == 118):
			code = 966
		elif (code == 87) or (code == 119):
			code = 967
		elif (code == 88) or (code == 120):
			code = 968
		elif (code == 89) or (code == 121):
			code = 969
		elif (code == 90) or (code == 122):
			code = 970
		nouvC = nouvC + chr(code)
	return nouvC

def convGr2Fr(ch):
	nouvC = ""
	for car in ch:
		code = ord(car)
		if code == 945:
			code = 65
		elif code == 946:
			code = 66
		elif code == 947:
			code = 67
		elif code == 948:
			code = 68
		elif code == 949:
			code = 69
		elif code == 950:
			code = 70
		elif code == 951:
			code = 71
		elif code == 952:
			code = 72
		elif code == 953:
			code = 73
		elif code == 954:
			code = 74
		elif code == 955:
			code = 75
		elif code == 956:
			code = 76
		elif code == 957:
			code = 77
		elif code == 958:
			code = 78
		elif code == 959:
			code = 79
		elif code == 960:
			code = 80
		elif code == 961:
			code = 81
		elif code == 962:
			code = 82
		elif code == 963:
			code = 83
		elif code == 964:
			code = 84
		elif code == 965:
			code = 85
		elif code == 966:
			code = 86
		elif code == 967:
			code = 87
		elif code == 968:
			code = 88
		elif code == 969:
			code = 89
		elif code == 970:
			code = 90
		nouvC = nouvC + chr(code)
	return nouvC

if __name__ == '__main__':    ####@@PROGRAMME@DE@TEST@@####
	print(convFr2Gr("Salut"))
	print(convGr2Fr("σαμυτ"))
