import PyPDF2

# page 297

# # Read pdf
# pdfFileObj = open('data/watermarkedCover.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())



# # Encrypt
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addBlankPage(width=200, height=400)
# pdfWriter.encrypt('test')

# pathPdf = open('data/enc.pdf', 'wb')

# pdfWriter.write(pathPdf)
# pathPdf.close()



# # Rotate
# page = pdfReader.getPage(0)
# page = page.rotateClockwise(180)

# pdfWriter = PyPDF2.PdfFileWriter() 
# pdfWriter.addPage(page)
# resultPdfFile = open('data/rotatedPage.pdf', 'wb') 
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# pdfFileObj.close()

