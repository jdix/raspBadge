import datetime

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from EPD import EPD


__author__ = 'james'

img = Image.new('L', (176, 264))
d = ImageDraw.Draw(img)
d.rectangle(xy=(0, 0, 176, 264), fill=(255))
d.rectangle(xy=(0, 0, 176, 17), fill=(200))

font08 = ImageFont.load("helvO08.pil")
fontB08 = ImageFont.load("helvB08.pil")
font10 = ImageFont.load("timR10.pil")


def header(bookedDesk=''):
    d.text((5, 3), datetime.date.today().strftime('%d-%b-%Y'), fill=(0), font=font08)
    if bookedDesk != '':
        d.text((125, 3), bookedDesk, fill=(0), font=font08)

    d.rectangle((0, 18, 176, 22), fill=(0))


def scheduled_item(placement, text='', start='0', stop='0', location='', important=0):
    """
    :param placement: int
    :param text: string
    :param start: string
    :param stop:  string
    :param location: string
    :param important: int
    """
    offset = 20 + (placement * 40)

    if important == 1:
        d.rectangle((0, offset + 2, 176, offset + 40), fill=(210))
    else:
        d.rectangle((0, offset + 2, 176, offset + 40), fill=(235))

    if start != '0' and stop != '0':
        d.text((105, offset + 3), start + " - " + stop, font=font08)
    elif start != '0':
        d.text((145, offset + 3), start, font=font08)

    d.text((5, offset + 3), text, fill=0, font=font10)
    d.line((0, offset + 41, 176, offset + 41), fill=(100))


header('B4J.F45.2')
scheduled_item(0, 'Sit in Meeting', start='12:00', stop='13:00', important=1)
scheduled_item(1, 'Get Coffee', start='13:30')
scheduled_item(2, 'Call Wife', important=1)
scheduled_item(3, 'Brainstorm RaspBadge')
scheduled_item(4)
scheduled_item(5)

# import cStringIO
# s = cStringIO.OutputType.StringIO()
fin = img.rotate(90)

epd = EPD()
epd.clear()
epd.display(fin)
epd.update()

# fin.save("halibut.png", 'png')

# in_memory_file = s.getvalue()
