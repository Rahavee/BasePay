# importing required modules

import PyPDF2
import re


def main():
    # creating a pdf file object
    pdfFileObj = open('salary.pdf', 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    dataCum = []

    for k in range(1, 78):

        # creating a page object
        pageObj = pdfReader.getPage(k)

        # extracting text from page
        extracted = pageObj.extractText()
        ex = extracted.split("\n \n")

        for i in range(len(ex)):
            ex[i] = re.sub("\n", "", ex[i])

        for j in range(0, 6):
            ex.pop(0)

        ex.pop(-1)

        dataCum = dataCum + ex

    dataCum.remove("Herrera,Diego")
    dataCum[289] = "Information Tech Professional"
    del dataCum[290]
    dataCum[544] = "Administrative Professional"
    del dataCum[545]
    dataCum[559] = "Assistant Professor (COM)"
    del dataCum[560]
    dataCum[1240] = "Information Tech Professional"
    del dataCum[1241]
    dataCum[1711] = "Academic Srvcs Professional"
    del dataCum[1712]
    dataCum[1860] = "Carthew, Jessica Jane"
    del dataCum[1861]
    dataCum[2010] = "Cheung, Katharine Lana"
    del dataCum[2011]
    del dataCum[2056]
    dataCum[2158] = "Clinical Engineer"
    del dataCum[2159]
    dataCum[3051] = "Dimick, Ellen Madeline"
    del dataCum[3052]
    dataCum[3804] = " Fitzpatrick, George Matthew"
    del dataCum[3805]
    dataCum[4204] = "Assistant Professor (COM)"
    del dataCum[4205]
    dataCum[4251] = "Gervais,Joseph Robert"
    del dataCum[4252]
    dataCum[4444] = "Assistant Professor (COM)"
    del dataCum[4445]
    dataCum[4732] = "Admin f Analyst/Planner Sr"
    del dataCum[4733]
    del dataCum[5578]
    dataCum[5736] = "Johnson,Douglas Ian"
    del dataCum[5737]
    dataCum[5818] = "Post Doctoral Associate"
    del dataCum[5819]
    dataCum[6448] = "Academic Srvcs Professional"
    del dataCum[6447]
    del dataCum[6745]
    dataCum[7660] = "Assistant Professor (COM)"
    del dataCum[7661]
    dataCum[7926] = "Morgan-Parmett,Helen"
    del dataCum[7927]
    dataCum[8257] = "Custodial Maintenance Spec Sr"
    del dataCum[8258]
    dataCum[8541] = "Ossareh,Hamid Reza"
    del dataCum[8542]
    del dataCum[9016]
    dataCum[9445] = "Technical Support Specialist"
    del dataCum[9446]
    dataCum[9685] = "Custodial Maintenance Spec"
    del dataCum[9686]
    del dataCum[9934]
    del dataCum[10025]
    del dataCum[10684]
    del dataCum[10699]
    dataCum[10789] = "Assistant Professor (COM)"
    del dataCum[10790]
    dataCum[10867] = "Library f Assistant Prof"
    del dataCum[10868]
    del dataCum[10993]
    dataCum[11332] = "Associate Professor"
    del dataCum[11333]
    dataCum[11347] = "Assistant Professor"
    del dataCum[11348]
    dataCum[11362] = "Information Tech Professnl Sr"
    del dataCum[11363]
    dataCum[11901] = "Wallace III,Harold James"
    del dataCum[11902]
    dataCum[12057] = "Weimersheimer,Peter Edward"
    del dataCum[12058]
    dataCum[12301] = "Clinical Practice Phys (COM)"
    del dataCum[12302]
    dataCum[12330] = "Williams,Clayton Jack"
    del dataCum[12331]
    dataCum[12555] = "Youlen,Katherine Elizabeth"
    del dataCum[12556]
    dataCum[12601] = "Biomedical Equipment Tech"
    del dataCum[12602]

    pdfFileObj.close()

    names = []
    pay = []
    jobs = []
    for k in range(0, len(dataCum)):
        if k % 3 == 0:
            names.append(dataCum[k])
        if k % 3 == 2:
            pay.append(dataCum[k])
        if k % 3 == 1:
            flagOriginal = True
            for u in range(len(jobs)):
                if jobs[u] == dataCum[k]:
                    flagOriginal=False
            if flagOriginal:
                jobs.append(dataCum[k])



    print(jobs)

    return jobs


main()
