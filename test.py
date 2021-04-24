def add(str1, str2):
    # Before proceeding further,
    # make sure length of str2 is larger.
    if (len(str1) > len(str2)):
        str1, str2 = str2, str1
 
    # Take an empty string for
    # storing result
    str3 = ""
 
    # Calculate length of both string
    n1,n2 = len(str1), len(str2)
 
    # Reverse both of strings
    str1,str2 = str1[::-1], str2[::-1]
 
    carry = 0;
    for i in range(n1):         
        # Do school mathematics, compute
        # sum of current digits and carry
        sum = ((ord(str1[i]) - ord('0')) +
              ((ord(str2[i]) - ord('0')) + carry))
        str3 += chr(sum % 10 + ord('0'))
 
        # Calculate carry for next step
        carry = int(sum / 10)
 
    # Add remaining digits of larger number
    for i in range(n1, n2):
        sum = ((ord(str2[i]) - ord('0')) + carry)
        str3 += chr(sum % 10 + ord('0'))
        carry = int(sum / 10)
 
    # Add remaining carry
    if (carry):
        str3 += chr(carry + ord('0'))
 
    # reverse resultant string
    str3 = str3[::-1]
 
    return str3

if __name__ == '__main__':
	with open('test.txt') as f:
		lines = f.readlines()

	string = "0"
	for line in lines:
		string = add(string,line.strip())
	print(string)
