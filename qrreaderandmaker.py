from pyzbar.pyzbar import decode
from PIL import Image
d = decode(Image.open("./qcodefile.png"))
print(d[0].data.decode())
print(type(d))
