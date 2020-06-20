# importing required modules
import PyPDF2
import re

# creating a pdf file object
pdfFileObj = open('salary.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

dataCum = []

for k in range(1,78):

    # creating a page object
    pageObj = pdfReader.getPage(k)

    # extracting text from page
    extracted = pageObj.extractText()
    ex = extracted.split("\n \n")



    for i in range(len(ex)):
        ex[i] = re.sub("\n","",ex[i])

    for j in range(0,6):
        ex.pop(0)

    ex.pop(-1)

    dataCum = dataCum + ex

# closing the pdf file object
print(dataCum)
pdfFileObj.close()

