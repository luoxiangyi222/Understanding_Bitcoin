# The code is initially published in the book <<Mastering Bitcoin>>
# Modified by me slightly.

import bitcoin as btc

# ############### Private key #########################
valid_private_key = False
private_key = None
decoded_private_key = None

while not valid_private_key:
    # Generate a private key and check whether it is within the range
    private_key = btc.random_key()  # here the private key is a string

    decoded_private_key = btc.decode_privkey(private_key, 'hex') # convert it to the integer format

    valid_private_key = 0 < decoded_private_key < btc.N
    print('Private key, a string: \n' + private_key)
    print('Private key, an integer: \n' + str(decoded_private_key))
    print('Within valid range?: \n' + str(valid_private_key))

# Convert private key into WIF format
# noted that private key WIF add 0x80 prefix
wif_encoded_private_key = btc.encode_privkey(decoded_private_key, 'wif')
print('Private key (WIF): \n' + wif_encoded_private_key)

# Add suffix '01' to indicate a compressed private key
compressed_private_key = private_key + '01'
print('Compressed private key (hex): \n' + compressed_private_key )
# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = btc.encode_privkey(btc.decode_privkey(compressed_private_key,'hex'), 'wif')
print('Private key (WIF-compressed): \n' + wif_compressed_private_key)


# ############### Public key #########################
# Multiply the EC generator point G with the private key to get a public key point
public_key = btc.multiply(btc.G, decoded_private_key)
print('Public key (x, y): \n' + str(public_key))
# Encode as hex, prefix 04
hex_encoded_public_key = btc.encode_pubkey(public_key, 'hex')
print('Public key (hex): \n' + hex_encoded_public_key)
# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key

if public_key_y % 2 == 0:
    compressed_prefix = '02'
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + btc.encode(public_key_x, 16)
print('Compressed Public Key (hex): \n' + hex_compressed_public_key)

# ############### Bitcoin Address #########################
# Generate bitcoin address from public key
print('Bitcoin Address (b58check): \n' + btc.pubkey_to_address(public_key))
print('Bitcoin Address (b58check): \n' + btc.pubkey_to_address(hex_compressed_public_key))
