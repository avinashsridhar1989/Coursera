from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

blk_size = AES.block_size

# Function to perform AES CBC decryption with PKCS-5 Paddind
def Decrypt_CBC_PKCS5(ciphertext, key) :
	plaintext = []
	num_cipher = len(ciphertext)
	for index in range(num_cipher) :
		iv = ciphertext[index][:blk_size]
		new_cipher = ciphertext[index][blk_size:]
		cipher = AES.new(key[index], AES.MODE_CBC, iv)
		plaintext.append((cipher.decrypt(new_cipher)))
		plaintext[index] = str(plaintext[index], 'ascii')

# Pad logic from http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
		plaintext[index] = (plaintext[index][:-ord(plaintext[index][-1])])
	return plaintext

# Function to perform AES CTR decryption using Counter mechanism. We are using the Counter functionality from Crypto.Util.Counter
def Decrypt_CTR(ciphertext, key) :
	plaintext = []
	num_cipher = len(ciphertext)
	for index in range(num_cipher) :
		iv = ciphertext[index][:blk_size]
		ctr = Counter.new(128, initial_value = int(binascii.hexlify(iv), 16))
		new_cipher = ciphertext[index][blk_size:]

# counter = ctr is a callback function here
		cipher = AES.new(key[index], AES.MODE_CTR, counter = ctr)
		plaintext.append(cipher.decrypt(new_cipher))
		plaintext[index] = str(plaintext[index], 'ascii')
	return (plaintext)

# main
if __name__ == "__main__" :

# Questions 1 and 2	
	key1 = ["140b41b22a29beb4061bda66b6747e14", "140b41b22a29beb4061bda66b6747e14"]
	ciphertext1 =["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"]
	key1_unhex = [binascii.unhexlify(element) for element in key1]
	ciphertext1_unhex = [binascii.unhexlify(element) for element in ciphertext1]
	plaintext1 = Decrypt_CBC_PKCS5(ciphertext1_unhex, key1_unhex)
	print ("\nAnswers for Q1 and Q2 :\n")
	print (plaintext1)

# Questions 3 and 4
	key2 = ["36f18357be4dbd77f050515c73fcf9f2", "36f18357be4dbd77f050515c73fcf9f2"]
	ciphertext2 = ["69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"]
	key2_unhex = [binascii.unhexlify(element) for element in key2]
	ciphertext2_unhex = [binascii.unhexlify(element) for element in ciphertext2]
	plaintext2 = Decrypt_CTR(ciphertext2_unhex, key2_unhex)
	print ("\nAnswers for Q3 and Q4 :\n")
	print (plaintext2, "\n")