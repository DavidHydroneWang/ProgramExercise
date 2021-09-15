#!/usr/bin/env python
# coding=utf-8
from fpdf import FPDF
from pgmagic import Image
import os


def makePdf(pdfFileNname,listPages):

    cover = Image.open(listPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(page,0,0)

    pdf.output(pdfFileName, "F")


makePdf("result.pdf", [ imgFileName for imgFileName in os.lisdir('.')  if imgFileName.endwith("png") ])
