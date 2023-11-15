import hashlib

filename = "image.jpg"

with open(filename,"rb") as f:

	file_data = f.read()

hashed_image = hashlib.sha3_256(file_data)
print("sha3_256 image: ",hashed_image.hexdigest())
