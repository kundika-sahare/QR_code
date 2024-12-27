'''import qrcode as qr
img=qr.make("https://www.youtube.com")
img.save("youtube.png")'''

import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("http://www.youtube.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="pink")
img.save("youtube.png")