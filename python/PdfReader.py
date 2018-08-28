import PyPDF2

f= open("/home/pignak/Scrivania/pdf1.txt","w+")

pdf_file = open('/home/pignak/Scrivania/pdf1.pdf',mode="rb")
read_pdf = PyPDF2.PdfFileReader(pdf_file)
np = read_pdf.getNumPages()
print("pagine: ",np)
for i in range(np):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    f.write("\n"+page_content)
print(page_content)
f.close()