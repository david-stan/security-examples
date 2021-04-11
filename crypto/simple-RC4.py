## implementstion of a pseudo random generator
## which returns keystream, given a 32-byte key k
def get_prg(plaintext_size, k):
    tempKey = [char for char in k];
    keystream = [];
    i = j = counter = 0;
    while (counter < plaintext_size):
        i = (i + 1) % 32;
        j = (j + ord(tempKey[i])) % 32;

        temp = tempKey[i];
        tempKey[i] = tempKey[j];
        tempKey[j] = temp;

        nchar = (ord(tempKey[i]) + ord(tempKey[j])) % 32
        keystream.append(tempKey[nchar]);
        
        counter += 1

    return ''.join(keystream);


def fake_rc4(plaintext, keystream):
    return perform_xor(plaintext, keystream);

## performs bitwise xor on the two charstreams
def perform_xor(charstream1, charstream2):
    bytestream1, bytestream2 = charstream1.encode(), charstream2.encode();
    bytelist = [chr(x ^ y) for x, y in zip(bytestream1, bytestream2)];
    return ''.join(bytelist);


## given the 32-byte string k, representing the key
## generate ciphertext based on that key k, using the custom prg
def encrypt(plaintext, k):
    plaintext_size = len(plaintext);
    keystream = get_prg(plaintext_size, k);
    return fake_rc4(plaintext, keystream);