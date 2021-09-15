#!/usr/bin/env python
# coding=utf-8
from fpdf import FPDF
#from pgmagick import Image
from PIL import Image
import os


def makePdf(pdfFileName,listPages):

    listPages = listPages
    listPages.sort()
    cover = Image.open(listPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(page,0,0)

    pdf.output(pdfFileName, "F")


makePdf("result.pdf", [imgFileName for imgFileName in os.listdir('.') \
                       if imgFileName.endswith("png") ] )
#for imgFileName in os.listdir('.'):
#    if imgFileName.endswith("png"):
#        if imgFileName.sort():
#            print( imgFileName )
