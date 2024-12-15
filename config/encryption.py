import yaml
import base64


def read_key_from_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config['aes256_key']

class Encrypter:
    def __init__(self):
        key = read_key_from_config("config.yaml")
        self.key = key.encode('utf-8')

    def encrypt_decrypt(self, data):
        key_len = len(self.key)
        return bytes([data[i] ^ self.key[i % key_len] for i in range(len(data))])

    def encode(self, data):
        encrypted_data = self.encrypt_decrypt(data.encode('utf-8'))
        return base64.b64encode(encrypted_data).decode('utf-8')

    def decode(self, encoded_data):
        encrypted_data = base64.b64decode(encoded_data)
        decrypted_data = self.encrypt_decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')

