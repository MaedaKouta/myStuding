import string
import random
from Crypto.Cipher import AES

# 初期設定
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode()
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
).encode()

with open('seacret.txt', 'r') as f, open('complexity.dat', 'wb') as c:
    # 暗号化したいデータの準備
    cipher = AES.new(key, AES.MODE_CBC, iv)
    text = f.read()
    reflesh_length = AES.block_size - len(text.encode()) % AES.block_size
    text += chr(reflesh_length) * reflesh_length

    # 暗号化
    cipher_text = cipher.encrypt(text.encode()) # 暗号化
    c.write(cipher_text)

with open('complexity.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decryption_text = cipher2.decrypt(cipher_text)
    print('******復号化したデータ******\n')
    print(decryption_text[:-decryption_text[-1]].decode())