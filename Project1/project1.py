from PyPDF2 import PdfMerger

AllPDF = ['p1.pdf' , 'p2.pdf' , 'p3.pdf' ]

Ourmerger= PdfMerger()

for x in  AllPDF:
    Ourmerger.append(x)


Ourmerger.write('SwapnilCv.pdf')
Ourmerger.close()
