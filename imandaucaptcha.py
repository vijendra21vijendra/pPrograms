from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
img = ImageCaptcha()
audio = AudioCaptcha()
# img.write("xy12", 'xy.png')

data = audio.generate('123456789')
audio.write('1234', '2.mp3')
