from Crypto.Hash import MD5
from Crypto.Hash import SHA256

#hash = MD5.new()
#hash2 = SHA256.new()
hash = MD5.new(b'123456')
hash2 = SHA256.new(b'123456')
hash.update(b'hola')
hash2.update(b'hola')
print(hash.hexdigest())
print(hash2.hexdigest())