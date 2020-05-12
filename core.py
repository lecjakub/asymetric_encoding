import math
import random
import algorithms


def encrypt_file(input_file , output_file, publicKey):
    with open(input_file, "rb") as text_file:
        bytes_stream = text_file.read()
        encoded = algorithms.encrypt_rsa(bytes_stream, publicKey)

        with open(output_file, 'wb+') as encoded_file:
            encoded_file.write(encoded)


def decrypt_file(input_file : str, output_file: str, privateKey):
    with open(input_file,"rb") as encoded_file:
        encoded = encoded_file.read()
        decoded = algorithms.decrypt_rsa(encoded, privateKey)
        with open(output_file,'wb+') as decoded_file:
            decoded_file.write(decoded)
