#import necessary modules 
from functools import reduce

# initialize the data
data = [1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0]

# assigning the number to the data
indexed_data = list(enumerate(data))

# creating an emptylist to store corresponding 1 value's position 
selected_bit = []

# for adding values to the parity list
for i,j in indexed_data:
	if j == 1:
		selected_bit.append(i)
# XOR -ing parity data to get the error bit
error_postition = reduce(lambda x,y: x^y, selected_bit)


# creating necessary functions
# function to reverse a list
def reverse_list(n):
	new_list = n[::-1]
	return new_list


# function to invert bit
def inverse(n):
	if n == 1:
		return 0
	else:
		return 1

# function to convert binary list to decimal list
def decimal(list):
	power = 0
	decimal_list = []
	for i in list:
		if int(i) == 1:
			decimal_list.append(2**power)
			power += 1
	return decimal_list



# converting error position to a list to iterate
encode_list = reverse_list(list(bin(error_postition)))
     #by the workings of python this list has unnecessary 0 and a be to remove it we use the following code
encode_list = encode_list[:-2]


print(f"This is initial data: {data}")

# creating function to encode the data

def encoder(encode_list, unencoded_data):
	data = unencoded_data
	position_data = decimal(encode_list)

	# to change the parity checking bit in the initial data
	for i in position_data:
		data[int(i)] = inverse(data[int(i)])
	print(f"This is encoded data: {data}")

# print out the position data where the error is 
	print(f"This is position data: {position_data}")


print(f"This is where the error: {error_postition}")


# calling the encoder function
encoder(encode_list, data)
