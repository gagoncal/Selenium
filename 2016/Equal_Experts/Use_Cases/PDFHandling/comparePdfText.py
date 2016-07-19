from ReadPdfFromUrl import PdfFromUrl
from pdftotext import PdfToText
##define an instance of PdfFrom Url object
pdffromUrl=PdfFromUrl()
##define an instance of PdfToText object
p2t=PdfToText()
##open first pdf file and save it as file1.pdf
pdffromUrl.open_pdf_from_url("http://www.seleniummaster.com/sitecontent/images/Selenium_Master_Test_Case_Base_Template.pdf","file1.pdf")
##open second pdf file and save it as file2.pdf
pdffromUrl.open_pdf_from_url("http://www.seleniummaster.com/sitecontent/images/Selenium_Master_TestCase_Modified_Template.pdf","file2.pdf")
##get texts of file1.pdf
textOfFile1=p2t.convert_pdf_to_txt("file1.pdf")
##get texts of file2.pdf
textOfFile2=p2t.convert_pdf_to_txt("file2.pdf")
##get length of file1.pdf texts
lengthOfTextFile1=len(textOfFile1)
##get length of file2.pdf texts
lengthOfTextFile2=len(textOfFile2)
##print text length information
print "Length of text of File1",lengthOfTextFile1
print "Length of text of File2",lengthOfTextFile2
##compare text length
if(lengthOfTextFile1==lengthOfTextFile2):
    print "Two pdf files' texts are the same"
else:
    print "Two pdf files' texts are different"


if __name__=="__main__":
        nose.main()