from xhtml2pdf import pisa

from wand.image import Image
from PIL import Image as PImage
from PIL import ImageOps as PImageOps

from EPD import EPD


sourceFile = "test.html"
pdfOutputFile = "test.pdf"
imageOutput = "test.png"


def convertHtmlToPdf(sourceFile, pdfOutputFile, imageOutput):
    resultFile = open(pdfOutputFile, "w+b")
    sourceHtml = open(sourceFile, "r")
    pisaStatus = pisa.CreatePDF(
        src=sourceHtml,
        dest=resultFile)
    resultFile.close()
    sourceHtml.close()

    with Image(filename=pdfOutputFile) as img:
        img.save(filename=imageOutput)

    return pisaStatus.err


def display_file(file_name):
    epd = EPD()
    epd.clear()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version))
    # Open image and convert to black and white
    image = PImage.open(file_name)
    image = PImageOps.grayscale(image)

    # Cropping the image as too large to display on panel.
    # Note: the height and width are backwards on purpose as I am forcing it to portrait and rotate the image a bit further down
    # (I couldn't get xhtml2pdf to recognise the flag in the html style sheet, but could be the version of the lib...)
    cropped = image.crop((0, 0, epd.height, epd.width))
    bw = cropped.convert("1", dither=PImage.FLOYDSTEINBERG)
    bw = bw.rotate(90)

    epd.display(bw)
    epd.update()


if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceFile, pdfOutputFile, imageOutput)
    display_file(imageOutput)
