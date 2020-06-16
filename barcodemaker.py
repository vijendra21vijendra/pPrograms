import barcode  # pip install python-barcode
from barcode.writer import ImageWriter

clas = barcode.get_barcode_class('code39')
inst = clas("Vijen1234c", writer=ImageWriter())

inst.save("mypassword")

# if we want to make svg file then don't give writer parameter
