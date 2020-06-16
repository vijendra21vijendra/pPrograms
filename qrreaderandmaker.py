from pyzbar.pyzbar import decode
from PIL import Image
# d = decode(Image.open("./qcodefile.png"))
d = decode(Image.open("./myinf.png"))
print(d[0].data.decode())
print(type(d))
