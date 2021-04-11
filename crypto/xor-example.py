ciphertext1 = b'\x56\x10\x34\xf8';

keystream1 = b'\x34\x71\x58\x94';
keystream2 = b'\x35\x71\x5f\x9d';
keystream3 = b'\x26\x7f\x51\x95';

ciphertext2 = b'\x46\x06\x3e\xf3';

def perform_xor(bytestream1, bytestream2):
	bytelist = [chr(x ^ y) for x, y in zip(bytestream1, bytestream2)];
	return ''.join(bytelist);

def perform_xor_simpl(bytestream1, bytestream2):
	for x, y in zip(bytestream1, bytestream2):
		print(x, y)

#print(perform_xor(ciphertext1, keystream3))
#print(perform_xor(ciphertext2, keystream3))

def perform_xor_string(string1, string2):
    print(string1[0], string2[0]);
    bytearr1, bytearr2 = string1.encode(), string2.encode();
    print(bytearr1[0], bytearr2[0])
    bytelist = [chr(x ^ y) for x, y in zip(bytearr1, bytearr2)];
    return ''.join(bytelist)

#print(perform_xor_string('alo', 'kol'))

stream1 = '\x61'
stream2 = '\x6c'

print(perform_xor_string(stream1, stream2))
