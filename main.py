from wand.image import Image as Img
import csv
import pytesseract as ocr
from PIL import Image
import os
import codecs
import pyocr
import pyocr.builders

#-----------------------------Convertendo o PDF em Imagem-----------------------------------------------------#
# with Img(filename='your_document.pdf', resolution=300) as img:
#     img.compression_quality = 99
#     img.save(filename='your_document.jpg')
#-------------------------------------------------------------------------------------------------------------#

# #---------------------------------Executando o OCR do seu documento-----------------------------------------#
tool = pyocr.get_available_tools()[0]
builder = pyocr.builders.TextBuilder()

txt0 = tool.image_to_string(Image.open('your_document.jpg'),lang='por',builder=builder)
print("Documento txt0 processado")

# #---------------------------------------Salvando no TXT-----------------------------------------------------#
with codecs.open("path_of_your_file", 'w', encoding='utf-8') as file_descriptor:
    builder.write_file(file_descriptor, txt0)
    print("Documento txt0 salvo")

# print("#-----------------Todos os documentos foram salvos em result.txt------------------------------------#")

