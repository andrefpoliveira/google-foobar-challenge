# Python 3.6
import base64

message = "<message>"

key = "<username>"

result = []
for i, c in enumerate(base64.b64decode(message)):
    result.append(chr(c ^ ord(key[i % len(key)])))

print(''.join(result))
