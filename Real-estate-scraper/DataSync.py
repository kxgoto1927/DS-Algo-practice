import pdfkit
import time

from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def writeFooter(filename):
	outputPDF = PdfFileWriter()
	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	can = canvas.Canvas(packet, pagesize=letter)
	can.setFont("Helvetica", 11)
	# Writting the new line
	oknow = time.strftime("%m/%d/%y")
	can.drawString(27, 25, url)
	can.drawString(500, 25, oknow)
	can.save()
	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# read your existing PDF
	existing_pdf = PdfFileReader(file('PDF/test.pdf', "rb"))
	pages = existing_pdf.getNumPages()
	output = PdfFileWriter()
	# add the "watermark" (which is the new pdf) on the existing page
	for x in range(0,pages):
	    page = existing_pdf.getPage(x)
	    page.mergePage(new_pdf.getPage(0))
	    output.addPage(page)
	# finally, write "output" to a real file
	outputStream = file('PDF/' + filename, "wb")
	output.write(outputStream)
	outputStream.close()

def getPDF(index,onePID):
	filename = 'PDF/test.pdf'
	options = {
	'quiet': None
	}
	pdfkit.from_url(url, filename,options=options)
	PIDString = onePID[:2] + '-' + onePID[2:4] + '-' + onePID[4:7] + '-' + onePID[7:10] + '-' + onePID[10:14] + '.pdf'
	writeFooter(PIDString)
	print str(index) + ' / ' + str(len(PID))

text_file = open("input.txt", "r")
PID = text_file.read().split('\n')
start = time.time()
for index, onePID in enumerate(PID):
	url = 'http://www.cookcountyassessor.com/Property.aspx?mode=details&pin=' + onePID
	try:
		getPDF(index,onePID)
	except Exception as e:
		f = open('errorLog.txt', 'a')
		f.write('Exception: ' + str(e) + '\n')
		f.write('PID: ' + onePID + '\n')
		f.write('Iteration: ' + str(index) + ' / ' + str(len(PID)) + '\n')
		f.write('URL: ' + url + '\n')
		f.write('--------------------------------- \n')
		f.close()


end = time.time()
print(str(round(end - start,2))) + ' seconds'
