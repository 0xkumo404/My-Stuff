import os

def clear():
	os.system("clear")
def tobinary():
	clear()
	space_loop = False
	while space_loop != True:
	    	spaces = input("Do you want to add spaces [y/n]")
    		if spaces == "y": 
        		add_spaces = True
        		space_loop = True
    		elif spaces == "n": 
        		add_spaces = False 
        		space_loop = True
    		else:
        		print("\033[31mError\033[0m: Invalid input")
        		input("---press enter---")
	
	txt = input("\n---Enter Text---\n")
	print("---Translated Text---")
	
	for char in txt:
	    numtxt = ord(char)
	    binmidtxt = bin(numtxt)[2:]
	    bintxt = binmidtxt.zfill(8)
	    
	    if add_spaces == False:
	        print(bintxt, end="")
	    elif add_spaces == True:
	        print(bintxt, end=" ")
	print()
def totext():
	clear() 
	inputbintxt = input("---Enter Binary Code---\n")
	bintxt = inputbintxt.replace(" ", "")
	if len(bintxt) % 8 != 0:
		print("\033[31mError\033[0m: Invalid input")
		input("---press enter---")
		totext()
	else:
		print("\n---Translated Text---")
		for char in range(0, len(bintxt), 8):
			byte = bintxt[char : char + 8]
			numtxt = int(byte, 2)
			txt = chr(numtxt)
			print(txt, end="")
		print()
def main():
	clear()
	print("-----Select Mode-----\n")
	funct = input("1. txt >>> 101\n\n2. 101 >>> txt\n\n> ")
	if funct == "1":
		tobinary()
	elif funct =="2":
		totext()
	else:
		print("\033[31mError\033[0m: Invalid input")
		input("---press enter---")
		main()
if __name__ == "__main__":
	main()
