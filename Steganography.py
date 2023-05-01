#Steganography-data is hidden in plain sight
#Steganography is the art and science of embedding secret messages in cover message in such a way that no one, apart from sender and intended recipient, suspects the existamce of the mssg
#Steganography-Steganos(concealed or hidden)+graphen(drawing/writing)
#cover media-means by which u are hiding image
#steganography types:text,image,audio,video,network,email

#Charcteristics of Steganographic techniques:transparency(there must be no distortion in image after we hide the mssg),robustness(the image does not loose info even if the media undergoes some damage like cropping,filtering),tamper resistance(the ability of a device to defend against a threat that has the objective to compromise the device and or the data processed by the device)

"""
Basic Steganographic model:

cover file(X), secret message(M),Key(K)-->steganographic encoder{f(X,M,K)}-->(Stego object)-->communication channel-->(Stego object)-->Steganographic Decoder(stego object,Key)-->Secet message(M)
Key is optional-its for extra security
Stego object just look likes the cover file
"""

"""
Steganographic model:with encryption

more safe
message,Key-->encrytping algorithm-->(cypher text)-->cyphertext,stegokey,cover file-->steganographic encoder-->(stego object)-->communication channel-->(stego object)-->stgokey,stego object-->steganographic decoder-->cypher text-->cyphertext,key-->decrypting algo-->mssg
"""

#LSB steganography-least significant bit steganography
#if we change most significant bit, it will have a larger imapct on final value. If we change LSB, the impact on final value is very less.
"""
Value:255=1111 1111
Value after changing msb:0111 1111=127 so change in bytes is 99.9999%
value after changing lsb:1111 1110=254 so change in bytes is 0.000002%
"""
#lsb steganography involves overwriting the bit with the lowest arithmetic value

"""
Steps to encode the text into image:
1-Loads an image and looks at each pixels in hexadecimal value
2-convets secret text into bits and stores them in LSB of pixels value
3-A delimiter is added to the end of the edited pixel values

Steps to decode the text from image:
4-while retriving all the 0's and 1's extracted until delimiter is found. Extracted bits are converted into string(secret mssg)
"""

# Python program implementing Image Steganography



# PIL module is used to extract pixels of image and modify it

from PIL import Image

# Convert encoding data into 8-bit binary form using ASCII value of characters

def genData(data):
    # list of binary codes of given data
	newd = []
	for i in data:
	    newd.append(format(ord(i), '08b'))
	return newd
	

# Pixels are modified according to the 8-bit binary data and finally returned
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)# returns the iterator object, it is used to convert an iterable to the iterator#it runs only once
	
	for i in range(lendata):

		# Extracting 3 pixels at a time
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]
		

		# Pixel value should be made odd for 1 and even for 0
		for j in range(0, 8):
			
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
		
		# Eighth pixel of every set tells whether to stop ot read further. 0 means keep reading; 1 means the message is over.
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):

		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1

# Encode data into image
def encode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = input("Enter data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	new_img_name = input("Enter the name of new image(with extension) : ")
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

# Decode the data in the image
def decode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')

	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]

		# string of binary data
		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data


a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
if (a == 1):
	encode()

elif (a == 2):
	print("Decoded Word : " + decode())


