import base64
encoded = 'eWEgYnVzcXVlIGxvcyBhbHF1aWxlcmVzIGRlIHJhbW9z'
data= base64.b64decode(encoded)
print(data)
