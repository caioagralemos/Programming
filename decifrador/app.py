from decode import decode
from encode import encode

while True:
    doe = int(input("press 1 to encode or 2 to decode: "))

    if doe == 1 or doe == 2:
        break

if doe == 1:
    encode()
elif doe == 2:
    decode()