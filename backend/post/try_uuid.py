import uuid
import hashlib
""" uuid_val = uuid.uuid4()
uuid_str = str(uuid_val).encode('utf-8')
md5 = hashlib.md5()
md5.update(uuid_str)
random_str = md5.hexdigest()

print(uuid_str)
print(type(uuid_val))
print(type(uuid_str))
print(random_str)
print(type(random_str)) """

def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()
