from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal

# Open a PDF file.
fp = open('final.pdf', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
document = PDFDocument()
parser.set_document(document)

# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
password=""
document.set_parser(parser)
document.initialize(password)

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

pages = list(document.get_pages())
#page_1 = pages[0] # 1st page
#page_1

fp.close()

fp = open('final.txt', 'w')

# interpreter pages
for page in pages:
    interpreter.process_page(page)

    # receive the LTPage object for the page.
    # layoutの中にページを構成する要素（LTTextBoxHorizontalなど）が入っている
    layout = device.get_result()
    #print(layout)
    
    for l in layout:
    #     print(l) # l is object
        if isinstance(l, LTTextBoxHorizontal):
            fp.write(l.get_text().replace('\n',' ').replace('- ',''))
	    #print(l.get_text().replace('-\n','')) # オブジェクト中のtextのみ

fp.close()
