import hashlib
m = hashlib.md5()
m.update(b"message for cryptographic signature")
print(m.digest())
