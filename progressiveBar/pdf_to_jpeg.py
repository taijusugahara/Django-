from pdf2image import convert_from_path

images = convert_from_path('test.pdf',30)

images[0].save('out.jpeg')