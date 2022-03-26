from docx2pdf import convert

inputFile = "sample1.docx"
outputFile = "document2.pdf"

# file = open(outputFile, "w")
# file.close()

# convert(inputFile, outputFile)
# convert(inputFile)
convert("Roboter.docx", "output.pdf")
# convert("docsfolder/")