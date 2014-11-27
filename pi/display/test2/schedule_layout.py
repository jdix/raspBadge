import datetime

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from EPD import EPD


class EInkImage:
    img = Image.new('L', (176, 264))
    d = ImageDraw.Draw(img)
    d.rectangle(xy=(0, 0, 176, 264), fill=255)
    d.rectangle(xy=(0, 0, 176, 17), fill=200)

    scheduleCount = 0

    def __init__(self, resources_dir):
        self.font08 = ImageFont.load(resources_dir + "/helvO08.pil")
        self.fontB08 = ImageFont.load(resources_dir + "/helvB08.pil")
        self.font10 = ImageFont.load(resources_dir + "/timR10.pil")

    def header(self, booked_desk=''):
        """
        :param booked_desk: string
        """
        self.d.text((5, 3), datetime.date.today().strftime('%d-%b-%Y'), fill=0, font=self.font08)
        if booked_desk != '':
            self.d.text((125, 3), booked_desk, fill=0, font=self.font08)

        self.d.rectangle((0, 18, 176, 22), fill=0)

    def scheduled_item(self, placement, text='', start='0', stop='0', location='', important=0):
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
            self.d.rectangle((0, offset + 2, 176, offset + 40), fill=210)
        else:
            self.d.rectangle((0, offset + 2, 176, offset + 40), fill=235)

        if start != '0' and stop != '0':
            self.d.text((105, offset + 3), start + " - " + stop, font=self.font08)
        elif start != '0':
            self.d.text((145, offset + 3), start, font=self.font08)

        self.d.text((5, offset + 3), text, fill=0, font=self.font10)
        self.d.line((0, offset + 41, 176, offset + 41), fill=100)

    def add_header(self, title):
        """
        :param title: string
        """
        self.header(title)

    def add_item(self, title, location='', start='0', end='0', important=0):
        """
        :param title: string
        :param location: string
        :param start: string
        :param end: string
        :param important: int
        """
        self.scheduled_item(placement=self.scheduleCount, text=title, start=start, stop=end, location=location,
                            important=important)
        self.scheduleCount += 1

    def render(self):
        fin = self.img.rotate(90)

        epd = EPD()
        epd.clear()
        epd.display(fin)
        epd.update()