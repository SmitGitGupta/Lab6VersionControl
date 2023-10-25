def encode(num):
	line1 = str(num)
	line2 = ""
	for i in range(0, len(line1)):
		a = int(line1[i]) + 3
		if a > 9:
			a -= 10
		line2 += str(a)
	return line2



def main():
	while True:
		print("0. Exit\n1. Encode\n2. Decode")
		op = int(input("How would you like to proceed: "))
		if op == 0:
			break
		elif op == 1:
			line = str(input("Enter number: "))
			print(encode(line))
	
	pass

if __name__ == "__main__":
	main()
