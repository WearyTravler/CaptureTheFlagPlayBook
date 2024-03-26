import brotli

def decode_brotli(encoded_data):
    return brotli.decompress(encoded_data)

# Example usage: Decode Brotli-encoded data
with open('image.br', 'rb') as file:
    encoded_data = file.read()

decoded_data = decode_brotli(encoded_data)

# Now you have the decoded data, you can write it to a file or process it further
with open('decoded_image.jpg', 'wb') as file:
    file.write(decoded_data)


#CHAT GPT CODE, I'm sorry but I must give credit where credit is due.
#It worked though, suprisingly...
