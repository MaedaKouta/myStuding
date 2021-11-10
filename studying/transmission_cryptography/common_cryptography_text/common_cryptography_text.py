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
cipher = AES.new(key, AES.MODE_CBC, iv)

# 暗号化したいデータの準備
text = 'seacret data'
reflesh_length = AES.block_size - len(text) % AES.block_size
text += chr(reflesh_length) * reflesh_length
print('暗号化したいデータ :', text)

# 暗号化
cipher_text = cipher.encrypt(text.encode()) #暗号化
print('暗号化されたデータ :', cipher_text)

# 復号
cipher2 = AES.new(key, AES.MODE_CBC, iv)
decryption_text = cipher2.decrypt(cipher_text)
print('復号したデータ :', decryption_text[:-decryption_text[-1]])