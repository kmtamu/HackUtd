from django.db import models
import PyPDF2
import json
from docx import Document
from watson_developer_cloud import AlchemyLanguageV1
# Create your models here.
class random99():

    def mainmethod(self,fulltext):
        alchemy = AlchemyLanguageV1(api_key='27185a2ad5a2d610839c302e37d51e460657e99e')
        output = json.dumps(alchemy.combined(text=fulltext, extract='doc-emotion'))
        out2 = json.loads(output)
        ThisValueNeeded = out2['docEmotions']
        maximum = max(ThisValueNeeded, key=ThisValueNeeded.get)
        return {maximum: fulltext}
        #print(parameters)

    def convertPdf(self):

        pdfFileObj = open('document.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        num = pdfReader.numPages
        pageObj = pdfReader.getPage(2)
        fulltext = pageObj.extractText()
        someObject = random99()
        return someObject.mainmethod(fulltext)


