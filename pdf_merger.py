'''
Uses : Can be Helpful to Merge Pdf
How to Use: name the file as 1.pdf, 2.pdf, 3.pdf as to merge
            Put the file to merge in the same working directory where py file is placed
Output: merged_file.pdf
used lbr: PYPDF2
install: pip install PyPDF2
'''

import PyPDF2
import os

all_files = os.listdir()
print(all_files)
all_files.sort()
pdfWriter = PyPDF2.PdfFileWriter()
pdfOutputFile = open('merged_file.pdf', 'wb')

for file in all_files:
    if file.endswith(".pdf"):
        print(file)
        pdfFile = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            pdfWriter.addPage(pageObj)
        pdfWriter.write(pdfOutputFile)
        pdfFile.close()
    else:
        pass

pdfOutputFile.close()
