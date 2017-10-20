##Author Karle Sleith

#Adapted From: 
#https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
#https://stackoverflow.com/questions/2872381/how-to-read-a-file-byte-by-byte-in-python-and-how-to-print-a-bytelist-as-a-binar

import gzip
import PIL.Image as pil
import numpy as np

cnt = 0


##Method to read images from File
def read_images_from_file(filename):
	with gzip.open(filename, 'rb')as f:
		magic = f.read(4)
		magic = int.from_bytes(magic,'big')
		print('Magic is : ', magic)
		
		noimg = f.read(4)
		noimg = int.from_bytes(noimg,'big')
		print('No: of Img : ', noimg)
		
		norow = f.read(4)
		norow = int.from_bytes(norow,'big')
	
		
		nocol = f.read(4)
		nocol = int.from_bytes(nocol,'big')
	
		images=[]
		
		for i in range(noimg):
			rows =[]
			for r in range(norow):
				cols =[]
				for c in range(nocol):
					cols.append(int.from_bytes(f.read(1),'big'))
				rows.append(cols)
			images.append(rows)
			
	return images
	

def printImage(image):

	for i in range(28):
		img_rep = ""
		for j in range(28):
			if image[i][j] <=128:
				img_rep +='.'
			else:
				img_rep += '#'
		
		print(img_rep)
			
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')


##Print The image to the cmd
# for image in test_images:
	# for row in test_images[cnt]:
		# for col in row:
			# print('.' if col <= 127 else '#', end='' )
		# print()	
	# cnt = cnt+ 1
		
		
	
	
##Printing a Image to a file
for image in train_images:	
	img= train_images[cnt]
	img = np.array(img)
	img = pil.fromarray(img)
	img = img.convert('RGB')
	#img.show()
	img.save("./TrainImgs/train-"+str(cnt)+".png")
	cnt = cnt+1;

print('DONE!')

	






