import datetime

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from EPD import EPD


class EInkImage:

    def __init__(self, resources_dir):
	self.img = Image.new('L', (176, 264))
    	self.d = ImageDraw.Draw(self.img)
    	self.d.rectangle(xy=(0, 0, 176, 264), fill=255)
    	self.d.rectangle(xy=(0, 0, 176, 17), fill=200)
	self.scheduleCount = 0

        self.font08 = ImageFont.load(resources_dir + "/helvO08.pil")
        self.fontB08 = ImageFont.load(resources_dir + "/helvB08.pil")
        self.font10 = ImageFont.load(resources_dir + "/timR10.pil")
        self.fontB10 = ImageFont.load(resources_dir + "/timB10.pil")

    def header(self, booked_desk=''):
        """
        :param booked_desk: string
        """
        self.d.rectangle((0, 0, 176, 22), fill=0)
        self.d.text((5, 3), datetime.date.today().strftime('%d-%b-%Y'), fill=255, font=self.fontB08)
        if booked_desk != '':
            self.d.text((115, 3), booked_desk, fill=255, font=self.fontB08)

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
            self.d.rectangle((0, offset + 2, 176, offset + 40), fill=255)

        # Place the text in the scheduled item
        self.d.text((5, offset + 3), text, fill=0, font=self.fontB10)

        # Place the location of the scheduled item if one specified
        if location != '':
            self.d.text((5, offset + 25), location, font=self.fontB08)

        # Place the start and stop times of the scheduled items if there are any in
        # the bottom right hand corner ofthe scheduled item
        if start != '0' and stop != '0':
            self.d.text((105, offset + 25), start + " - " + stop, font=self.fontB08)
        elif start != '0':
            self.d.text((145, offset + 25), start, font=self.fontB08)

        self.d.line((0, offset + 41, 176, offset + 41), fill=100)

    def add_header(self, title):
        """
        :param title: string
        """
        self.header(title)

    def add_item(self, title, start='0', end='0', location='', important=0):
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
        # fin.save("halibut.png", 'png')

        epd = EPD()
        epd.clear()
        epd.display(fin)
        epd.update()
