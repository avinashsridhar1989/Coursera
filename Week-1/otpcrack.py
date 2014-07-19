#!/usr/bin/env python
#  blitzavi89
# ----------------------------------------------------------------
# COURSERA CRYPTOGRAPHY-1 PROGRAMMING ASSIGNMENT-1 (Python 3.x)
# ----------------------------------------------------------------
import base64
def xor_TwoString(string1, string2) :
	output_string = ''
	output_string += chr(ord(string1) ^ ord(string2))
	return output_string

def xor_CheckSpace(xor_string_ref,index) :
	if (xor_string_ref >= 'a ' and xor_string_ref <= 'z') or (xor_string_ref >= 'A' and xor_string_ref <= 'Z') or xor_string_ref == '\0' :
		print (xor_string_ref + "  " + str(index))
		return True
	else :
		return False

def OTP_Crack(Cipher_Text_ref) :
	global Key
	global Key_Occupied
	Stack_Cipher = Cipher_Text_ref

# Iterate through all the ciphers
	for i in range(len(Stack_Cipher)) :
		cipher_test = Stack_Cipher[0]
		master_space_mask = [' ' for z in range(len(cipher_test))]
		count = 1

# Since we are operating on cipher stack, we need to ensure count is less than length of cipher stack
		while count < len(Stack_Cipher) :
			print ("count = " + str(count) + "\n")
			temp_space_mask = []
			cipher1 = Stack_Cipher[0]
			cipher2 = Stack_Cipher[count]
			xor_result = ''

# Determine cipher length based on which cipher string is smaller and calculate the XOR result of two cipher strings, which is same as message 1 XOR message 2
			if len(cipher1) > len(cipher2) :
				cipher_length = len(cipher2)
			else :
				cipher_length = len(cipher1)
			cipher1 = cipher1[:cipher_length]
			cipher2 = cipher2[:cipher_length]
			print (cipher1)
			print (cipher2)
# Calculate the XOR result of two cipher strings, which is same as message 1 XOR message 2
			for char_index in range(cipher_length) :
				xor_result += xor_TwoString(cipher1[char_index], cipher2[char_index])

# Check if there are spaces in the xor_result by calling xor_CheckSpace(). Accordingly manipulate temp_space_mask by setting it to ' ' or '\0'
			for char_index in range(cipher_length) :
				if xor_CheckSpace(xor_result[char_index],char_index) :
					temp_space_mask.append(' ')
				else :
					temp_space_mask.append('\0')

# We now check the temp_space_mask value with master_space_mask and set it to ' ' where there is a match. Rest we will set to '\0' in master_space_mask
			print (master_space_mask)
			print ('\n')
			print (temp_space_mask)
			print ('\n')
			for char_index in range(cipher_length) :
				if master_space_mask[char_index] != temp_space_mask[char_index] :
					master_space_mask[char_index] = '\0'
				else :
					pass
			count += 1
		print (len(master_space_mask))

		print (master_space_mask)
		print (cipher1)
		print ("\n")

		for i in range(len(cipher1)) :
			print (ord(cipher1[i]))

		for char_index in range(len(cipher1)) :
			if master_space_mask[char_index] == ' ' :
				if Key_Occupied[char_index] == '\0' :
					#if ord(cipher1[char_index + backlash_additional_counter]) == 92 and ord(cipher1[char_index + backlash_additional_counter + 1]) == 92 :
					Key[char_index] = chr(ord(cipher1[char_index]) ^ ord(' '))
					Key_Occupied[char_index] = chr(ord(cipher1[char_index]) ^ ord(' '))
						#backlash_additional_counter +=1				
					print ("MASTER SPACE MASK IS" + str(master_space_mask[char_index]))
					print (str(cipher1[char_index]))
					print (chr(ord(Key[char_index])) + "         " + str(char_index))
				else :
					pass
			else :
				pass
		Stack_Cipher = [Stack_Cipher.pop()] + Stack_Cipher

# XOR of two string is performed here
def strxor(str_a, str_b) :
	new_plaintext = []
	if len(str_a) > len(str_b) :
		for char_index in range(len(str_b)) :
			if str_b[char_index] != '\0' :
				new_plaintext.append(chr(ord(str_b[char_index]) ^ ord(str_a[char_index])))
			else :
				new_plaintext.append(' ')

	else :
		for char_index in range(len(str_a)) :
			new_plaintext += '\0'
			if str_b[char_index] != '\0' :
				new_plaintext.append(chr(ord(str_b[char_index]) ^ ord(str_a[char_index])))
			else :
				new_plaintext.append(' ')
	return new_plaintext

# Print the key here
def Key_Output() :
	global Key
	print (Key)

# Print the plaintext for each cipher string in the list of ciphers declared initially
def Plaintext_Output(Cipher_Text_ref) :
	global Key
	Plaintext_temp = []
	for i in range(len(Cipher_Text_ref)) :
		Plaintext_temp.append(strxor(Cipher_Text_ref[i], Key))
	print ("call" + str(i))
	return Plaintext_temp

# Do conversion of string from hex to ASCII
def Cipher_to_Hex(Cipher_Text_ref) :
	for list_element in range(len(Cipher_Text_ref)) :
		Cipher_Text_ref[list_element] = ''.join(chr(int(Cipher_Text_ref[list_element][i:i+2],16)) for i in range(0,len(Cipher_Text_ref[list_element]),2))
	return Cipher_Text_ref

# Function that prints the decrypted values for question and 10 encrypted messages
def Cracked() :
	global Cipher_Text
	global Key
	global Plaintext
	Plaintext = Plaintext_Output(Cipher_Text)
	for i in range(len(Plaintext)) :
		print (''.join(Plaintext[i]))
	Question_Text = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
	Question_Non_Hex = ''.join(chr(int(Question_Text[i:i+2],16)) for i in range(0,len(Question_Text),2))
	Answer = strxor (Question_Non_Hex, Key)
	print (''.join(Answer))

# main()
Cipher_Text_HexString = ['315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e', '234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f', '32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb', '32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa', '3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070', '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4', '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce', '315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3','271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027','466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83']
Key = []
Key_Occupied = []
# Append key with all null values initially in a list fashion
for key_iterate in range(1000) :
	Key.append('\0')
for i in range(1000) :
	Key_Occupied.append('\0')

Plaintext = []
Cipher_Text = Cipher_to_Hex(Cipher_Text_HexString)
string = Cipher_Text[0]
OTP_Crack(Cipher_Text)
Key_Output()
Cracked()

#main(), Additional decodes to fill in and determine remaining keys (based on above solution of Plaintext) :

Plaintext[0][0] = 'W'
Plaintext[1][2] = 'l'
Plaintext[1][7] = 'o'
Key[0] = chr(ord(Plaintext[0][0]) ^ int('31', 16))
Key[2] = chr(ord(Plaintext[1][2]) ^ int('02', 16))
Key[7] = chr(ord('r') ^ int('be', 16))
Key[14] = chr(ord('s') ^ int ('e6',16))
print (Key)
Cracked()

#String needs to be guessed and calculated so on...

		





	
