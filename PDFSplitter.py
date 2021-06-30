import PyPDF2

pdf = 'test.pdf'
splits = [5,7]

fileObj = open(pdf,'rb')

readerObj = PyPDF2.PdfFileReader(fileObj)

s = 0
t = splits[0]

for i in range(len(splits)+1):
    pdfWObj = PyPDF2.PdfFileWriter()
    resultpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
    for p in range(s,t):
        pdfWObj.addPage(readerObj.getPage(p))
    with open(resultpdf,"wb") as f:
        pdfWObj.write(f)
    s = t
    try:
        t = splits[i+1]
    except:
        t = readerObj.numPages

fileObj.close()

print('Split Files Successfully!!')
