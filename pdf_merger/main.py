import PyPDF2

# List of PDF files to merge
pdfiles = ["1.pdf", "2.pdf"]

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    # Open the PDF file in binary mode
    with open(filename, 'rb') as pdfFile:
        # Append the PDF file to the merger
        merger.append(pdfFile)

# Write the merged PDF to a new file
merger.write('merged.pdf')
merger.close()
