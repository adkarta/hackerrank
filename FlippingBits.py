inp = 3
#inp = input()

cases = [2147483647,1,0]

for case in range (0, inp):
    # print input()
    s_bit= bin(cases[case]).lstrip('0b').zfill(32)
    
    s_result = ""
    for letter in s_bit:
    	if letter == "1":
    		s_result += "0"
    	else:
    		s_result += "1"

    print int(s_result,2)